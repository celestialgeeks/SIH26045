import numpy as np
import networkx as nx
import pickle
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict
from scipy.spatial import cKDTree
import heapq

@dataclass
class Observation:
    """Single EKF observation for map matching"""
    timestamp: float
    pos: np.ndarray      # (2,) - ENU x,y
    pos_cov: np.ndarray  # (2, 2) - position covariance
    heading: float       # radians - vehicle heading (ENU)
    heading_std: float   # heading uncertainty
    speed: float         # m/s

@dataclass
class Candidate:
    """Candidate road edge for an observation"""
    edge_id: Tuple[int, int, int]  # (u, v, key) for MultiDiGraph
    u: int
    v: int
    length: float
    heading: float
    speed_limit: float
    dist_to_obs: float      # perpendicular distance to edge
    along_edge: float       # distance along edge from u
    proj_point: np.ndarray  # (2,) projected point on edge

@dataclass
class MatchedPath:
    """Result of Viterbi decoding"""
    edges: List[Tuple[int, int, int]]  # sequence of edge_ids
    log_prob: float
    states: List[Candidate]  # candidates at each timestep


class MapMatcher:
    """
    HMM Map Matcher with Viterbi + Multi-hypothesis
    
    States: Road edges (u, v, key)
    Observations: EKF position + heading
    Transition: Distance-based + heading alignment
    Emission: Gaussian on perpendicular distance + heading difference
    """
    
    def __init__(self, graph_path: str, search_radius: float = 50.0):
        with open(graph_path, 'rb') as f:
            self.G = pickle.load(f)
        
        self.search_radius = search_radius
        
        # Build edge index for fast candidate search
        self._build_edge_index()
        
        # Transition params
        self.sigma_dist = 10.0      # transition distance sigma [m]
        self.sigma_heading = 0.3    # transition heading sigma [rad]
        
        # Emission params
        self.sigma_emission_pos = 15.0  # position emission sigma [m]
        self.sigma_emission_head = 0.5  # heading emission sigma [rad]
        
        # Multi-hypothesis
        self.max_hypotheses = 2
        self.hypothesis_heading_gate = 25.0 * np.pi / 180  # 25 deg
        self.hypothesis_time_window = 3.0  # seconds
    
    def _build_edge_index(self):
        """Build KD-tree on edge midpoints for fast candidate search"""
        self.edge_midpoints = []
        self.edge_list = []
        
        for u, v, key, data in self.G.edges(keys=True, data=True):
            x1, y1 = self.G.nodes[u]['x'], self.G.nodes[u]['y']
            x2, y2 = self.G.nodes[v]['x'], self.G.nodes[v]['y']
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            self.edge_midpoints.append([mid_x, mid_y])
            self.edge_list.append((u, v, key, data))
        
        self.edge_midpoints = np.array(self.edge_midpoints)
        self.kdtree = cKDTree(self.edge_midpoints)
    
    def _get_candidates(self, obs: Observation, k: int = 10) -> List[Candidate]:
        """Find k nearest road edges to observation"""
        # KD-tree query
        dists, indices = self.kdtree.query([obs.pos], k=min(k, len(self.edge_list)))
        dists = dists[0] if len(dists.shape) > 1 else dists
        indices = indices[0] if len(indices.shape) > 1 else indices
        
        candidates = []
        for idx, d in zip(indices, dists):
            if d > self.search_radius:
                continue
            
            u, v, key, data = self.edge_list[idx]
            
            # Project observation onto edge
            x1, y1 = self.G.nodes[u]['x'], self.G.nodes[u]['y']
            x2, y2 = self.G.nodes[v]['x'], self.G.nodes[v]['y']
            
            # Edge vector
            ex, ey = x2 - x1, y2 - y1
            edge_len = np.hypot(ex, ey)
            if edge_len < 1e-6:
                continue
            
            # Projection parameter t
            ox, oy = obs.pos[0] - x1, obs.pos[1] - y1
            t = (ox * ex + oy * ey) / (edge_len ** 2)
            t = np.clip(t, 0, 1)
            
            # Projected point
            proj_x = x1 + t * ex
            proj_y = y1 + t * ey
            proj_point = np.array([proj_x, proj_y])
            
            # Perpendicular distance
            perp_dist = np.hypot(obs.pos[0] - proj_x, obs.pos[1] - proj_y)
            
            # Along-edge distance from u
            along = t * edge_len
            
            # Heading difference
            heading_diff = self._angle_diff(obs.heading, data['heading'])
            
            candidates.append(Candidate(
                edge_id=(u, v, key),
                u=u, v=v,
                length=edge_len,
                heading=data['heading'],
                speed_limit=data['speed_limit'],
                dist_to_obs=perp_dist,
                along_edge=along,
                proj_point=proj_point
            ))
        
        # Sort by combined score (distance + heading)
        candidates.sort(key=lambda c: c.dist_to_obs + 10 * abs(self._angle_diff(obs.heading, c.heading)))
        return candidates[:k]
    
    @staticmethod
    def _angle_diff(a: float, b: float) -> float:
        """Signed angle difference in [-pi, pi]"""
        diff = a - b
        while diff > np.pi:
            diff -= 2 * np.pi
        while diff < -np.pi:
            diff += 2 * np.pi
        return diff
    
    def _emission_logprob(self, obs: Observation, cand: Candidate) -> float:
        """Log probability of observation given candidate edge"""
        # Position: Gaussian on perpendicular distance
        pos_ll = -0.5 * (cand.dist_to_obs / self.sigma_emission_pos) ** 2
        
        # Heading: Gaussian on heading difference
        heading_diff = self._angle_diff(obs.heading, cand.heading)
        head_ll = -0.5 * (heading_diff / self.sigma_emission_head) ** 2
        
        # Speed consistency (soft)
        speed_ratio = obs.speed / max(cand.speed_limit, 1.0)
        speed_ll = -0.5 * ((speed_ratio - 1.0) / 0.3) ** 2 if obs.speed > 1.0 else 0
        
        return pos_ll + head_ll + speed_ll
    
    def _transition_logprob(self, cand_prev: Candidate, cand_curr: Candidate, 
                            dt: float, obs_speed: float) -> float:
        """Log probability of transition between candidate edges"""
        # If same edge, high probability
        if cand_prev.edge_id == cand_curr.edge_id:
            return 0.0  # log(1) = 0
        
        # Check connectivity: prev.v == curr.u
        if cand_prev.v != cand_curr.u:
            # Not connected - check if close in space (U-turn, parallel roads)
            dist = np.hypot(
                cand_prev.proj_point[0] - cand_curr.proj_point[0],
                cand_prev.proj_point[1] - cand_curr.proj_point[1]
            )
            if dist > 20.0:  # too far
                return -np.inf
        
        # Distance traveled along path
        expected_dist = obs_speed * dt
        actual_dist = cand_curr.along_edge + (cand_curr.length - cand_prev.along_edge) if cand_prev.v == cand_curr.u else 0
        
        dist_ll = -0.5 * ((actual_dist - expected_dist) / self.sigma_dist) ** 2
        
        # Heading continuity
        heading_diff = self._angle_diff(cand_prev.heading, cand_curr.heading)
        head_ll = -0.5 * (heading_diff / self.sigma_heading) ** 2
        
        return dist_ll + head_ll
    
    def viterbi(self, observations: List[Observation]) -> List[MatchedPath]:
        """Viterbi decoding with multi-hypothesis"""
        if not observations:
            return []
        
        T = len(observations)
        
        # Get candidates for each observation
        all_candidates = [self._get_candidates(obs) for obs in observations]
        
        if any(len(c) == 0 for c in all_candidates):
            return []
        
        # Initialize: log-prob, backpointer, hypothesis_id
        # dp[t][i][h] = (log_prob, prev_cand_idx, prev_hypothesis)
        dp = [[{} for _ in range(len(all_candidates[t]))] for t in range(T)]
        
        # t=0: initialize all candidates
        for i, cand in enumerate(all_candidates[0]):
            log_prob = self._emission_logprob(observations[0], cand)
            dp[0][i][0] = (log_prob, -1, -1)  # hypothesis 0
        
        # Forward pass
        for t in range(1, T):
            dt = observations[t].timestamp - observations[t-1].timestamp
            
            for i, cand_curr in enumerate(all_candidates[t]):
                emission_ll = self._emission_logprob(observations[t], cand_curr)
                
                # Consider transitions from all previous candidates
                transitions = []
                for j, cand_prev in enumerate(all_candidates[t-1]):
                    for h, (prev_prob, _, _) in dp[t-1][j].items():
                        trans_ll = self._transition_logprob(cand_prev, cand_curr, dt, observations[t].speed)
                        if trans_ll > -np.inf:
                            total_ll = prev_prob + trans_ll + emission_ll
                            transitions.append((total_ll, j, h))
                
                # Keep top max_hypotheses
                transitions.sort(key=lambda x: x[0], reverse=True)
                for h, (prob, j, h_prev) in enumerate(transitions[:self.max_hypotheses]):
                    dp[t][i][h] = (prob, j, h_prev)
        
        # Backtrack for each hypothesis at final timestep
        hypotheses = []
        final_t = T - 1
        
        # Collect all final states
        final_states = []
        for i in range(len(all_candidates[final_t])):
            for h, (prob, j, h_prev) in dp[final_t][i].items():
                final_states.append((prob, i, h, j, h_prev))
        
        final_states.sort(key=lambda x: x[0], reverse=True)
        
        # Backtrack top hypotheses
        for prob, i, h, j, h_prev in final_states[:self.max_hypotheses]:
            edges = []
            states = []
            curr_i, curr_h = i, h
            
            for t in range(final_t, -1, -1):
                cand = all_candidates[t][curr_i]
                edges.append(cand.edge_id)
                states.append(cand)
                
                if t > 0:
                    _, prev_i, prev_h = dp[t][curr_i][curr_h]
                    curr_i, curr_h = prev_i, prev_h
            
            edges.reverse()
            states.reverse()
            hypotheses.append(MatchedPath(edges=edges, log_prob=prob, states=states))
        
        return hypotheses
    
    def get_pseudo_measurement(self, matched_path: MatchedPath, 
                                obs: Observation) -> Tuple[np.ndarray, np.ndarray]:
        """Convert matched path to pseudo-measurement for EKF"""
        if not matched_path.states:
            return obs.pos, obs.pos_cov
        
        # Weighted average of projected points (weight by emission prob)
        weights = []
        points = []
        
        for cand in matched_path.states:
            emission_ll = self._emission_logprob(obs, cand)
            weight = np.exp(emission_ll)
            weights.append(weight)
            points.append(cand.proj_point)
        
        weights = np.array(weights)
        weights = weights / (weights.sum() + 1e-10)
        points = np.array(points)  # (n_candidates, 2)
        
        mean_pos = np.average(points, axis=0, weights=weights)
        
        # Covariance: weighted covariance + emission noise
        centered = points - mean_pos
        cov = np.zeros((2, 2))
        for w, c in zip(weights, centered):
            cov += w * np.outer(c, c)
        cov += np.eye(2) * (self.sigma_emission_pos ** 2)
        
        return mean_pos, cov


