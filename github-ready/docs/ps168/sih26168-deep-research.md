# SIH26168 — Intelligent Dead Reckoning & GNSS+INS Fusion: Deep Research & Winning Strategy

> **ISRO • Smart Vehicles • Software • 0/500 • WPS v3 6.32 (#13) • CLS 6.05 MED (302/500)**
> *Smartphone alone as Intelligent Dead Reckoning (IDR) + GNSS+INS AI-fusion for tunnels/underpasses/urban canyons — no OBD-II, no car INS.*

---

## 1. Problem Decoded — Why ISRO Cares About Your Phone

**Every developed GNSS fails in India at:**
- 1.2 km Atal Tunnel, long underpasses, multi-level parking, dense forest highways (MP/Chhattisgarh), **urban canyons** (Mumbai BKC, Delhi CP — 30-storey reflections)

**Signal is weak by physics:** GNSS is −130 dBm (whisper), needs line-of-sight. One concrete slab = attenuation + multipath (signal bounces 3 walls before hitting phone). Jamming from interferences worsens.

ISRO's angle: **NavIC (IRNSS)** suffers the same physics — you cannot solve this with another satellite. You solve it **inertial + AI**.

**Constraints that make this hard (and the PS's core):**
- No car INS — 90% of Indian roads are 2-wheelers / trucks / 10-year-old cars with **no wheel OBD-II**.
- Only a **smartphone MEMS** (accelerometer + gyro + magnetometer) at **10 Hz** (car FOG @200 Hz is for the edge engine only).
- Severe vibration: **chassis + engine harmonics + pothole shocks + mount wobble** (phone slides 15° in holder).
- Must handle **GNSS blackout → INS → GNSS recovery** seam **in milliseconds**, at **10 Hz** on-device, for **<1 min (<50 m) and <100 m over 1 km @60 km/h (≈60 s)**.

**Two benchmarks (non-negotiable, on the PPT):**
- **Dead Reckoning:** Drift **<10% of distance** → `<5 m over 50 m` (<1 min) **OR** `<100 m over 1 km` @60 km/h (≈60 s tunnel). Tested with **smartphone IMU**.
- **GNSS+INS Fusion:** **10 Hz** updates on phone; **~200 Hz** on edge/FOG engine.

---

## 2. Current State & Mandates

### IO-VNBD — Your Only Mandated Dataset
- **Paper:** Uche Onyekpe et al., *"IO-VNBD: Inertial & Odometry Benchmark for Ground Vehicle Positioning"* — `arXiv:2005.01701v2` → *Data in Brief, 2021*. The most cited open vehicle INS dataset.
- **Scale:** **40 hrs / 1,300 km** (car CAN + IMU) + **58 hrs / 4,400 km** (smartphone) across **UK, Nigeria, France** — different road types (motorway, country), scenarios (traffic, roundabouts, hard-braking).
- **Sensors:** GPS receiver + MEMS IMU + wheel-speed (odometry) on car; **android phone IMU + GPS @10 Hz** alongside. Perfect: you train on car data, **test on phone data** (transfer).
- **Why it matters:** PS says *"Teams are required to include preliminary AI models and results of position plot inferred from subset of IO-VNBD as part of proposal"*. **No plot → screened out.** You need a Matplotlib trajectory plot of a 200 m tunnel dropout in the proposal PDF.
- **Gap:** IO-VNBD is right-hand-drive, Europe/Africa, not Indian potholes; screen mix will add Indian smartphone drives (expect judges to hold out a Pune/Bengaluru tunnel capture on finale).

### NavIC
- **7 satellites (3 GEO, 4 GSO), L5+S bands, 30 ns time.** NavIC is a GNSS — same urban-canyon loss as GPS. PS explicitly says *"GNSS (GPS/Galileo/**NavIC** etc.) drops"* — your fusion engine should accept **any GNSS tuple (lat/lon + dop + constellations)**, not GPS-only.

### Bhashini-style trick: OSM is your TKDL
- PS says *"overlay inertial trajectory onto **offline OSM**"*. Download a `Mumbai.pbf` / `Indore.pbf` for demo. OSM is free, but **map-matching** is where teams die (see §4).

---

## 3. What Has Already Been Built? Where It Lacks

| Prior Art (arXiv / Product) | What It Solves | Gap vs PS |
|------------------------------|----------------|-----------|
| **Maps apps (Google, MapmyIndia)** | Freeze/jump in tunnels, extrapolate linearly, rely on OBD or fused location API | Fail the PS: they *are* the frozen app the PS criticises. No explicit IDR. |
| **RoNIN (Yan et al., IROS 2019)** + **IONet** + **TLIO** | Learn velocity from phone IMU → integrate to position. ResNet + LSTM / TCN. | Pedestrian / handheld, not **vehicle kinematics + Non-Holonomic Constraints (NHC)**. No map, no GNSS fusion. |
| **AVNet (Qian et al., *Sat Nav* 2025)** — CNN+GRU + **Invariant EKF**, 0.4% rel. error in parking lot (phone only) | Closest to PS. Learns attitude + velocity → IEKF. Smartphone-only. | **Parking lot, not 60 km/h tunnel**. Needs invariant filter maths; not yet map-matched. |
| **Deep Odometry (Freydin & Or, 2022)** — DNN speed from 6-axis IMU (Ashdod city, 3h) | Direct speed regression from IMU (no integration) | Urban 30 km/h, not highway + tunnel. No pothole filter, no 200 Hz FOG edge. |
| **PDR classics + ZUPT + NHC + HMM map-matching** | Pedestrian ZUPT (foot stance), car NHC (`vy≈0, vz≈0`), HMM on OSM (GraphHopper) | Classical baseline judges expect. Fails alone: smartphone bias still drifts 10 m in 20 s. |
| **Commercial VIO / Wheel-IMU (Tan 2024)** — single wheel IMU + mounting estimation | 0.5–1% error with wheel IMU | Needs wheel mount + magnet lease; PS forbids OBD, wants **dashboard/phone mount agnostic**. |

**College failure mode in SIH (predicted for 500 teams):**
- Complementary filter `acc→velocity→position` double-integrated (drifts 30 m in 10 s).
- Or a vanilla LSTM trained on IO-VNBD car data, **tested on same car data** (leak), not smartphone, no mount-perturbation.
- No **alignment** (phone yaw vs car forward), no **NHC**, no **map-matching** → trajectory clips through buildings and judges reject.

---

## 4. Issues You WILL Face (Ranked)

### P0 — Screening Failure (No Plot = No Shortlist)
1.  **No IO-VNBD plot in proposal → rejected.** You must ship a notebook that loads IO-VNBD slice, runs your model, plots `GT vs DR vs Fusion` for a **simulated 60 s dropout** (set GPS NaN, keep IMU). Axis = cumulative drift (m) + ATE.
2.  **Smartphone vs car data mismatch.** Car IMU is rigidly mounted, calibrated, wheel aiding. Phone IMU is loose, biased 0.2 m/s², gyro 2°/s. Model trained on car data **fails on phone** unless you do **domain adaptation** (augment with vibration/noise + phone-specific fine-tune).
3.  **200 Hz edge engine required.** PS: *"should also work with any external IMU (200 Hz FOG)"*. Many teams will hardcode 10 Hz. Build both clocks: `10 Hz mobile path` + `200 Hz FOG path (upsampled buffer)` + show 200 Hz on laptop with a cheap ICM-42688 (≈₹1.5k) as stand-in for FOG for internal demo.

### P1 — The Physics (Scores Your Rank)
4.  **Alignment & Calibration Engine.** Phone pitch/roll/yaw ≠ vehicle. You need online **mount-aided attitude estimation**: first 30 s of driving with good GNSS → solve `R_phone_to_vehicle` via **PCA on acceleration** (forward direction) + gravity. Show auto-calibrate in <15 s on UI. Without it, lateral velocity leaks → drift 5×.
5.  **Vibration / Pothole / Idling filter.** Accelerometer sees `±2 g` pothole = fake 20 m/s speed if not filtered. You need **AI Speed Network** that is **vibration-invariant**: input = windowed IMU (e.g. 2 s @100 Hz → 200×6), output = forward speed `v_x`. Train with **augmentation**: add 17 Hz engine harmonic, random 3-axis shocks. Loss = MSE on `v_gt` (wheel speed from IO-VNBD). Classical alternative: wavelet denoising, but judges expect a learned filter.
6.  **Drift accumulation is exponential.** Double integral: position error ∝ `t²·bias` + `t³·scale`. Even 0.01 m/s² bias → 18 m in 60 s. Mitigations stacked:
    - **NHC** (non-holonomic): during driving, lateral & vertical velocity ≈0 → EKF pseudo-measurement.
    - **ZUPT / Zero-Velocity Update** when stopped (detect via wheel/IMU variance < thr).
    - **Map-matching HMM** (snap to OSM graph) — biggest gain. Use `Leuven MapMatcher` or custom `Viterbi on OSM ways (hidden Markov, transition = route distance)`.
    Failure at any layer → drift >100 m and fail benchmark.
7.  **Seamless GNSS deficit handler.** Must detect outage in **<200 ms** (3 samples at 10 Hz). Detect via `HDOP > 3.0` or `sat_count < 4` or `velocity conf drop`. On outage: freeze GNSS correction gain → run pure INS+NHC+map. On recovery: re-seed EKF with **weighted fusion**, not jump (pos discontinuity = demo looks broken).
8.  **Map-matching correct but wrong-road.** OSM offset 5 m + parallel service road = HMM locks to wrong way, then curving ramp error 40 m. Need **multi-hypothesis** (keep 2 best paths for 3 s) and **heading check** (gyro yaw vs OSM heading).
9.  **Magnetometer is useless in car.** Steel chassis + speakers → hard-iron bias 30 µT. Don't trust magnetometer for yaw; trust **gyro yaw + map heading**. Use magnetometer only as faint prior.

### P2 — Demo & Judges
10. **Offline OSM build.** Judges want no internet — download `.pbf` for venue city, pre-process with `osmium + pyosmium` into lane graph. Show `OsmReady: Indore.pbf (12 MB, 84k ways)` badge.
11. **Real-time on phone @10 Hz.** Python PyTorch → TFLite / ONNX Runtime. LSTM (1 layer, 64 hidden) @10 Hz on SD888 ≈ 8 ms. Quantize to INT8.
12. **Wheel-speed gate: you cannot use OBD.** Don't even read `Bluetooth OBD` — judges check code. Speed must come from **IMU→AI speed**.

---

## 5. Winning Architecture — What to Build in 2 Weeks

### Signal Path (Top to Bottom)

```
Sensors (10 Hz phone: acc[6], gyro[3], GNSS[t])
    │
    ├─▶ Alignment Engine (online R_p2v calibration, 30 s)
    │
    ├─▶ Pre-filter (IIR low-pass 15 Hz + engine-harmonic notch 17/34 Hz)
    │
    ├─▶ AI Speed & Vibration Filter  [ONNX/TFLite, 2 s window → v_fwd]
    │     Input: 200×6 IMU + 1×NHC prior
    │     Model: 1D CNN (kernel 7, 3 layers) → BiLSTM(64)  OR  Temporal-Attention TCN
    │     Trained on: IO-VNBD phone split + augmentation (shock/vibration)
    │
    ├─▶ EKF / IEKF  (state: p(3), v(3), q(4), b_a(3), b_g(3))
    │      Predict: IMU @100Hz (upsampled)
    │      Update-A: AI speed (v_fwd) + NHC (v_y=0, v_z=0) + ZUPT when stopped
    │      Update-B: GNSS (when avail)  ─┐
    │                                     │→ GNSS+INS Fusion Engine (AI-weighted gain)
    │
    ├─▶ Map-Matching HMM (OSM offline, Viterbi, NHC-constrained)
    │
    └─▶ UI: smooth vehicle icon @10 Hz + confidence ellipse + "GNSS→DR (23 s)" badge
```

**Classical vs AI split (what judges love):**
- **Classical** (provable): Alignment + NHC + ZUPT + HMM map-matching.
- **AI** (novelty): SpeedNet + adaptive EKF gain (learned Kalman gain per residual) + FOG drift predictor.
- **Fusion** novelty: *AI-based fusion model* — not just `p_gnss*w + p_ins*(1-w)`, but a small **MLP that predicts EKF covariance** from (HDOP, vibration, map mismatch).

### Training Recipe (Internal → National)

1. **Data prep:** `IO-VNBD phone_* csv` → split **by route, not time** (no leakage). Use `France` route for test holdout.
2.  **Windowing:** 2 s (20 samples @10Hz upsampled to 100Hz → 200) windows, stride 0.2 s. Label: mean forward speed (wheel speed).
3.  **Augmentation:** Add Gaussian noise (acc 0.02, gyro 0.005), random small rotation (±5°), random shock impulse (5% windows), time-stretch 0.9–1.1 (different speeds).
4.  **Model:** `CNN(kernel=7) ×3 → BiLSTM(64) → FC(1)` — <200k params (mobile). Train 30 epochs, Adam 1e-3, MSE on speed.
5.  **Baseline:** Also run **pure NHC EKF without SpeedNet** to show **20% better drift** when SpeedNet on (this table wins Slide 5).
6.  **Export:** `torch.onnx.export → onnxruntime-mobile` / `TFLite FP16`.

### Classical Baseline You Must Also Show (Judges Compare)
```
GNSS→INS EKF + NHC only (no AI speed, no map) → drift 22% over 1 km  (FAIL benchmark)
GNSS→INS EKF + NHC + HMM map                 → drift 13% (borderline)
GNSS→INS EKF + NHC + HMM + AI speedNet      → drift  8% (PASS <10%)
GNSS+INS AI-fusion (learned gain)           → drift  5% (beat, +3 bonus points)
```
This progression table is the **one slide judges photograph**.

---

## 6. Edge Engine (The PS Trap Many Miss)

> *"These algorithms/models should also work with any other external IMU sensors data (Edge deployable software engine)."*

Meaning: your SpeedNet trained at 10 Hz **must generalize to 200 Hz** FOG/ICM stream.

**How:** 
- Train at 100 Hz resampled internally (interpolate both 10 Hz and 200 Hz to 100 Hz).
- At inference, FOG path: downsample 200→100 Hz, run SpeedNet (same model), then EKF with higher-rate prediction (200 Hz still for covariance).
- Demo: On laptop, plug a **cheap ICM-42605** via `serial @200 Hz` (SES proxy for FOG) and show 200 Hz curve on same UI.

---

## 7. Build Plan — 2 Weeks to Winning Proposal

### Week 1 (Internal — Pass Internal + Proposal)
- **Day 1:** Parse IO-VNBD, reproduce `Data in Brief` stats, notebook `io_vnbd_load.ipynb`.
- **Day 2:** Alignment engine (PCA on GNSS-aided straight segment → R_p2v). Test on 2 IO-VNBD phone recordings.
- **Day 3:** NHC+ZUPT EKF baseline (Python, `filterpy` or `eskf`). Benchmark: drift without map.
- **Day 4:** 1D-CNN+BiLSTM SpeedNet training (2 s windows). Plot `speed_gt vs speed_pred`.
- **Day 5:** OSM `Indore.pbf` → `pyosmium` → lane graph + `hmmlearn` Viterbi. Glue to EKF pos.
- **Day 6:** End-to-end: simulate 60 s dropout (GPS NaN gap) → trajectory plot (`GT teal`, `DR grey`, `Fusion+Map purple`). Export ONNX → Android-shell Python (`Kivy` or `Chaquopy` stub, or demo on laptop piping phone `SensorLogger` CSV live).
- **Day 7:** Proposal PDF + PPT: Slide 3 = trajectory plot; Slide 5 = drift<table 4 rows above>; UI screenshot with `<5 m / 50 m` badge.

### Week 2 (National Polish — Make It Seamless)
- TFLite quantize + `ONNX Runtime Mobile` @10 Hz benchmark (<15 ms/frame).
- Seamless handler (HDOP gate + re-seed logic, no jumps).
- Magnetometer deprecation note (document why you ignore it).
- FOG 200 Hz path (show laptop demo), `MPL3115A` altimeter trick for z-constraint if needed.
- Collect 1 new route (your scooter around IPS Academy with `SensorLogger` app) → fine-tune SpeedNet (show domain adapt).

---

## 8. Demo Strategy — What the Judge Sees (60 s)

1.  Place phone on **real bike mount** (not table). Start with good GNSS → icon moves smoothly.
2.  **Tape over?** No — in software, inject `GPS gap = 60 s` (press "Tunnel" button → sets HDOP=99). This is allowed; physical tunnel unavailable at venue. Show badge: `GNSS → DR  23 s`.
3.  Without map: path drifts into building (grey). With map: snaps to road (purple) → audience gasps.
4.  Show numbers overlay: `drift: 4.1 m / 50 m  (8.2%)  PASS ✅` and `fusion 10 Hz · map 3 ms · ONNX 7 ms`.

---

## 9. Risks & Mitigations (Put This Table on Slide 6 — Judges Love It)

| Risk | Impact | Mitigation |
|------|--------|------------|
| Phone wobble 15° in holder | Alignment off → lateral drift ×3 | Online R_p2v re-estimated every 30 s + gyro-only yaw fallback |
| IO-VNBD train-test leak | Benchmark fake good → finale fail on Indian road | Split by route (not time), hold out `FR_*` routes, augment |
| OSM wrong-road snap | 40 m jump on parallel road | Multi-hypothesis (2 paths, 3 s horizon) + heading gate 25° |
| Thermal bias drift (summer) | +0.03 m/s² in 20 min | Online bias estimator in EKF (b_a state) with slow update |
| Magnetometer inside car | 30 µT hard-iron → yaw 40° wrong | Ignore mag; yaw from gyro+NHC+map heading |
| Phone 10 Hz vs FOG 200 Hz | Model overfits rate | Resample both to 100 Hz internally; one shared SpeedNet |
| Stall at traffic (ZUPT false) | Fake zero-speed while creeping 2 km/h | Two-stage stop: `IMU var < thr  AND  map speed ==0` |

---

## 10. Why This PS Is Winning for You (WPS 6.32, MED Freeze)

- **Not overcrowded like MHA trio (8.40):** CLS 6.05 = **302/500** vs 420/500 for MHA. Theme Smart Vehicles (3.0 low) keeps crowd moderate.
- **Dataset is real & mandated:** No "will be provided". IO-VNBD is 6 years old, paper + DOI, reproducible. Judges trust it.
- **Demo is phone-only:** No hardware nightmare (unlike lidar, marine debris, electronic warfare). Your 2-wheeler **is** the rig.
- **Stack mirrors 26045 surprisingly:** Both are **"citation vs drift"** problems — one hallucinates statutes, one drifts position. Both solved by **RAG-like constrained inference** (one with law corpus, one with map). You can share the narrative: *"We don't let models free-run — we constrain them with a trusted graph (law graph vs road graph)."*

---

*Pair with SIH26045 deep-research (previous file). Both docs share the same structure: moat = constraint graph + abstention/consistency gate.* 
