import osmium
import networkx as nx
import pickle
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional
import numpy as np
from pyproj import Transformer

@dataclass
class OSMNode:
    id: int
    lat: float
    lon: float
    x: float  # UTM/ENU
    y: float

@dataclass
class OSMEdge:
    u: int
    v: int
    length: float
    heading: float  # radians, from u to v
    speed_limit: float  # m/s
    highway_type: str
    oneway: bool
    geometry: List[Tuple[float, float]]  # [(x, y), ...] for shape

class OSMGraphBuilder(osmium.SimpleHandler):
    """Build drivable road graph from OSM PBF"""
    
    # Highway types we consider drivable
    DRIVABLE_HIGHWAYS = {
        'motorway', 'trunk', 'primary', 'secondary', 'tertiary',
        'unclassified', 'residential', 'service', 'living_street',
        'motorway_link', 'trunk_link', 'primary_link', 'secondary_link', 'tertiary_link'
    }
    
    SPEED_LIMITS = {
        'motorway': 30.0,      # 108 km/h
        'trunk': 25.0,         # 90 km/h
        'primary': 20.0,       # 72 km/h
        'secondary': 15.0,     # 54 km/h
        'tertiary': 12.0,      # 43 km/h
        'unclassified': 10.0,  # 36 km/h
        'residential': 8.0,    # 29 km/h
        'service': 5.0,        # 18 km/h
        'living_street': 3.0,  # 11 km/h
    }
    
    def __init__(self, transformer: Transformer):
        super().__init__()
        self.transformer = transformer
        self.nodes: Dict[int, OSMNode] = {}
        self.edges: List[OSMEdge] = []
        self.way_nodes: List[int] = []
        self.current_way_tags: Dict[str, str] = {}
    
    def node(self, n):
        x, y = self.transformer.transform(n.location.lat, n.location.lon)
        self.nodes[n.id] = OSMNode(n.id, n.location.lat, n.location.lon, x, y)
    
    def way(self, w):
        highway = w.tags.get('highway')
        if highway not in self.DRIVABLE_HIGHWAYS:
            return
        
        oneway = w.tags.get('oneway') == 'yes'
        maxspeed = w.tags.get('maxspeed')
        speed_limit = float(maxspeed) / 3.6 if maxspeed else self.SPEED_LIMITS.get(highway, 10.0)
        
        # Get node sequence
        way_nodes = [n.ref for n in w.nodes]
        if len(way_nodes) < 2:
            return
        
        # Build edges between consecutive nodes
        for i in range(len(way_nodes) - 1):
            u, v = way_nodes[i], way_nodes[i+1]
            if u not in self.nodes or v not in self.nodes:
                continue
            
            nu, nv = self.nodes[u], self.nodes[v]
            
            # Length (haversine approx for short edges)
            dx = nv.x - nu.x
            dy = nv.y - nu.y
            length = np.hypot(dx, dy)
            heading = np.arctan2(dy, dx)  # radians, u->v
            
            # Geometry (interpolated for curved ways)
            geometry = [(nu.x, nu.y), (nv.x, nv.y)]
            
            self.edges.append(OSMEdge(
                u=u, v=v, length=length, heading=heading,
                speed_limit=speed_limit, highway_type=highway,
                oneway=oneway, geometry=geometry
            ))
            
            if not oneway:
                self.edges.append(OSMEdge(
                    u=v, v=u, length=length, heading=heading + np.pi,
                    speed_limit=speed_limit, highway_type=highway,
                    oneway=False, geometry=[(nv.x, nv.y), (nu.x, nu.y)]
                ))
    
    def build_networkx(self) -> nx.MultiDiGraph:
        """Convert to NetworkX graph with edge attributes"""
        G = nx.MultiDiGraph()
        
        # Add nodes
        for node in self.nodes.values():
            G.add_node(node.id, x=node.x, y=node.y, lat=node.lat, lon=node.lon)
        
        # Add edges
        for edge in self.edges:
            G.add_edge(
                edge.u, edge.v,
                length=edge.length,
                heading=edge.heading,
                speed_limit=edge.speed_limit,
                highway=edge.highway_type,
                geometry=edge.geometry
            )
        
        return G


def build_graph(pbf_path: str, output_path: str, city_bounds: Tuple[float, float, float, float] = None):
    """
    Build and save OSM graph
    city_bounds: (min_lat, min_lon, max_lat, max_lon) for clipping
    """
    # UTM zone for Indore (43R / EPSG:32643)
    transformer = Transformer.from_crs("epsg:4326", "epsg:32643", always_xy=True)
    
    handler = OSMGraphBuilder(transformer)
    handler.apply_file(pbf_path)
    
    G = handler.build_networkx()
    
    # Remove isolated nodes
    G.remove_nodes_from(list(nx.isolates(G)))
    
    # Save
    with open(output_path, 'wb') as f:
        pickle.dump(G, f)
    
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print(f"Saved to {output_path}")
    
    return G


if __name__ == "__main__":
    # Example: Download Indore PBF from Geofabrik
    # wget https://download.geofabrik.de/asia/india/central-india-latest.osm.pbf
    # build_graph("central-india-latest.osm.pbf", "indore_graph.pkl")
    pass