# SIH26168 — Map-Matching HMM on OSM (Offline)
**Date:** 2026-09-03 | Researcher: @researcher | Iteration 2/4

> Prototype: `projects/sih26/prototype/map_matching/map_matcher.py` (13K, landed) — this doc is spec + demo plan.

---

## 1. Offline Graph Build (no internet at venue)

```bash
# Download once (Geofabrik) — use Indore as IPS Academy demo city
wget https://download.geofabrik.de/asia/india-latest.osm.pbf -O indore.osm.pbf  # clip later
# or city extract via bbbike.org
osmium extract -b 75.8,22.6,76.0,22.8 india-latest.osm.pbf -o indore.pbf
```

```python
# map_matcher.py:build_graph(pbf_path)
import pyosmium, networkx as nx
# Keep only drivable: highway in [motorway,trunk,primary,secondary,tertiary,residential,unclassified,service]
# Node = OSM node (lat,lon), Edge = way segment with attrs {length, heading, maxspeed, oneway}
# Output: DiGraph 12 MB for Indore ≈84k ways, 220k edges
# Save as indore.graph.pkl + show badge: "OsmReady: Indore.pbf (12 MB, 84k ways)"
```

## 2. HMM Model

- **Hidden states:** graph edges (road segments) within 50m of EKF pos
- **Observation:** `o_t = (p_ekf, heading_ekf, cov)` at 3 Hz (downsampled from 10 Hz)
- **Emission:** `p(o|s) = N( dist(p_ekf, proj(p_ekf,s)) ; 0, σ=8m ) * VonMises( Δheading ; κ=4 )`
- **Transition:** `p(s_j|s_i) ∝ exp(-|route_dist(s_i,s_j) - euclid(p_i,p_j)| / β) * heading_align` with `β=5m`, penalize U-turns

## 3. Viterbi + Multi-Hypothesis

```python
# Single best path
path = viterbi(observations, candidates, trans, emit)  # returns edge sequence

# Multi-hypothesis (keeps 2 best paths for 3s, heading gate 25°)
# At parallel service road offset 5m, wrong snap → 40m ramp error if not.
# Keep top-2, propagate 3s, pick max posterior * heading_consistency.
paths = multi_hypothesis_viterbi(..., k=2, horizon=9)  # 9 steps @3Hz =3s
best = max(paths, key=lambda p: score(p) * (1 if heading_delta(p)<25° else 0.1))
projected = project(p_ekf, best[-1])  # snap to road
```

Library: `hmmlearn` or custom Viterbi (map_matcher.py has both). Complexity ~30ms/frame.

## 4. Pseudo-measurement to EKF

```
p_map = projected  # (x,y) + keep EKF z
Send to ekf.update_map(p_map, R_map=diag([2,2,4]))
# Only when match confidence >0.7 and distance <15m
```

## 5. Demo trick (judge sees)

Without map: trajectory drifts into building (grey). With map: snaps to road (purple). The 60s tunnel button injects HDOP=99 gap — map keeps icon on road, drift badge `4.1m/50m PASS ✅`.

## 6. Gotchas

- OSM offset 5m → multi-hypothesis fixes wrong-road lock.
- Magnetometer ignored (hard-iron 30µT) — yaw from gyro+map heading.
- Offline: ship `indore.pbf + indore.graph.pkl` in repo, badge it on slide.
