# SIH 2026 — Research Gap Analysis & Iterative Deepening Plan
**Date:** 2026-09-03 | **Researcher:** @researcher | **For:** @sih26 (SIH 2026 bot)  
**PS Pair:** SIH26045 (Ayush IP-SAKTI) + SIH26168 (ISRO Dead Reckoning)  
**Team:** PrajnaPath (6, IPS Academy) | **Internal:** 05 Sep 2026

---

## Executive Assessment

**What we have (excellent):**
- Complete PS evaluation engine (175 PS, 9 scores, deterministic, reproducible)
- Deep research reports for both primary PS (14K + 16K lines each)
- Clear winning strategy: Combo A (26045 × 26047) for internal, with 26168 as ISRO differentiation
- 48-hour action plan locked

**What's missing (critical for building, not just briefing):**
The existing research is **strategic/architectural** — it tells us *what* to build and *why*. But to actually **implement in 48 hours** and **ideate novel differentiators**, we need **tactical/implementation-grade knowledge** on:

1. **Exact legal corpus acquisition** — Gazette URLs, PDF sha256s, version dates for every statute
2. **Formulation classification state machine** — the exact 3-5 question decision tree with citations
3. **Jurisdiction toggle implementation** — how to enforce separation at retrieval + generation time
4. **Citation validator regex patterns** — exact patterns for every statute/treaty/article
4. **Bhashini ULCA API** — endpoints, auth, request/response schemas, rate limits
5. **Evaluation harness** — the exact 20 gold Q-A pairs + 5 adversarial queries with expected outputs
6. **Neo4j knowledge graph schema** — Cypher DDL, node/rel types, traversal queries
7. **IO-VNBD preprocessing** — exact CSV schema, train/test split by route, windowing code
8. **SpeedNet architecture** — exact CNN/BiLSTM config, ONNX export, TFLite quantization
9. **EKF/IEKF implementation** — state vector, covariance init, NHC/ZUPT pseudo-measurements
10. **Map-matching HMM on OSM** — graph construction, Viterbi, multi-hypothesis
11. **Seamless GNSS dropout handler** — HDOP/sat thresholds, re-seed logic, no-jump fusion
12. **10Hz↔200Hz resampling** — interpolation strategy, shared model generalization

---

## Research Loop Design

### Loop Structure
```
ITERATION 1 (Today)     → Legal corpus + Formulation wizard + Bhashini API + IO-VNBD prep
ITERATION 2 (Tomorrow)  → Citation validator + Eval harness + Knowledge graph schema
ITERATION 3 (Tomorrow)  → SpeedNet + EKF + Map-matching + GNSS handler + Resampling
ITERATION 4 (04 Sep AM) → Integration testing + Demo recording + PPT finalization
```

### Each Iteration:
1. **I (Researcher)** analyze gaps → define precise research tasks
2. **@sih26** executes research (web search, paper extraction, API docs, code repos)
3. **I** evaluate findings → verify, synthesize, identify next gaps
4. **Save** to vault → `reference/research/sih26/<topic>-YYYY-MM-DD.md`
5. **Repeat** until build-ready

---

## Iteration 1 Research Tasks (Dispatching Now)

### Task 1A: SIH26045 — Legal Corpus Acquisition (Exact Sources)
**Goal:** Get every statute/treaty/rule PDF with: official URL, Gazette date, sha256, page count
**Needed for:** Version-tracked corpus badge, chunk metadata, citation validator ground truth

