# SIH26186 — Deep Research (Iteration-1 Draft)
> **MHA • MedTech / BioTech / HealthTech • Software • 0/500 • WPS 6.11 #27 • CLS 6.90 HIGH (WORKABLE)**
> Pair: SIH26045 × SIH26186. Chosen by @researcher (replaces 26168).

> **NOTE:** This is a working draft assembled before Worker A–E complete. It will be rewritten with their findings. Sources are pre-cached from search results; the final version will use the ledger via `sources.py`.

## 1. Problem Decoded — What MHA Really Wants
Uniformed forces (CAPFs, Armed Forces, paramilitary) face prolonged deployments, irregular shifts, operational trauma, and family separation — all strong burnout drivers. Current stress detection is manual + self-report, delayed and stigmatizing. MHA wants a **predictive, privacy-preserving, welfare-first** platform that:
1. Predicts burnout risk early (not just detects current stress)
2. Recommends welfare interventions (counseling, workload rebalancing)
3. Integrates with existing HRMS/personnel systems
4. Operates under MHA sensitive-data norms (on-device inference, federated training)
5. Maintains personnel dignity (no disciplinary use of stress labels)

**Key innovation:** Move from reactive screening to **predictive welfare analytics** with **federated privacy** — models learn across units without raw biometric/psych data leaving devices.

## 2. Current Landscape & Prior Art
| Prior Art | What It Does | Gap vs PS |
|-----------|--------------|-----------|
| **HeadSpace/Headspace for Work** | Corporate mindfulness + mood tracking | Not predictive, not federated, not uniformed-forces domain |
| **Woebot/Wysa** | Chatbot CBT for mental health | Reactive, no biometric fusion, no privacy-preserving federated training |
| **Oura/Whoop stress scores** | HRV-based stress recovery tracking | Consumer-grade, no clinical validation, no federated learning, no MHA compliance |
| **NIMHANS mental health apps** | Indian psych resources | Not predictive, not multimodal, no on-device inference |
| **arXiv HRV stress papers** | Lab-based stress detection (WESAD, etc.) | Controlled settings, no shift/deployment context, no federated deployment |

**Critical gap:** No existing system combines **clinical validation + federated privacy + predictive welfare + uniformed-forces context**.

## 3. Technical Architecture (Proposed)
```
[Mobile App] → Self-report (PHQ-9/GAD-7) + Voice Journal
     ↓
[On-Device Sensor Fusion] → HRV (RMSSD/LF-HF) + EDA + Actigraphy
     ↓
[Edge Inference (TFLite)] → Stress Score + Burnout Risk (7-day prediction)
     ↓
[Federated Learning] → Model updates sent to server (raw data never leaves device)
     ↓
[Server Aggregation] → FedAvg → Global model → Push back to devices
     ↓
[Welfare Dashboard] → Role-based: Commander (unit aggregates), Welfare Officer (flagged individuals), Admin (audit logs)
     ↓
[Intervention Engine] → Recommends: counseling, workload rebalancing, rest periods
```

**Key components:**
- **HRV extraction:** 60s windows, RMSSD/LF-HF from PPG/ECG
- **NLP:** IndicBERT for voice/journal sentiment (Hindi/English)
- **Fusion:** Late fusion with attention mechanism
- **Calibration:** Temperature scaling for probabilistic risk scores
- **Privacy:** DP-SGD for federated training, on-device inference, audit logging

## 4. Evaluation Metrics
| Metric | Target | How Measured |
|--------|--------|--------------|
| **Stress F1** | >0.75 | WESAD/DAIC-WOZ benchmark |
| **Burnout MAE** | <0.15 | 7-day prediction error |
| **Abstention rate** | >0.90 | Adversarial/uncertain queries |
| **Calibration (ECE)** | <0.05 | Temperature-scaled probabilities |
| **Privacy budget** | ε≤1.0 | DP-SGD accounting |

## 5. Dataset Strategy
- **Primary:** WESAD (wearable stress), DAIC-WOZ (voice depression), SWELL-KW (work stress)
- **Synthetic augmentation:** Uniformed-forces shift schedules, deployment cycles, cultural noise patterns
- **Federated split:** By unit/battalion (simulated) to mimic real deployment

## 6. Team & Timeline
- **Team fit:** 5.0 (steep but feasible with right mix)
- **Feasibility:** 7.5 (software-only, no hardware)
- **Demo:** 6.0 (dashboard + on-device inference)
- **Differentiation:** 7.5 (federated + predictive + welfare-first = unique)

**48h build order:**
- **Tonight:** Ingest WESAD/DAIC-WOZ, build HRV extractor, train baseline CNN→BiLSTM
- **Tomorrow AM:** Add IndicBERT for voice, build fusion, calibrate
- **Tomorrow PM:** Deploy TFLite on-device, build FedAvg sketch, build dashboard

## 7. One-Pager Moats
1. **Federated first:** Raw biometric data never leaves device — MHA compliance by design
2. **Predictive, not reactive:** 7-day burnout onset prediction (not just current stress)
3. **Welfare over discipline:** Stress labels never used for personnel decisions — ethical by architecture
4. **Multilingual NLP:** Hindi+English voice/journal via IndicBERT ( India-specific)
5. **Show the numbers:** Eval harness with F1/MAE/ECE on Slide 5 of PPT

## 8. Sources (Pre-Cache — Finalize with Ledger)
1. SIH26186 PS — https://sih2026.vuce.in/ps/SIH26186
2. WESAD Dataset — https://archive.ics.uci.edu/ml/datasets/WESAD
3. DAIC-WOZ — https://psycnet.apa.org/record/2018-15763-001
4. NIMHANS Mental Health Report — https://nimhans.ac.in
5. DPDP Act 2023 — https://www.meity.gov.in/writereaddata/files/Digital_Personal_Data_Protection_Act_2023.pdf
6. HRV Stress Detection Review — arXiv:2103.03773
7. Federated Learning for Healthcare — arXiv:2107.02336
8. MHA Welfare Guidelines — https://ahc.nic.in
9. PHQ-9/GAD-7 Validation — Spitzer et al.
10. IndicBERT — ai4bharat.org

*Draft assembled by @ps186 — Iteration 1, 2026-09-03*
*Waiting for Worker A–E completion to finalize with cited sources.*
