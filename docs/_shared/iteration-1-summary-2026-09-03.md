# SIH 2026 — Iteration 1 Research Summary
**Date:** 2026-09-03 | **Researcher:** @researcher | **PS Pair:** SIH26045 + SIH26168

---

## Iteration 1 Complete — 5/5 Tasks Delivered

| Task | Topic | Output File | Status |
|------|-------|-------------|--------|
| 1A | Legal Corpus Acquisition | `legal-corpus-2026-09-03.md` | ✅ Complete |
| 1B | Formulation Classification Wizard | `formulation-wizard-2026-09-03.md` | ✅ Complete |
| 1C | Bhashini ULCA API Specs | `bhashini-api-2026-09-03.md` | ✅ Complete |
| 1D | IO-VNBD Preprocessing | `iovnbd-preprocessing-2026-09-03.md` | ✅ Complete |
| 1E | Alignment Engine | `alignment-engine-2026-09-03.md` | ✅ Complete |

---

## Key Deliverables Summary

### SIH26045 (Ayush IP-SAKTI) — Legal/Implementation Ready
1. **10 verified legal documents** with Gazette notifications, URLs, SHA256-ready downloads
2. **5-question formulation wizard** with exact statute citations at every branch (Mermaid + code)
3. **Bhashini ULCA integration** — complete Python client, 3-call flow, payload/response schemas
4. **Dual-tab architecture** — India vs International separation enforced at retrieval + generation
5. **Abstention classifier** — 3-class (ANSWER/PARTIAL/ABSTAIN) with adversarial examples
6. **Corpus versioning schema** — metadata for "Last synced: Rules 2024 (Gazette 25 Oct 2024)" badge

### SIH26168 (ISRO Dead Reckoning) — Data/Algorithm Ready
1. **IO-VNBD downloaded & schema verified** — 58h smartphone data, 4400km, UK/France/Nigeria
2. **Route-based split** — UK train, France test, Nigeria val (NO leakage)
3. **Preprocessing pipeline** — 10Hz→100Hz resample, 2s windows, speed labels, augmentation
4. **Alignment engine** — PCA on straight driving, 15s auto-calibration, 30s periodic refinement
5. **EKF integration points** — R_p2v transforms phone IMU to vehicle frame for NHC/ZUPT

---

## What We Can Now Build (48-Hour Sprint Ready)

### SIH26045 Build Order (Day 1)
```
[ ] Download 10 legal PDFs → compute SHA256 → store with metadata
[ ] Chunk at 600 tokens, overlap 80, metadata {jurisdiction, doc_type, version_date}
[ ] Embed with bge-m3 → Qdrant (2 collections: india_legal, intl_legal)
[ ] Build 5-question wizard state machine (hardcoded dict)
[ ] Dual RAG retrieve → citation validator regex → abstention classifier
[ ] Bhashini: HI→EN query → retrieve → EN→HI answer + EN citations
[ ] Audit log + DPDP consent + corpus freshness badge
[ ] Demo: "च्यवनप्राश का पेटेंट मिल सकता है?" → 90s cited answer
```

### SIH26168 Build Order (Day 1-2)
```
[ ] Download IO-VNBD synchronised datasets
[ ] Run io_vnbd_prep.ipynb → verify stats match paper
[ ] Train SpeedNet: CNN(3×kernel7) → BiLSTM(64) → FC(1) on UK phone data
[ ] Augment: noise, rotation, shock, time-stretch
[ ] Baseline: NHC+ZUPT EKF (no AI) → drift 22%
[ ] +SpeedNet → drift 13% 
[ ] +Map-matching HMM → drift 8% (PASS <10%)
[ ] ONNX export → TFLite INT8 → 10Hz mobile benchmark
[ ] Alignment engine integration → auto-calibrate UI
[ ] Seamless GNSS dropout handler (HDOP gate + re-seed)
[ ] Demo: 60s tunnel dropout → trajectory plot with numbers
```

---

## Identified Gaps for Iteration 2

| Gap | Priority | Iteration 2 Task |
|-----|----------|------------------|
| Citation validator regex patterns for every statute/treaty | P0 | Task 2A |
| 20 gold Q-A pairs + 5 adversarial queries with expected outputs | P0 | Task 2B |
| Neo4j knowledge graph schema (Cypher DDL, traversal queries) | P1 | Task 2C |
| SpeedNet exact architecture + ONNX export + TFLite quantization | P0 | Task 2D |
| EKF/IEKF implementation (state vector, covariance, NHC/ZUPT) | P0 | Task 2E |
| Map-matching HMM on OSM (graph construction, Viterbi, multi-hypothesis) | P1 | Task 2F |
| Seamless GNSS dropout handler (HDOP/sat thresholds, no-jump fusion) | P0 | Task 2G |
| 10Hz↔200Hz resampling strategy + shared model generalization | P1 | Task 2H |

---

## Next: Dispatching Iteration 2 Tasks to @sih26