| Document | Official Source | Gazette Date | Status |
|----------|----------------|--------------|--------|
| Patents Act 1970 (as amended) | ipindia.gov.in | — | |
| Patents (Amendment) Rules 2024 | egazette.nic.in | 15 Mar 2024 | |
| Biological Diversity Act 2002 | nbaindia.nic.in | — | |
| Biological Diversity (Amendment) Act 2023 | egazette.nic.in | — | |
| Biological Diversity Rules 2024 | egazette.nic.in | 25 Oct 2024 | |
| WIPO GRATK Treaty 2024 | wipo.int | May 2024 | |
| Ayurvedic Pharmacopoeia of India (API) | ayush.gov.in | — | |
| IMPPAT 2.0 DB | db.imppat.org | — | |
| Drugs & Magic Remedies Act 1954 + 2024 advisory | cdscO.gov.in | — | |
| FSSAI Ayurveda Aahar Regs 2022 | fssai.gov.in | — | |

**Deliverable:** Table with verified URLs, PDFs downloaded to local, sha256, page counts.

---

### Task 1B: SIH26045 — Formulation Classification Wizard (Exact Decision Tree)
**Goal:** The exact 3-5 question flow with statute citations at each branch
**Questions to resolve:**
1. Is it a **classical formulation** listed in First Schedule of Drugs & Cosmetics Act?
   - If YES → Sec 3(p) bar applies → TKDL/API citation → GI/TM route → ABSTAIN on patent
   - If NO → Q2
2. Is it a **new drug** (not in API, new combination/process)?
   - If YES → NDCT Rules 2019 + CDSCO → Patent possible (if novel/inventive) → Sec 3(p) analysis
   - If NO → Q3
3. Is it a **phytopharmaceutical** (standardized extract, marker compounds)?
   - If YES → CDSCO phytopharma pathway → Patent + regulatory dual track
   - If NO → Q4
4. Is it an **Ayurveda Aahar** (food category)?
   - If YES → FSSAI 2022 Regs → No patent, TM + GI only
   - If NO → Q5
5. Is it a **cosmetic** (topical, non-therapeutic claims)?
   - If YES → Drugs & Cosmetics Act cosmetic schedule → Different IP regime

**Deliverable:** Mermaid flowchart + statute citation at every decision node.

---

### Task 1C: SIH26045 — Bhashini ULCA API Integration Specs
**Goal:** Exact integration details for hackathon demo
**Needed:**
- Base URL, authentication (API key? JWT?),
- Endpoints: `/translate` (T2T), `/transliterate`, `/asr`, `/tts`
- Request/response JSON schemas
- Rate limits, latency (p50/p99)
- Language codes for 22 scheduled languages
- Legal-domain BLEU benchmarks (if published)
- Sample curl/Postman collection
- Python SDK if exists

**Deliverable:** Working integration notebook cell + rate-limit handling.

---

### Task 1D: SIH26168 — IO-VNBD Data Acquisition & Preprocessing
**Goal:** Download, verify, and prepare the mandated dataset
**Steps:**
1. Download IO-VNBD from official source (Google Drive/Kaggle/arXiv supplement)
2. Verify checksums, explore CSV schema (columns, units, sampling rates)
3. Split by **route** (not time) — hold out France routes for test
4. Extract smartphone subset (58 hrs / 4400 km) — separate from car subset
5. Windowing: 2s @ 10Hz → upsample to 100Hz → 200×6 tensor
6. Labels: mean forward speed from wheel-speed (car) / GNSS-derived (phone)
7. Augmentation pipeline: Gaussian noise, rotation, shock impulse, time-stretch

**Deliverable:** `io_vnbd_prep.ipynb` with verified stats matching paper.

---

### Task 1E: SIH26168 — Alignment Engine (Phone→Vehicle Rotation)
**Goal:** Online calibration using first 30s of good GNSS
**Approach:**
- Collect accelerometer + GNSS velocity during straight-line driving
- PCA on acceleration → forward axis in phone frame
- Gravity vector → roll/pitch
- Solve R_phone_to_vehicle (3×3 rotation matrix)
- Auto-calibrate UI: show "Calibrating... 12s remaining" → "Aligned ✓"
- Re-estimate every 30s during driving

**Deliverable:** Mathematical derivation + Python implementation + validation on IO-VNBD.

---

## Next: Dispatching Tasks to @sih26