def match_trajectory(graph_path: str, ekf_trajectory: List[Observation]) -> List[MatchedPath]:
    """High-level function to match full trajectory"""
    matcher = MapMatcher(graph_path)
    return matcher.viterbi(ekf_trajectory)


if __name__ == "__main__":
    # Quick test with synthetic data
    import tempfile
    import os
    
    # Create minimal test graph
    G = nx.MultiDiGraph()
    G.add_node(1, x=0, y=0)
    G.add_node(2, x=100, y=0)
    G.add_node(3, x=100, y=100)
    G.add_edge(1, 2, length=100, heading=0, speed_limit=10, highway='residential')
    G.add_edge(2, 3, length=100, heading=np.pi/2, speed_limit=10, highway='residential')
    
    with tempfile.NamedTemporaryFile(suffix='.pkl', delete=False) as f:
        pickle.dump(G, f)
        graph_path = f.name
    
    # Synthetic observations along the L-shape
    obs = [
        Observation(0.0, np.array([10, 1]), np.eye(2)*25, 0, 0.1, 5),
        Observation(1.0, np.array([30, 2]), np.eye(2)*25, 0, 0.1, 5),
        Observation(2.0, np.array([50, 1]), np.eye(2)*25, 0, 0.1, 5),
        Observation(3.0, np.array([70, 0]), np.eye(2)*25, 0, 0.1, 5),
        Observation(4.0, np.array([90, -1]), np.eye(2)*25, 0, 0.1, 5),
        Observation(5.0, np.array([100, 10]), np.eye(2)*25, np.pi/2, 0.1, 5),
        Observation(6.0, np.array([100, 30]), np.eye(2)*25, np.pi/2, 0.1, 5),
    ]
    
    matcher = MapMatcher(graph_path)
    paths = matcher.viterbi(obs)
    
    print(f"Found {len(paths)} hypotheses")
    for i, path in enumerate(paths):
        print(f"Hypothesis {i}: log_prob={path.log_prob:.2f}, edges={path.edges}")
        pos, cov = matcher.get_pseudo_measurement(path, obs[3])
        print(f"  Pseudo-measurement at t=3: pos={pos}, cov_diag={np.diag(cov)}")
    
    os.unlink(graph_path)