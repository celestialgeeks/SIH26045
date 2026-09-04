# PrajnaPath — SIH 2026 | PS45 × PS168
**IPS Academy, Indore — Team PrajnaPath (6) | Internal: 05 Sep 2026**

> **Chosen pair (WPS v3):** `SIH26045` **IP-SAKTI Sahayak** (Ayush, 7.33 #1, CLS 3.35) × `SIH26168` **Intelligent Dead Reckoning** (ISRO, 6.32 #13) — WORKABLE
> **Researcher:** `@researcher` (opencode-free) oversees; `@ps45` + `@ps168` execute isolated loops (no cross-contamination)

---

## 🚀 Quick Start for Team

```bash
git clone <this-repo>
# PS45 docs (Ayush RAG)
ls docs/ps45/          # 8 tactical docs + deep research
ls prototype/ps45/     # validator (56 patterns) + 40+10 harness + Neo4j

# PS168 docs (Dead Reckoning)
ls docs/ps168/         # 7 docs (IO-VNBD, alignment, SpeedNet, EKF, map-matching)
ls prototype/ps168/    # speednet + ekf + map_matching + gnss_handler + resampler

# Shared evaluation (why this pair won)
cat research/ps-evaluation/06-complete-ps-ranking-v3.md
cat docs/INDEX.md
```

---

## 📁 Repo Map

```
docs/
├── ps45/  → SIH26045 IP-SAKTI (multilingual RAG, source-cited, jurisdiction-aware)
│   ├── sih26045-deep-research.md        14K — winning strategy
│   ├── legal-corpus-2026-09-03.md        7.7K — 10 PDFs + Gazette G.S.R. 211(E)/665(E)
│   ├── formulation-wizard-2026-09-03.md  9.8K — 5-Q classifier + DSI branch (2025 update)
│   ├── bhashini-api-2026-09-03.md        13K — ULCA 64392f96daac500b55c543cd, 22 langs
│   ├── citation-validator-2026-09-03.md  12K → 56 regex (see prototype)
│   ├── eval-harness-2026-09-03.md        17K → 40 gold + 10 adversarial
│   ├── neo4j-schema-2026-09-03.md        27K — schema.cypher + queries.cypher
│   └── field-intelligence-2026-09-03.md  9.9K — current news 2024-2026 (NEW)
├── ps168/ → SIH26168 Dead Reckoning (phone 10Hz, 60s tunnel <10% drift)
│   ├── sih26168-deep-research.md
│   ├── iovnbd-preprocessing-2026-09-03.md
│   ├── alignment-engine-2026-09-03.md
│   ├── speednet-arch-2026-09-03.md       CNN→BiLSTM 180K → ONNX→TFLite
│   ├── ekf-iekf-2026-09-03.md
│   ├── map-matching-hmm-2026-09-03.md    OSM pyosmium → HMM Viterbi k=2
│   └── gnss-resampler-2026-09-03.md      HDOP>3 + DualRateIMU 10↔200Hz
├── shared/                              gap analysis + iteration summary
└── INDEX.md                             master handoff map

prototype/
├── ps45/  citation_validator/ (validator.py 56 patterns) + eval_harness/ (40+10) + neo4j_schema/
└── ps168/ speednet/ + ekf/ + map_matching/ + gnss_handler/ + resampler/ (both verified)

research/ps-evaluation/                  why 45×168 beat 26046/26186 — WPS v3, combos, reasoning
```

---

## 🎯 Expected Solution — What We Build (48h)

### PS45: IP-SAKTI Sahayak
**Problem:** Ayurveda startup must decide patentability (Sec 3(p)/(e)/(i)/(j)/(k)), IP regime, ABS (Form 1/2, DSI=BR 29 Apr 2025), and international GRATK disclosure — no cited, jurisdiction-aware tool exists.

**Our solution (judge-ready):**
- **Dual-tab RAG (India vs International)** — Qdrant ×2, Bhashini ULCA (HI→EN retrieve/cite→HI, 22 langs, MoU 10 Apr 2026)
- **5-Q Formulation Wizard** with DSI branch (BD Rules 25 Dec 2024 + Benefit Sharing 29 Apr 2025)
- **Citation validator: 56 regex, 100% or ABSTAIN** — every answer has `[CIT: ...]` or safe abstention
- **Demo: 90s** — Hindi voice query “क्या च्यवनप्राश पेटेंट हो सकता है?” → dual tabs, validator badge, Suraksha 10k complaints slide

**Stack:** Qdrant + Neo4j + IndicTrans2 + Dhwani ASR/TTS + FastAPI

### PS168: Intelligent Dead Reckoning
**Problem:** Seamless navigation through GNSS-dark zones (tunnels) — phone-only, no infrastructure.

**Our solution:**
- **IO-VNBD 58h (UK train / FR test / NG val)**, 10→100Hz DualRateIMU, SpeedNet CNN→BiLSTM (180K) → drift 4.1m/50m
- **EKF 16-D (NHC/ZUPT/GNSS/Map)** + **OSM HMM Viterbi** + **seamless HDOP>3 handler**
- **Demo: 60s tunnel** (purple snap, 4.1m badge, HDOP=99 button)

**Stack:** PyTorch → ONNX → TFLite (INT8) + pyosmium + EKF

---

## 📊 Current Situation (Field 2024-2026) — PS45

| Date | Signal |
|---|---|
| 25 Oct 2024 | BD Rules 2024 notified (supersedes 2004) → effective 25 Dec 2024 (Form 1/2 split) |
| 29 Apr 2025 | NBA Benefit Sharing Regs: **DSI = BR for ABS** (8 monetary + 14 non-monetary) |
| 29 May 2025 | Ayush Nivesh Saarthi portal (100% FDI, 17% CAGR, 8k species) |
| 30 May 2025 | Ayush Suraksha Portal → 10k complaints (misleading ads) by Mar 2026 |
| 2025 | IP India Ayush Guidelines 2025 (14p, device patentability) |
| 10 Apr 2026 | Ayush × BHASHINI MoU — 22 languages across Ayush Grid |

*Full dossier: `docs/ps45/field-intelligence-2026-09-03.md` (sources: PIB, IP India, Conventus, DD News, TKDL, BananaIP 2025)*

---

## 🧭 Strategy — How We Win

1. **Hit 3 live 2024-25 traps in demo** — DSI=BR, Form1 vs Form2, Vamana sensor device (2025 Guidelines) — stale-law teams fail.
2. **Moat slide: “We Implement Government Policy”** — BHASHINI Rajyam MoU + BD Rules + Ayush Guidelines (with dates).
3. **Pain → Solution:** Suraksha 10k complaints → citation validator.

---

## 🔧 Implementation Status (19:58 03 Sep)

| PS | Docs | Prototype | Next |
|---|---|---|---|
| ps45 | 8/8 ✓ (field-intel just added) | validator 56 ✅, harness 40+10 ✅ | @ps45 to finish: BD re-verify + Bhashini live + Neo4j live |
| ps168 | 7/7 ✓ | 5 modules verified ✓ | idle — ready |

---

## 👥 Collaboration

- **This repo is ready to push:** `git init && git add . && git commit -m "SIH26 ps45×ps168 — all research + prototypes" && git remote add origin <github> && git push`
- **Vault is source of truth:** `reference/research/sih26/` + `projects/sih26/` (this folder is a clean snapshot).
- **Bots:** `@researcher` oversees; `@ps45` + `@ps168` isolated (see `docs/INDEX.md`).

*Generated by @researcher — 2026-09-03 19:59 IST*
