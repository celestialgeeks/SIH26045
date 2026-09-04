# SIH26168 — Seamless GNSS Handler + Dual-Rate Resampler
**Date:** 2026-09-03 | Researcher: @researcher | Iteration 2/4 — CLOSURE

---

## GNSS Handler (`gnss_handler/gnss_handler.py`)

| Aspect | Spec |
|---|---|
| Detect | `HDOP>3.0 OR sats<4 OR vel_conf<0.5 OR pos is None` → bad. Confirm 3 frames ( <200ms @10Hz) → `OUTAGE`. |
| On outage | `K_gnss=0`, inflate `Q×2`, keep `INS+NHC+ZUPT+Map` only, track `outage_duration`. |
| On recovery | Confirm 5 good frames. If `‖pos_gnss - p_ekf‖ > 3σ` → `hard_reseed` with `α=0.3` smoothing; else `soft_fusion` (adaptive R= R0*(1+2*HDOP)*0.5). No jumps. |
| Badge | `GNSS→DR 23s` vs `GNSS OK` for UI. |
| Thresholds | `hdop_thr=3.0, sats_thr=4, conf_thr=0.5, outage_confirm=3, recovery_confirm=5` — matches PS “seamless in ms, @10Hz”. |

Integration:
```python
handler=GnssHandler()
ekf=EKF()
for sample in stream:  # 10Hz
    info=handler.update(sample, t, ekf)
    ui.badge=handler.badge()
```

## Resampler (`resampler/resampler.py`)

| Aspect | Spec |
|---|---|
| Target | `100Hz` internal — single shared SpeedNet. |
| Phone 10Hz | `linear interp 10→100` → window `(200,6)` @10Hz SpeedNet cadence. |
| FOG 200Hz | `decimate/linear 200→100` → same `(200,6)` window; EKF predict still @200Hz. |
| Class | `DualRateIMU(native_hz)` buffers 3s, `get_100hz_window()` + `should_run_speednet(period=0.1)`. |
| Training | Train only at 100Hz resampled; augment with both rates → generalizes. |
| Demo | ICM-42688 @200Hz on laptop shows 200Hz curve on same UI (PS requires it). |

```python
phone=DualRateIMU(10); fog=DualRateIMU(200)
win=phone.get_100hz_window()  # (200,6) → SpeedNet → v_fwd
# EKF: phone predict @100Hz, fog predict @200Hz, SpeedNet @10Hz always
```

## Files

| File | Lines |
|---|---|
| `gnss_handler/gnss_handler.py` | 110 |
| `resampler/resampler.py` | 85 |
| `ekf/ekf.py` | 512 |
| `map_matching/map_matcher.py` | ~380 |

## Iteration 2 now 8/8 ✅

All Iteration 2 prototypes executable: `python -m pytest citation_validator`, `python resampler.py`, `python gnss_handler.py` smoke tests pass.

Next: **Iteration 3 — Integration testing + 60s tunnel demo + 90s Ayush demo + 6-slide PPT**.
