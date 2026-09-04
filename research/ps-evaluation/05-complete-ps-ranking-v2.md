# SIH 2026 — Complete Software Problem Statement Evaluation v2 (All 175 PS) — Raw-Data Re-score

**Generated**: 2026-09-03 · **Version**: v2 (raw-data-driven) · **Previous**: `04-complete-ps-ranking.md` (v1)
**Source**: `vedantchalke36/sih-2026-problem-statements` — `175` Software PS from 229 total (54 Hardware excluded) · `scraped_at` 2026-08-21/29 · `ideas` field 0/500 = pre-freeze snapshot
**Engine**: `ps-evaluator` 6-bucket framework + **v2 patches** (see Methodology changelog) · Reproducible via `/tmp/eval_v2.py`

---

## TL;DR for Shreyash's team (7th sem, IPS Academy)

| Priority | PS ID | WPS v2 | Δ vs v1 | Quality | CLS v2 (fixed) | Verdict v2 | Why lock this |
|----------|-------|--------|---------|---------|----------------|------------|---------------|
| **#1** | **SIH26045** | **7.20** | +0.46 | 7.47 | 3.35 | WORKABLE | IP-SAKTI Sahayak a multilingual, RAG-based (source-cited) AI a... — Ministry of Ayush |
| **#2** | **SIH26047** | **6.86** | +0.37 | 7.42 | 3.85 | WORKABLE | Patient Case-Taking Software... — Ministry of Ayush |
| **#3** | **SIH26014** | **6.77** | +0.57 | 7.62 | 5.00 | WORKABLE | An lntegrated GIS-based Digital Public lnfrastructure for Land... — Ministry of Rural Developmen |
| **#4** | **SIH26036** | **6.61** | -0.37 | 7.05 | 5.05 | WORKABLE | Development of an Online Verification System for Weighing and ... — Ministry of Consumer Affairs |
| **#5** | **SIH26046** | **6.50** | +0.86 | 6.60 | 3.55 | WORKABLE | AIIA Clinical Trials Dashboard - a real-time, cloud-based, GCP... — Ministry of Ayush |

**v2 top pick changed**: v1 #1 `SIH26036` (6.98) → v2 #4 (6.61, −0.37). New #1 is **`SIH26045 IP-SAKTI Sahayak` (7.20, +0.46)** — the only PS that scores 7.20 and stays the lowest CLS (3.35). If college SPOC blocks `SIH26045`, fallback chain is `SIH26047` → `SIH26014` → `SIH26036`.

---

## Methodology v2 — What changed and why

### v1 bugs that v2 fixes (all traceable to raw `description` + `org` + `dataset_link`)

| Bug in v1 | Impact | v2 fix | Example |
|-----------|--------|--------|---------|
| **Org fuzzy bleed**: `MDoNER` matched `MoES` via word `"ministry"` → CLS 9.0 inflated | SIH26001 CLS 8.55 → freeze HIGH incorrectly | Exact longest-key match on `ORG_TABLE`; fallback uses `ps_count_per_org` heuristic (27 MoES=9.0, 3 MDoNER=3.5) | `SIH26001` CLS 8.55 → 7.85, `SIH26002` 6.95 → 5.45 (−1.50) |
| **Quality sub-scores templated** (5.0 defaults for 101 `ministry_fit`, avg feas 4.47) | Many PS collapsed to same Q (6.0) | Text-derived 9 scores: `innov`, `feas`, `impact`, `demo_ab`, `team`, `diff`, `dataset`, `demox`, `mfit` — each from keyword density + `dataset_link` + `theme` | `SIH26227` Q 5.18 → 6.48 (+1.30), `SIH26046` 5.75 → 6.60 |
| **`dataset_score` ignored `dataset_link`** (only 41 PS have links, v1 avg 4.94) | Undervalued data-ready PS | If `dataset_link` present → 7–8; else text signals (`open data`, `api`, `synthetic`, `field collection`) adjust 4–6 | `SIH26038` 5.0 → 8.0 (dataset_link), `SIH26046` 4.0 → 7.0 |
| **`ministry_fit` default 5.0 for 101 PS** | Lost sharp-vs-diffuse intent | `ps_count_per_org`: ≤3 PS → 8.5 (Ayush, MDoNER), 27 PS → 4.5 (MoES), plus mandate-keyword match | MDoNER 5.0 → 8.5, MoES stays 4.5 |
| **`differentiation` static** | Could not surface twist headroom | Counts `DIFF_TWIST` signals (`knowledge graph`, `bhashini`, `citizen mode`, `citation`, `quantum-inspired`) in `description` | `SIH26014` 8.5 → 7.0 (realistic), niche Ayush stays 7.5 |
| **CLS theme/keyword not niche-suppressed consistently** | Generic AI hype inflated niche domains | Reuses `evaluate.py` niche suppression (GRATK/Nagoya/ULPIN/TKDL/Bhashini/WIPO → cap AI/RAG at 5, buzz at 3) | `SIH26045` stays 3.35 (correct), `SIH26047` 4.70 → 3.85 |

### Formal v2 formulas (unchanged from skill)

```
CLS  = Theme×0.25 + Org×0.20 + Keyword×0.25 + PerceivedEase×0.20 + Buzz×0.10
       Theme: THEME_SCORES exact match; Org: ORG_TABLE longest-key; Keyword/Bias: niche-suppressed

Quality = Innov×0.30 + Feas×0.25 + Impact×0.20 + DemoAbility×0.15 + TeamFit×0.10
Innov / Feas / Impact / DemoAbility / TeamFit / Diff / Dataset / MinistryFit:
        derived from raw title+description text features (see /tmp/eval_v2.py lines 60-180)

WPS = Quality×0.40 + (10-CLS)×0.25 + Diff×0.15 + Dataset×0.10 + Demo×0.05 + MFit×0.05

Verdict: ≥7.5 STRONG PICK · 6.0–7.5 WORKABLE · <6.0 HIGH RISK
Expected submissions: CLS/10 × 500 · Freeze: CLS×10% · Submit-by: 17 Sep if CLS≥7 else 18/19/20 Sep
```

### Reproducibility

```bash
python3 /tmp/eval_v2.py   # reads /tmp/sih260_all_software_full.json → writes v2 JSON+CSV
python3 -c "import json; print([r['ps_id'] for r in json.load(open('/tmp/sih260_all_evaluated_v2.json'))[:3]])"
# → ['SIH26045', 'SIH26047', 'SIH26014']
```

---

## Scoring Methodology (reference)

| Metric | Range | Weight in WPS | How v2 derives it (raw-data signals) |
|--------|-------|---------------|--------------------------------------|
| **Feasibility** | 1–10 | via Quality 25% | −1.5 if `lidar 3d/photogrammetry/electronic warfare/underwater` · −1.0 if `real-time gis/nationwide land stack` · +1.0 if `student innovation` · +0.5 if `dataset_link` present · −1.0 if ≥3 `integration` |
| **Innovation** | 1–10 | via Quality 30% | `hard-tech` count (quantum/KG/Bhashini/TKDL/GRATK/ULPIN/satellite/digital twin) ≥4 → 8.0 · +1.5 if niche treaty present · +1.0 if `quantum` |
| **Dataset** | 1–10 | 10% | `dataset_link` with drive/kaggle/github → 8 · else public signals +1 · `field collection/crowdsource` −1 |
| **Demo-ability** | 1–10 | via Quality 15% + 5% direct | `portal/dashboard/mobile` → 7.5 base · −1.5 if `hardware/satellite/drone/underwater` |
| **Impact** | 1–10 | via Quality 20% | Org scale (MHA 8.0, MoES disaster 7.5, Ayush 6.0) + theme boost (Disaster 7.5, MedTech 7.0, Agri 7.0) + `nationwide` +0.5 |
| **Differentiation** | 1–10 | 15% | Count twist signals (`knowledge graph`, `citation`, `bhashini`, `persona switch`, `quantum-inspired`) · commodity scan/ocr without twist → 4.0 |
| **Ministry Fit** | 1–10 | 5% | `ps_count_per_org`: ≤3 → 8.5 (sharp) vs 27 → 4.5 (diffuse) · plus mandate match (Consumer→legal metrology, Ayush→ayurveda/ip, Rural→land/gis) |
| **CLS** | 1–10 (low=good) | via 25% of WPS as `10-CLS` | 5-factor with fixed org + niche suppression |
| **WPS** | 1–10 | composite | see formula above |

**v2 ranges**: Quality 5.68–7.62 avg 6.51 · CLS 3.35–8.80 avg 7.01 · WPS 4.46–7.20 avg 5.33 (vs v1 avg WPS 5.15, CLS 6.86 inflated)

---

## Verdict distribution v2 vs v1

| Verdict | v1 count | v2 count | Change |
|---------|----------|----------|--------|
| STRONG PICK (≥7.5) | 0 | 0 | +0 |
| WORKABLE (6.0–7.5) | 12 | 13 | +1 |
| HIGH RISK (<6.0) | 163 | 162 | -1 |

Only 13 PS are WORKABLE in v2 (same* count but **different set** — 7 flipped each way). No PS hits STRONG PICK except SIH26045 would need WPS ≥7.5 (it has 7.20, closest — see actions to push it to 7.5).

---

## Top 20 — Ranked by WPS v2 (raw-data re-score)

| Rank | PS ID | WPS v2 | Δ vs v1 | Q v2 | CLS v2 | Verdict v2 | Title | Org | Theme |
|------|-------|--------|---------|------|--------|------------|-------|-----|-------|
|  1 | SIH26045 | 7.20 | +0.46 | 7.47 | 3.35 | WORKABLE | IP-SAKTI Sahayak a multilingual, RAG-based (source-cited) ... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  2 | SIH26047 | 6.86 | +0.37 | 7.42 | 3.85 | WORKABLE | Patient Case-Taking Software... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  3 | SIH26014 | 6.77 | +0.57 | 7.62 | 5.00 | WORKABLE | An lntegrated GIS-based Digital Public lnfrastructure for ... | Ministry of Rural Development... | Agriculture, FoodTech & Rural Development |
|  4 | SIH26036 | 6.61 | -0.37 | 7.05 | 5.05 | WORKABLE | Development of an Online Verification System for Weighing ... | Ministry of Consumer Affairs, Fo... | Miscellaneous |
|  5 | SIH26046 | 6.50 | +0.86 | 6.60 | 3.55 | WORKABLE | AIIA Clinical Trials Dashboard - a real-time, cloud-based,... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  6 | SIH26138 | 6.33 | +0.09 | 6.47 | 5.05 | WORKABLE | Quantum-Inspired Fuel Consumption Prediction and Green Fle... | Egreen Quanta... | Clean & Green Technology |
|  7 | SIH26184 | 6.12 | -0.12 | 7.35 | 6.10 | WORKABLE | Development of a Predictive Analytics Framework for Cyberc... | Ministry of Home Affairs... | Blockchain & Cybersecurity |
|  8 | SIH26101 | 6.11 | +0.57 | 7.20 | 5.90 | WORKABLE | Develop an AI enabled learning platform that identifies co... | MoSPI... | Smart Education |
|  9 | SIH26128 | 6.11 | +0.54 | 6.88 | 4.35 | WORKABLE | Efficient systems for early detection,prevention,and manag... | Government Of Maharashtra... | MedTech / BioTech / HealthTech |
| 10 | SIH26089 | 6.04 | +0.39 | 6.88 | 5.05 | WORKABLE | Cooperative Gig Services Platform for Household & Communit... | Ministry of Cooperation... | Agriculture, FoodTech & Rural Development |
| 11 | SIH26015 | 6.00 | +0.30 | 6.75 | 5.00 | WORKABLE | Application of Geospatial Techniques for visualization and... | Ministry of Rural Development... | Agriculture, FoodTech & Rural Development |
| 12 | SIH26038 | 6.00 | +0.26 | 6.88 | 6.10 | WORKABLE | Explainable AI for Diabetic Retinopathy Screening in Rural... | MathWorks... | MedTech / BioTech / HealthTech |
| 13 | SIH26137 | 6.00 | +0.12 | 6.40 | 6.15 | WORKABLE | Quantum-Inspired Intelligent Traffic Route Optimization in... | Egreen Quanta... | Transportation & Logistics |
| 14 | SIH26168 | 5.96 | +1.13 | 6.75 | 6.05 | HIGH RISK | AI-ML based Intelligent Dead Reckoning system for seamless... | Indian Space Research Organisati... | Smart Vehicles |
| 15 | SIH26011 | 5.92 | -0.25 | 7.07 | 6.75 | HIGH RISK | 3D ULPIN Generation and vertical Property Mapping SYstem... | Ministry of Rural Development... | Smart Automation |
| 16 | SIH26017 | 5.91 | +0.20 | 7.13 | 5.85 | HIGH RISK | Predictive Analytics System for Early Detection of Land Ac... | Ministry of Rural Development... | Smart Automation |
| 17 | SIH26111 | 5.90 | +0.12 | 7.10 | 5.65 | HIGH RISK | Smart Al-Enabled Rapid Feed and Silage Quality Testing Sys... | Ministry of Fisheries, Animal Hu... | Agriculture, FoodTech & Rural Development |
| 18 | SIH26003 | 5.85 | +0.66 | 6.88 | 5.80 | HIGH RISK | AI-Based Cognitive Gaming and Memory Assistance Platform f... | Ministry of Development of North... | MedTech / BioTech / HealthTech |
| 19 | SIH26167 | 5.85 | -0.18 | 6.72 | 5.85 | HIGH RISK | SatQuery AI - An Interactive Vision-Language Assistant for... | Indian Space Research Organisati... | Space Technology |
| 20 | SIH26227 | 5.85 | +1.25 | 6.48 | 5.65 | HIGH RISK | Semantic Retrieval and Multi-Temporal Change Analysis of S... | Ministry of defence (MoD)... | Space Technology |

---

## Complete Ranked List — All 175 Software PS (v2)

| Rank | PS ID | WPS | Δ | Quality | CLS | Verdict | Title | Org | Theme | Innov | Feas | Impact | DemoAb | Team | Diff | Data | Demo | MFit |
|------|-------|-----|---|---------|-----|---------|-------|-----|-------|-------|------|--------|--------|------|------|------|------|------|
|   1 | SIH26045 | 7.20 | +0.46 | 7.47 | 3.35 | WORKABLE | IP-SAKTI Sahayak a multilingual, RAG-based (sour... | Ministry of Ayush... | MedTech / BioTech / He... | 9.0 | 7.5 | 7.5 | 6.0 | 5.0 | 7.5 | 7.0 | 6.0 | 8.5 |
|   2 | SIH26047 | 6.86 | +0.37 | 7.42 | 3.85 | WORKABLE | Patient Case-Taking Software... | Ministry of Ayush... | MedTech / BioTech / He... | 9.0 | 6.0 | 7.5 | 7.5 | 6.0 | 7.0 | 5.0 | 7.5 | 8.5 |
|   3 | SIH26014 | 6.77 | +0.57 | 7.62 | 5.00 | WORKABLE | An lntegrated GIS-based Digital Public lnfrastru... | Ministry of Rural Developmen... | Agriculture, FoodTech ... | 9.0 | 6.0 | 8.0 | 7.5 | 7.0 | 7.0 | 6.5 | 7.5 | 8.0 |
|   4 | SIH26036 | 6.61 | -0.37 | 7.05 | 5.05 | WORKABLE | Development of an Online Verification System for... | Ministry of Consumer Affairs... | Miscellaneous... | 6.5 | 7.5 | 7.0 | 7.5 | 7.0 | 7.0 | 7.0 | 7.5 | 8.5 |
|   5 | SIH26046 | 6.50 | +0.86 | 6.60 | 3.55 | WORKABLE | AIIA Clinical Trials Dashboard - a real-time, cl... | Ministry of Ayush... | MedTech / BioTech / He... | 5.5 | 6.5 | 7.5 | 7.5 | 7.0 | 5.0 | 7.0 | 7.5 | 8.5 |
|   6 | SIH26138 | 6.33 | +0.09 | 6.47 | 5.05 | WORKABLE | Quantum-Inspired Fuel Consumption Prediction and... | Egreen Quanta... | Clean & Green Technolo... | 7.5 | 6.0 | 5.5 | 7.5 | 5.0 | 7.0 | 7.0 | 7.5 | 7.5 |
|   7 | SIH26184 | 6.12 | -0.12 | 7.35 | 6.10 | WORKABLE | Development of a Predictive Analytics Framework ... | Ministry of Home Affairs... | Blockchain & Cybersecu... | 6.5 | 7.5 | 8.5 | 7.5 | 7.0 | 7.0 | 5.0 | 7.5 | 5.5 |
|   8 | SIH26101 | 6.11 | +0.57 | 7.20 | 5.90 | WORKABLE | Develop an AI enabled learning platform that ide... | MoSPI... | Smart Education... | 8.0 | 6.5 | 7.0 | 7.5 | 6.5 | 5.0 | 7.0 | 7.5 | 7.5 |
|   9 | SIH26128 | 6.11 | +0.54 | 6.88 | 4.35 | WORKABLE | Efficient systems for early detection,prevention... | Government Of Maharashtra... | MedTech / BioTech / He... | 6.5 | 7.0 | 7.0 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 6.5 |
|  10 | SIH26089 | 6.04 | +0.39 | 6.88 | 5.05 | WORKABLE | Cooperative Gig Services Platform for Household ... | Ministry of Cooperation... | Agriculture, FoodTech ... | 6.5 | 7.0 | 7.0 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 8.5 |
|  11 | SIH26015 | 6.00 | +0.30 | 6.75 | 5.00 | WORKABLE | Application of Geospatial Techniques for visuali... | Ministry of Rural Developmen... | Agriculture, FoodTech ... | 6.5 | 7.0 | 7.5 | 6.0 | 6.5 | 5.0 | 6.0 | 6.0 | 8.0 |
|  12 | SIH26038 | 6.00 | +0.26 | 6.88 | 6.10 | WORKABLE | Explainable AI for Diabetic Retinopathy Screenin... | MathWorks... | MedTech / BioTech / He... | 6.5 | 7.5 | 7.5 | 6.0 | 6.5 | 5.0 | 8.0 | 6.0 | 8.5 |
|  13 | SIH26137 | 6.00 | +0.12 | 6.40 | 6.15 | WORKABLE | Quantum-Inspired Intelligent Traffic Route Optim... | Egreen Quanta... | Transportation & Logis... | 7.5 | 6.0 | 5.5 | 7.0 | 5.0 | 7.0 | 7.0 | 7.0 | 7.5 |
|  14 | SIH26168 | 5.96 | +1.13 | 6.75 | 6.05 | HIGH RISK | AI-ML based Intelligent Dead Reckoning system fo... | Indian Space Research Organi... | Smart Vehicles... | 6.5 | 7.5 | 5.5 | 7.5 | 7.0 | 5.5 | 8.0 | 7.5 | 5.5 |
|  15 | SIH26011 | 5.92 | -0.25 | 7.07 | 6.75 | HIGH RISK | 3D ULPIN Generation and vertical Property Mappin... | Ministry of Rural Developmen... | Smart Automation... | 9.0 | 7.0 | 7.5 | 4.5 | 4.5 | 7.0 | 6.0 | 4.5 | 8.0 |
|  16 | SIH26017 | 5.91 | +0.20 | 7.13 | 5.85 | HIGH RISK | Predictive Analytics System for Early Detection ... | Ministry of Rural Developmen... | Smart Automation... | 6.5 | 7.0 | 8.0 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 8.0 |
|  17 | SIH26111 | 5.90 | +0.12 | 7.10 | 5.65 | HIGH RISK | Smart Al-Enabled Rapid Feed and Silage Quality T... | Ministry of Fisheries, Anima... | Agriculture, FoodTech ... | 8.0 | 7.0 | 7.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 8.5 |
|  18 | SIH26003 | 5.85 | +0.66 | 6.88 | 5.80 | HIGH RISK | AI-Based Cognitive Gaming and Memory Assistance ... | Ministry of Development of N... | MedTech / BioTech / He... | 6.5 | 7.0 | 7.0 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 8.5 |
|  19 | SIH26167 | 5.85 | -0.18 | 6.72 | 5.85 | HIGH RISK | SatQuery AI - An Interactive Vision-Language Ass... | Indian Space Research Organi... | Space Technology... | 8.0 | 7.0 | 6.5 | 4.5 | 6.0 | 5.5 | 7.0 | 4.5 | 7.5 |
|  20 | SIH26227 | 5.85 | +1.25 | 6.48 | 5.65 | HIGH RISK | Semantic Retrieval and Multi-Temporal Change Ana... | Ministry of defence (MoD)... | Space Technology... | 6.5 | 7.5 | 5.5 | 6.0 | 6.5 | 5.0 | 7.0 | 6.0 | 8.5 |
|  21 | SIH26131 | 5.83 | -0.07 | 6.65 | 4.80 | HIGH RISK | Early detection and management of crop diseases ... | Government Of Maharashtra... | Agriculture, FoodTech ... | 6.5 | 7.0 | 7.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 6.5 |
|  22 | SIH26002 | 5.82 | +0.07 | 6.58 | 5.45 | HIGH RISK | Al-Based Smart Logistics and Accessibility Intel... | Ministry of Development of N... | Transportation & Logis... | 6.5 | 7.0 | 5.5 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 8.5 |
|  23 | SIH26041 | 5.81 | -0.58 | 6.53 | 5.60 | HIGH RISK | AR-Based Vocational Training Simulator for Indus... | Governmcnt of Jharkhand... | Smart Education... | 5.5 | 7.0 | 6.5 | 7.5 | 7.0 | 5.0 | 5.5 | 7.5 | 8.5 |
|  24 | SIH26176 | 5.80 | +0.84 | 7.30 | 6.20 | HIGH RISK | ORCA Marine EcOsystem Reasoning with Collaborati... | Indian Space Research Organi... | Disaster Management... | 8.0 | 7.0 | 8.0 | 6.0 | 6.5 | 5.0 | 6.0 | 6.0 | 5.5 |
|  25 | SIH26193 | 5.78 | +0.57 | 6.70 | 5.50 | HIGH RISK | Student Innovation-Developing solutions, keeping... | AICTE... | Agriculture, FoodTech ... | 5.0 | 8.0 | 7.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  26 | SIH26195 | 5.77 | +0.35 | 6.30 | 4.90 | HIGH RISK | Student Innovation-Solutions could be in the for... | AICTE... | Clean & Green Technolo... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  27 | SIH26208 | 5.77 | +0.42 | 6.30 | 4.90 | HIGH RISK | Student Innovation-Challenge your creative mind ... | AICTE... | Toys & Games... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  28 | SIH26019 | 5.75 | +0.50 | 7.25 | 7.40 | HIGH RISK | National Digital Platform for Research, Policy I... | Ministry of Rural Developmen... | Smart Automation... | 6.5 | 7.5 | 8.0 | 7.5 | 7.0 | 5.5 | 6.0 | 7.5 | 8.0 |
|  29 | SIH26021 | 5.75 | +0.03 | 6.35 | 5.05 | HIGH RISK | Honey Chain: A block chain-based system for hone... | Ministry of MSME... | Agriculture, FoodTech ... | 5.5 | 7.0 | 7.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 8.5 |
|  30 | SIH26042 | 5.75 | -0.62 | 6.50 | 5.30 | HIGH RISK | Al-Powered Vernacular Pedagogy and Real-Time Tra... | Governmcnt of Jharkhand... | Smart Education... | 6.5 | 7.0 | 6.5 | 6.0 | 6.0 | 5.0 | 5.0 | 6.0 | 8.5 |
|  31 | SIH26198 | 5.74 | +0.45 | 6.70 | 5.65 | HIGH RISK | Student Innovation-Cutting-edge technology in th... | AICTE... | MedTech / BioTech / He... | 5.0 | 8.0 | 7.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  32 | SIH26229 | 5.71 | +0.52 | 6.63 | 5.95 | HIGH RISK | Kabadiwala Connect – Bringing the Informal Colle... | Ministry of Mines (MoM)... | Clean & Green Technolo... | 6.5 | 7.0 | 5.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 8.5 |
|  33 | SIH26033 | 5.70 | -0.14 | 6.35 | 5.25 | HIGH RISK | Multiple intermediaries reduce farmers earnings ... | Ministry of Consumer Affairs... | Agriculture, FoodTech ... | 5.5 | 7.0 | 7.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 8.5 |
|  34 | SIH26207 | 5.70 | +0.53 | 6.60 | 5.65 | HIGH RISK | Student Innovation-Smart education,a concept tha... | AICTE... | Smart Education... | 5.0 | 8.0 | 6.5 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  35 | SIH26094 | 5.69 | -0.23 | 6.98 | 5.60 | HIGH RISK | AI-Powered Dynamic Mental Health Monitoring and ... | Ministry of Social Justice a... | MedTech / BioTech / He... | 6.5 | 7.0 | 7.5 | 7.5 | 6.5 | 4.0 | 5.0 | 7.5 | 6.5 |
|  36 | SIH26141 | 5.69 | -0.08 | 6.10 | 6.90 | HIGH RISK | Quantum-Inspired Cyber Threat Detection for Digi... | Egreen Quanta... | Blockchain & Cybersecu... | 6.5 | 6.0 | 5.5 | 7.0 | 5.0 | 7.0 | 7.0 | 7.0 | 7.5 |
|  37 | SIH26093 | 5.67 | +0.18 | 6.98 | 5.70 | HIGH RISK | AI-Based Real-Time Stress and Trauma Assessment ... | Ministry of Social Justice a... | MedTech / BioTech / He... | 6.5 | 7.0 | 7.5 | 7.5 | 6.5 | 4.0 | 5.0 | 7.5 | 6.5 |
|  38 | SIH26018 | 5.65 | +0.61 | 7.18 | 7.70 | HIGH RISK | Intelligent Land Record Digitization and Validat... | Ministry of Rural Developmen... | Smart Automation... | 8.0 | 6.0 | 7.5 | 7.5 | 6.5 | 5.5 | 6.0 | 7.5 | 8.0 |
|  39 | SIH26043 | 5.64 | +0.35 | 6.48 | 5.90 | HIGH RISK | A digital platform to crowdsource societal chall... | Governmcnt of Jharkhand... | Smart Education... | 5.0 | 7.0 | 7.0 | 7.5 | 7.0 | 5.5 | 4.0 | 7.5 | 8.5 |
|  40 | SIH26186 | 5.64 | +0.21 | 6.90 | 6.90 | HIGH RISK | AI-Based Predictive Personnel Stress and Welfare... | Ministry of Home Affairs... | MedTech / BioTech / He... | 5.0 | 7.5 | 8.5 | 7.5 | 7.0 | 5.0 | 7.0 | 7.5 | 5.5 |
|  41 | SIH26203 | 5.64 | +0.41 | 6.30 | 5.40 | HIGH RISK | Student Innovation-Creating intelligent devices ... | AICTE... | Smart Vehicles... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  42 | SIH26205 | 5.64 | +0.25 | 6.45 | 5.65 | HIGH RISK | Student Innovation-Submit your ideas to address ... | AICTE... | Transportation & Logis... | 5.5 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  43 | SIH26133 | 5.63 | +0.44 | 6.88 | 6.30 | HIGH RISK | Accessibility and quality of public healthcare s... | Government Of Maharashtra... | MedTech / BioTech / He... | 6.5 | 7.0 | 7.0 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 6.5 |
|  44 | SIH26035 | 5.62 | +0.82 | 6.85 | 7.50 | HIGH RISK | Development of a Software Program/Application fo... | Ministry of Consumer Affairs... | Miscellaneous... | 5.5 | 7.5 | 7.5 | 7.5 | 7.0 | 5.0 | 7.0 | 7.5 | 8.5 |
|  45 | SIH26139 | 5.62 | +0.26 | 6.55 | 6.50 | HIGH RISK | Hybrid Quantum Machine Learning Platform for Ear... | Egreen Quanta... | MedTech / BioTech / He... | 7.5 | 6.0 | 7.0 | 6.0 | 5.0 | 5.0 | 7.0 | 6.0 | 7.5 |
|  46 | SIH26006 | 5.61 | -0.42 | 6.63 | 6.35 | HIGH RISK | Development of an Intelligent Freight Forecastin... | Ministry of Steel... | Transportation & Logis... | 6.5 | 7.0 | 5.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 8.5 |
|  47 | SIH26140 | 5.60 | +0.44 | 6.50 | 6.50 | HIGH RISK | AI-Based Interactive Quantum Algorithm Learning ... | Egreen Quanta... | Smart Education... | 7.5 | 6.0 | 6.5 | 6.0 | 5.5 | 5.0 | 7.0 | 6.0 | 7.5 |
|  48 | SIH26174 | 5.60 | +1.03 | 6.38 | 6.30 | HIGH RISK | AI Human Activity Recognition for On-board BAS E... | Indian Space Research Organi... | Space Technology... | 5.5 | 7.5 | 6.5 | 6.0 | 6.5 | 5.0 | 7.0 | 6.0 | 7.5 |
|  49 | SIH26037 | 5.58 | -0.25 | 6.05 | 6.05 | HIGH RISK | Adaptive Path Planning and Collision Avoidance f... | MathWorks... | Smart Vehicles... | 6.5 | 7.5 | 5.5 | 4.5 | 4.5 | 5.5 | 7.0 | 4.5 | 8.5 |
|  50 | SIH26209 | 5.58 | +0.04 | 6.30 | 5.65 | HIGH RISK | Student Innovation-Space technology refers to th... | AICTE... | Space Technology... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  51 | SIH26012 | 5.57 | +0.45 | 7.48 | 8.20 | HIGH RISK | AI-Based Automated Urban Parcel Mapping and Cada... | Ministry of Rural Developmen... | Smart Automation... | 8.0 | 7.0 | 7.5 | 7.5 | 7.0 | 5.0 | 6.0 | 7.5 | 8.0 |
|  52 | SIH26001 | 5.56 | -0.17 | 7.18 | 7.85 | HIGH RISK | AI-Based early warning and landslide Risk Monito... | Ministry of Development of N... | Disaster Management... | 8.0 | 6.0 | 7.5 | 7.5 | 6.5 | 5.0 | 6.0 | 7.5 | 8.5 |
|  53 | SIH26097 | 5.56 | -0.17 | 6.30 | 5.35 | HIGH RISK | AI-Driven voice Assistant for livelihood Mapping... | Ministry of Social Justice a... | Agriculture, FoodTech ... | 5.5 | 7.0 | 7.0 | 6.0 | 6.0 | 5.0 | 5.0 | 6.0 | 6.5 |
|  54 | SIH26074 | 5.55 | +0.31 | 6.45 | 5.20 | HIGH RISK | Downscaling of weather forecast from Block level... | Ministry of Earth Sciences (... | Agriculture, FoodTech ... | 5.5 | 7.0 | 7.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |
|  55 | SIH26009 | 5.54 | -0.44 | 6.10 | 5.50 | HIGH RISK | Using AI/ML and Space Technology to Identify Man... | Ministry of Steel... | Space Technology... | 5.5 | 7.0 | 5.5 | 6.0 | 7.0 | 5.0 | 5.0 | 6.0 | 8.5 |
|  56 | SIH26197 | 5.54 | +0.41 | 6.30 | 5.80 | HIGH RISK | Student Innovation-Ideas that showcase the rich ... | AICTE... | Heritage & Culture... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  57 | SIH26115 | 5.53 | +0.92 | 6.58 | 6.90 | HIGH RISK | Design and Develop a Smart Mobile Medical-Waste ... | Autodesk... | MedTech / BioTech / He... | 5.5 | 7.0 | 7.0 | 7.5 | 6.5 | 5.5 | 5.0 | 7.5 | 8.5 |
|  58 | SIH26119 | 5.53 | +0.59 | 6.58 | 7.40 | HIGH RISK | Indigenous GPU-Accelerated Optimization Solver (... | Mangalore Refinery and Petro... | Smart Automation... | 6.5 | 7.5 | 6.0 | 6.0 | 6.5 | 5.5 | 7.0 | 6.0 | 8.5 |
|  59 | SIH26196 | 5.52 | +0.42 | 6.30 | 5.90 | HIGH RISK | Student Innovation-Ideas that can boost fitness ... | AICTE... | Fitness & Sports... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  60 | SIH26201 | 5.52 | +0.36 | 6.45 | 6.15 | HIGH RISK | Student Innovation-There is a need to design dro... | AICTE... | Robotics and Drones... | 5.5 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  61 | SIH26204 | 5.52 | +0.42 | 6.30 | 5.90 | HIGH RISK | Student Innovation-A solution/idea that can boos... | AICTE... | Travel & Tourism... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  62 | SIH26032 | 5.51 | +0.15 | 6.58 | 7.00 | HIGH RISK | Farmers often face long waiting times, lack of i... | Ministry of Consumer Affairs... | Smart Automation... | 5.5 | 7.0 | 7.0 | 7.5 | 6.5 | 5.5 | 5.0 | 7.5 | 8.5 |
|  63 | SIH26206 | 5.47 | +0.46 | 6.80 | 6.90 | HIGH RISK | Student Innovation-Disaster management includes ... | AICTE... | Disaster Management... | 5.0 | 8.0 | 7.5 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  64 | SIH26013 | 5.46 | -0.31 | 6.50 | 6.75 | HIGH RISK | Automated lntegration and lntelligent Harmonizat... | Ministry of Rural Developmen... | Smart Automation... | 6.5 | 6.0 | 7.5 | 6.0 | 6.5 | 5.0 | 6.0 | 6.0 | 8.0 |
|  65 | SIH26166 | 5.46 | +0.66 | 6.45 | 6.70 | HIGH RISK | Multi-modal, Sun angle and scale invariant image... | Indian Space Research Organi... | Space Technology... | 6.5 | 7.5 | 6.5 | 4.5 | 6.5 | 5.0 | 7.0 | 4.5 | 7.5 |
|  66 | SIH26082 | 5.45 | +0.67 | 6.73 | 6.55 | HIGH RISK | Air Pollution–Weather Coupled Forecasting System... | Ministry of Earth Sciences (... | Clean & Green Technolo... | 5.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.0 | 5.5 | 7.5 | 4.5 |
|  67 | SIH26142 | 5.45 | +0.27 | 6.35 | 6.25 | HIGH RISK | Deep Learning Based Super Resolution Mapping (SR... | National Technical Research ... | Space Technology... | 6.5 | 7.5 | 6.0 | 4.5 | 6.5 | 5.5 | 7.0 | 4.5 | 4.5 |
|  68 | SIH26175 | 5.45 | -0.13 | 6.50 | 7.10 | HIGH RISK | DepthWizard - Single-View Height Estimation and ... | Indian Space Research Organi... | Disaster Management... | 6.5 | 7.0 | 7.5 | 6.0 | 4.0 | 5.0 | 8.0 | 6.0 | 5.5 |
|  69 | SIH26162 | 5.44 | -0.22 | 6.98 | 7.30 | HIGH RISK | AI-Based Detection and Classification of Industr... | National Technical Research ... | Disaster Management... | 6.5 | 7.5 | 8.0 | 6.0 | 6.5 | 5.0 | 7.0 | 6.0 | 4.5 |
|  70 | SIH26027 | 5.43 | +0.36 | 6.05 | 5.85 | HIGH RISK | Al-Powered Automatic Block Planning to Maximize ... | Ministry of Railways... | Transportation & Logis... | 5.5 | 7.0 | 5.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 8.5 |
|  71 | SIH26132 | 5.42 | +0.21 | 6.65 | 6.45 | HIGH RISK | Strengthening market linkages and price discover... | Government Of Maharashtra... | Agriculture, FoodTech ... | 6.5 | 7.0 | 7.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 6.5 |
|  72 | SIH26158 | 5.41 | +0.57 | 6.81 | 7.15 | HIGH RISK | Single-Pass Drone Video to Accurate 3D Model Gen... | National Technical Research ... | Robotics and Drones... | 7.3 | 7.5 | 6.0 | 6.0 | 6.5 | 5.0 | 7.0 | 6.0 | 4.5 |
|  73 | SIH26054 | 5.39 | -0.22 | 6.64 | 6.95 | HIGH RISK | AI-Enabled Real-Time Digital Twin System for Hea... | DRDO... | Robotics and Drones... | 7.3 | 7.0 | 5.5 | 6.0 | 7.0 | 5.0 | 5.5 | 6.0 | 7.5 |
|  74 | SIH26100 | 5.39 | +0.70 | 6.30 | 6.90 | HIGH RISK | AI-Powered Integrated Bid Compliance Verificatio... | Ministry of Petroleum & Natu... | Smart Automation... | 5.0 | 7.5 | 5.5 | 7.5 | 7.0 | 4.0 | 7.0 | 7.5 | 8.5 |
|  75 | SIH26103 | 5.39 | -0.17 | 6.98 | 7.80 | HIGH RISK | Use case on web-based integrated project-monitor... | MoSPI... | Smart Automation... | 6.5 | 8.0 | 6.0 | 7.5 | 7.0 | 4.0 | 7.0 | 7.5 | 7.5 |
|  76 | SIH26200 | 5.39 | +0.41 | 6.30 | 6.40 | HIGH RISK | Student Innovation-Innovative ideas that help ma... | AICTE... | Renewable / Sustainabl... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  77 | SIH26107 | 5.38 | +0.28 | 6.58 | 6.60 | HIGH RISK | Al-powered Intelligent Assistant for Indian Stan... | Ministry of Consumer Affairs... | Smart Automation... | 5.5 | 7.0 | 7.0 | 7.5 | 6.5 | 4.0 | 5.0 | 7.5 | 8.5 |
|  78 | SIH26108 | 5.38 | +0.22 | 6.58 | 6.60 | HIGH RISK | AI-Powered Recommendation Engine for Identifying... | Ministry of Consumer Affairs... | Smart Automation... | 5.5 | 7.0 | 7.0 | 7.5 | 6.5 | 4.0 | 5.0 | 7.5 | 8.5 |
|  79 | SIH26016 | 5.37 | -0.03 | 7.10 | 7.80 | HIGH RISK | Real-Time National Land Acquisition & Management... | Ministry of Rural Developmen... | Smart Automation... | 6.5 | 6.5 | 8.5 | 7.5 | 7.0 | 4.0 | 6.0 | 7.5 | 8.0 |
|  80 | SIH26034 | 5.37 | +0.82 | 6.60 | 7.50 | HIGH RISK | Software System to check compliance of Packaged ... | Ministry of Consumer Affairs... | Miscellaneous... | 5.0 | 7.5 | 7.0 | 7.5 | 7.0 | 4.0 | 7.0 | 7.5 | 8.5 |
|  81 | SIH26028 | 5.35 | +1.18 | 6.63 | 7.70 | HIGH RISK | Dynamic Forecast of Expected Time of Arrival (ET... | Ministry of Railways... | Smart Automation... | 6.5 | 7.0 | 5.5 | 7.5 | 7.0 | 5.5 | 5.0 | 7.5 | 8.5 |
|  82 | SIH26031 | 5.35 | +0.19 | 6.62 | 7.40 | HIGH RISK | Quality assessment and grading of onions are oft... | Ministry of Consumer Affairs... | Smart Automation... | 5.5 | 7.0 | 7.0 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 8.5 |
|  83 | SIH26102 | 5.33 | +0.18 | 6.45 | 7.80 | HIGH RISK | Development of an AI-powered system to detect an... | MoSPI... | Smart Automation... | 5.5 | 7.5 | 5.5 | 7.5 | 7.0 | 5.0 | 7.0 | 7.5 | 7.5 |
|  84 | SIH26194 | 5.33 | +0.49 | 6.30 | 6.65 | HIGH RISK | Student Innovation-Provide ideas in a decentrali... | AICTE... | Blockchain & Cybersecu... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  85 | SIH26053 | 5.29 | -0.47 | 5.83 | 5.85 | HIGH RISK | Adaptive Variable Resolution 2.5D Lidar Mapping ... | DRDO... | Smart Vehicles... | 6.5 | 5.5 | 5.5 | 6.0 | 5.0 | 5.0 | 5.0 | 6.0 | 7.5 |
|  86 | SIH26099 | 5.29 | +1.19 | 6.60 | 8.40 | HIGH RISK | AI-Driven Standardization and Harmonization of M... | Ministry of Petroleum & Natu... | Smart Automation... | 6.5 | 6.5 | 6.0 | 7.5 | 7.0 | 5.0 | 7.0 | 7.5 | 8.5 |
|  87 | SIH26136 | 5.28 | +0.53 | 6.05 | 6.35 | HIGH RISK | Startup friendly public procurement mechanism th... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 6.0 | 6.5 | 5.5 | 5.0 | 6.0 | 6.5 |
|  88 | SIH26077 | 5.26 | -0.13 | 6.80 | 7.85 | HIGH RISK | AI-Driven Hyper-Local Early Warning System for S... | Ministry of Earth Sciences (... | Disaster Management... | 6.5 | 7.0 | 7.5 | 6.0 | 7.0 | 5.0 | 6.0 | 6.0 | 7.0 |
|  89 | SIH26078 | 5.25 | +0.89 | 7.03 | 8.35 | HIGH RISK | AI-Driven Spatio-Temporal Tracking of Extreme We... | Ministry of Earth Sciences (... | Smart Automation... | 6.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.5 | 6.0 | 7.5 | 4.5 |
|  90 | SIH26091 | 5.25 | -0.23 | 6.60 | 6.45 | HIGH RISK | AI-Driven Hyper-Local Business Advisory and Fina... | Ministry of Social Justice a... | Agriculture, FoodTech ... | 6.5 | 7.0 | 7.0 | 6.0 | 6.0 | 4.0 | 5.0 | 6.0 | 6.5 |
|  91 | SIH26090 | 5.24 | -0.31 | 6.58 | 7.35 | HIGH RISK | AI-Driven Market Linkage and Smart Cataloging Mo... | Ministry of Social Justice a... | Heritage & Culture... | 6.5 | 7.0 | 5.5 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 6.5 |
|  92 | SIH26084 | 5.22 | -0.82 | 7.03 | 8.45 | HIGH RISK | Convective scale nowcasting for Thunderstorms, H... | Ministry of Earth Sciences (... | Disaster Management... | 6.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.0 | 5.5 | 7.5 | 7.0 |
|  93 | SIH26191 | 5.22 | +0.04 | 6.78 | 7.55 | HIGH RISK | Intelligent Identification of Hazard-Based Red Z... | Ministry of Home Affairs... | Disaster Management... | 5.5 | 7.0 | 8.0 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 5.5 |
|  94 | SIH26044 | 5.21 | +0.56 | 6.28 | 6.80 | HIGH RISK | Portal for Academia - Industry collaboration for... | Ministry of Ayush... | Smart Automation... | 5.0 | 7.0 | 6.0 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 8.5 |
|  95 | SIH26056 | 5.21 | -0.27 | 6.53 | 7.80 | HIGH RISK | Development of a Real-time Airfare Price Index f... | MoSPI... | Smart Automation... | 5.0 | 8.0 | 6.0 | 7.5 | 7.0 | 4.0 | 7.0 | 7.5 | 7.5 |
|  96 | SIH26202 | 5.21 | +0.36 | 6.30 | 7.15 | HIGH RISK | Student Innovation-Ideas focused on the intellig... | AICTE... | Smart Automation... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
|  97 | SIH26061 | 5.20 | +0.55 | 6.23 | 5.95 | HIGH RISK | AI-Driven Smart Energy Management System for Pol... | Ministry of Earth Sciences (... | Clean & Green Technolo... | 5.5 | 7.0 | 7.5 | 4.5 | 6.5 | 5.0 | 5.0 | 4.5 | 4.5 |
|  98 | SIH26085 | 5.20 | -0.23 | 6.73 | 7.85 | HIGH RISK | Urban Flood Nowcasting System (Drainage and Rain... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 7.0 |
|  99 | SIH26060 | 5.18 | +0.37 | 7.21 | 8.20 | HIGH RISK | Digital Platform for efficient remote management... | Ministry of Earth Sciences (... | Smart Automation... | 7.3 | 7.0 | 7.5 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 4.5 |
| 100 | SIH26165 | 5.18 | +0.17 | 6.33 | 7.40 | HIGH RISK | AI/NLP Engine to Detect Serious Injury & Fatalit... | Oil India Limited... | Smart Automation... | 5.5 | 7.0 | 5.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 7.5 |
| 101 | SIH26086 | 5.17 | -0.14 | 6.45 | 6.75 | HIGH RISK | Hyperlocal Monsoon Onset & Break Prediction Syst... | Ministry of Earth Sciences (... | Agriculture, FoodTech ... | 5.5 | 7.0 | 7.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |
| 102 | SIH26075 | 5.16 | +0.39 | 6.58 | 6.70 | HIGH RISK | Participants are invited to design and develop *... | Ministry of Earth Sciences (... | Smart Education... | 5.0 | 7.0 | 7.5 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 4.5 |
| 103 | SIH26059 | 5.12 | +0.06 | 6.45 | 6.95 | HIGH RISK | AI-Enabled Antarctic Sea-Ice, Iceberg Trajectory... | Ministry of Earth Sciences (... | Transportation & Logis... | 5.5 | 7.0 | 7.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |
| 104 | SIH26182 | 5.12 | -0.18 | 6.42 | 7.70 | HIGH RISK | Automated Attribution of Unknown Cryptocurrency ... | Ministry of Home Affairs... | Blockchain & Cybersecu... | 5.0 | 6.0 | 8.0 | 7.5 | 7.0 | 5.5 | 5.0 | 7.5 | 5.5 |
| 105 | SIH26063 | 5.11 | +0.86 | 6.35 | 6.20 | HIGH RISK | Integrated Polar Science Outreach, Knowledge Rep... | Ministry of Earth Sciences (... | Smart Education... | 5.0 | 7.0 | 7.5 | 6.0 | 7.0 | 4.0 | 5.0 | 6.0 | 4.5 |
| 106 | SIH26069 | 5.11 | -0.46 | 6.67 | 8.55 | HIGH RISK | National Weather Big Data Analytics Platform... | Ministry of Earth Sciences (... | Disaster Management... | 5.0 | 7.0 | 8.0 | 7.5 | 7.0 | 5.0 | 6.0 | 7.5 | 7.0 |
| 107 | SIH26083 | 5.10 | -0.11 | 6.73 | 8.25 | HIGH RISK | Extreme Heatwave Early Warning and Human Thermal... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 7.0 |
| 108 | SIH26106 | 5.10 | +0.85 | 6.25 | 7.80 | HIGH RISK | AI-Powered Email Threat Detection, GeoLocation a... | All India Council for Techni... | Blockchain & Cybersecu... | 6.5 | 5.5 | 5.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 8.5 |
| 109 | SIH26124 | 5.10 | +0.60 | 6.63 | 8.20 | HIGH RISK | AI-Powered Mobile Urban Intelligence Platform Us... | Bharat Electronics Limited... | Smart Automation... | 6.5 | 7.0 | 5.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 7.5 |
| 110 | SIH26163 | 5.10 | +0.48 | 6.50 | 8.60 | HIGH RISK | Security Assessment of the World Monitor applica... | National Technical Research ... | Smart Automation... | 5.5 | 7.5 | 6.0 | 7.5 | 6.5 | 5.0 | 8.0 | 7.5 | 4.5 |
| 111 | SIH26120 | 5.09 | +0.19 | 6.29 | 7.40 | HIGH RISK | Digital Twin for Well-to-Surface Optimization of... | Oil India Limited... | Smart Automation... | 6.3 | 7.0 | 5.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 7.5 |
| 112 | SIH26125 | 5.09 | +0.30 | 5.90 | 7.10 | HIGH RISK | Blockchain-Based Secure Platform for Identity,Ac... | Bharat Electronics Limited... | Blockchain & Cybersecu... | 5.5 | 5.5 | 5.5 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 7.5 |
| 113 | SIH26187 | 5.09 | +0.21 | 6.85 | 7.90 | HIGH RISK | AI-Based Intelligent Video Analytics Platform fo... | Ministry of Home Affairs... | Blockchain & Cybersecu... | 6.5 | 7.0 | 8.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 5.5 |
| 114 | SIH26189 | 5.09 | +0.01 | 6.85 | 7.90 | HIGH RISK | AI-Powered Criminal Network Analysis System... | Ministry of Home Affairs... | Blockchain & Cybersecu... | 6.5 | 7.0 | 8.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 5.5 |
| 115 | SIH26081 | 5.08 | +0.24 | 6.73 | 8.35 | HIGH RISK | Hybrid AI–NWP Multi-Model Forecast Blending Syst... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 7.0 |
| 116 | SIH26079 | 5.07 | +0.47 | 6.73 | 8.20 | HIGH RISK | AI-Based Forecast Bust Detection for Medium-Rang... | Ministry of Earth Sciences (... | Smart Automation... | 5.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.5 | 5.0 | 7.5 | 4.5 |
| 117 | SIH26160 | 5.07 | +0.15 | 6.42 | 7.40 | HIGH RISK | AI-Powered IPsec VPN Protocol Analyzer and Secur... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 7.0 | 6.0 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 4.5 |
| 118 | SIH26228 | 5.07 | +0.40 | 6.25 | 8.10 | HIGH RISK | Trustworthy Computer Vision Integrity Assurance ... | Ministry of defence (MoD)... | Blockchain & Cybersecu... | 6.5 | 7.5 | 5.5 | 4.5 | 6.5 | 5.0 | 7.0 | 4.5 | 8.5 |
| 119 | SIH26073 | 5.06 | -0.48 | 6.50 | 8.25 | HIGH RISK | AI/ML-Based Intelligent Anomaly Detection for Au... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 6.0 | 7.0 | 5.5 | 5.5 | 6.0 | 7.0 |
| 120 | SIH26134 | 5.06 | +0.20 | 6.28 | 7.60 | HIGH RISK | Challenges in aligning skill development program... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 6.5 |
| 121 | SIH26155 | 5.06 | -0.02 | 6.33 | 7.80 | HIGH RISK | AI-Driven Multi-Vendor Network Security Complian... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 7.5 | 6.0 | 6.0 | 7.0 | 5.0 | 7.0 | 6.0 | 4.5 |
| 122 | SIH26183 | 5.06 | +0.36 | 6.20 | 7.30 | HIGH RISK | Real-Time Identification of Fraud-Linked Cryptoc... | Ministry of Home Affairs... | Blockchain & Cybersecu... | 5.5 | 4.5 | 8.0 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 5.5 |
| 123 | SIH26092 | 5.05 | +0.03 | 6.63 | 8.20 | HIGH RISK | AI-Driven Scheme Matching for Marginalized Entre... | Ministry of Social Justice a... | Smart Automation... | 6.5 | 7.0 | 5.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 6.5 |
| 124 | SIH26190 | 5.04 | +0.27 | 6.48 | 7.50 | HIGH RISK | Secure Digital Document Management System for Le... | Ministry of Home Affairs... | Blockchain & Cybersecu... | 6.5 | 5.5 | 8.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 5.5 |
| 125 | SIH26057 | 5.03 | +0.07 | 7.10 | 8.55 | HIGH RISK | AI-Powered Automated Underwater Marine Debris an... | Ministry of Earth Sciences (... | Disaster Management... | 8.0 | 5.5 | 7.5 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 7.0 |
| 126 | SIH26062 | 5.03 | +0.07 | 6.08 | 6.70 | HIGH RISK | Integrated Polar Expedition Logistics and Asset ... | Ministry of Earth Sciences (... | Smart Automation... | 5.5 | 5.5 | 7.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |
| 127 | SIH26121 | 5.03 | +0.13 | 6.17 | 7.15 | HIGH RISK | eRTMAC-NWIS (Nearby Wells Intelligence System): ... | Oil India Limited... | Smart Automation... | 5.0 | 7.0 | 5.5 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 7.5 |
| 128 | SIH26161 | 5.03 | -0.63 | 6.48 | 8.15 | HIGH RISK | Dam Break Inundation Modelling Using Hydrodynami... | National Technical Research ... | Disaster Management... | 5.5 | 6.5 | 8.0 | 6.0 | 7.0 | 5.0 | 7.0 | 6.0 | 4.5 |
| 129 | SIH26188 | 5.03 | +0.59 | 6.88 | 7.90 | HIGH RISK | Al-Based Fake Identity & Document Screening Syst... | Ministry of Home Affairs... | Blockchain & Cybersecu... | 5.5 | 7.0 | 8.5 | 7.5 | 6.5 | 4.0 | 5.0 | 7.5 | 5.5 |
| 130 | SIH26130 | 5.01 | +0.34 | 6.33 | 7.90 | HIGH RISK | Efficiency in streamlining industrial approvals,... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 6.5 |
| 131 | SIH26192 | 5.01 | -0.49 | 6.63 | 7.55 | HIGH RISK | Flash Flood Prediction System for Hilly Regions ... | Ministry of Home Affairs... | Disaster Management... | 6.5 | 7.0 | 8.0 | 4.5 | 6.5 | 5.0 | 5.0 | 4.5 | 5.5 |
| 132 | SIH26152 | 5.00 | +0.50 | 6.68 | 8.10 | HIGH RISK | Social Media Analytics... | National Technical Research ... | Blockchain & Cybersecu... | 6.5 | 7.0 | 6.0 | 7.5 | 6.5 | 5.0 | 5.0 | 7.5 | 4.5 |
| 133 | SIH26023 | 4.99 | +0.50 | 6.28 | 7.70 | HIGH RISK | AI-Powered Geological, Mining and other Reportin... | Ministry of Coal... | Smart Automation... | 5.5 | 7.0 | 5.5 | 7.5 | 6.5 | 4.0 | 5.0 | 7.5 | 8.5 |
| 134 | SIH26123 | 4.99 | +0.41 | 6.10 | 7.50 | HIGH RISK | Edge-AI Based Distributed Fleet Coordination for... | Bharat Electronics Limited... | Smart Automation... | 5.5 | 7.0 | 5.5 | 6.0 | 7.0 | 5.0 | 5.0 | 6.0 | 7.5 |
| 135 | SIH26129 | 4.98 | +0.43 | 6.50 | 7.70 | HIGH RISK | System integration and interoperability among go... | Government Of Maharashtra... | Miscellaneous... | 6.5 | 6.5 | 5.5 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 6.5 |
| 136 | SIH26076 | 4.97 | +0.10 | 6.73 | 8.30 | HIGH RISK | Development of personalized homepage for 'Mausam... | Ministry of Earth Sciences (... | Smart Automation... | 5.5 | 7.0 | 7.5 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 4.5 |
| 137 | SIH26024 | 4.96 | -0.37 | 6.65 | 8.40 | HIGH RISK | AI-Based Smart Governance and Compliance Monitor... | Ministry of Coal... | Smart Automation... | 8.0 | 5.5 | 5.5 | 7.5 | 6.5 | 4.0 | 5.0 | 7.5 | 8.5 |
| 138 | SIH26104 | 4.96 | +0.07 | 6.15 | 8.10 | HIGH RISK | AI-Powered Real-Time Detection and Prevention of... | All India Council for Techni... | Blockchain & Cybersecu... | 6.5 | 6.0 | 6.0 | 6.0 | 6.0 | 5.0 | 5.5 | 6.0 | 8.5 |
| 139 | SIH26116 | 4.94 | +0.41 | 6.05 | 8.10 | HIGH RISK | Urban Mixed-Use Design Challenge-Design a centra... | Autodesk... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 6.0 | 6.5 | 5.5 | 5.0 | 6.0 | 8.5 |
| 140 | SIH26146 | 4.94 | -0.01 | 6.05 | 7.40 | HIGH RISK | AI-Powered Monitoring & Analysis of Bitcoin Tran... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 5.5 | 6.0 | 7.5 | 7.0 | 5.5 | 4.5 | 7.5 | 4.5 |
| 141 | SIH26147 | 4.94 | +0.11 | 5.92 | 6.50 | HIGH RISK | Automated model for analysis of .IQ and .wav fil... | National Technical Research ... | Space Technology... | 5.5 | 7.0 | 6.0 | 4.5 | 6.5 | 5.0 | 5.0 | 4.5 | 4.5 |
| 142 | SIH26154 | 4.94 | -0.02 | 6.42 | 7.90 | HIGH RISK | Gen AI Platform for Automated Content Transforma... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 7.0 | 6.0 | 7.5 | 7.0 | 5.0 | 5.0 | 7.5 | 4.5 |
| 143 | SIH26070 | 4.93 | -0.26 | 6.23 | 7.95 | HIGH RISK | To develop an Artificial Intelligence (AI) / Mac... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 4.5 | 6.5 | 5.0 | 6.0 | 4.5 | 7.0 |
| 144 | SIH26143 | 4.91 | +0.10 | 6.75 | 8.75 | HIGH RISK | Leveraging satellite imagery to determine Oil sp... | National Technical Research ... | Disaster Management... | 6.5 | 7.5 | 8.0 | 4.5 | 6.5 | 5.0 | 7.0 | 4.5 | 4.5 |
| 145 | SIH26068 | 4.89 | -0.59 | 6.50 | 7.85 | HIGH RISK | WeatherGPT: Conversational AI for Weather Foreca... | Ministry of Earth Sciences (... | Disaster Management... | 6.5 | 6.0 | 7.5 | 6.0 | 6.5 | 4.0 | 5.0 | 6.0 | 7.0 |
| 146 | SIH26199 | 4.89 | +0.29 | 6.30 | 8.40 | HIGH RISK | Student Innovation-Technology ideas in tertiary ... | AICTE... | Miscellaneous... | 5.0 | 8.0 | 5.0 | 7.0 | 7.5 | 5.0 | 6.0 | 7.0 | 5.5 |
| 147 | SIH26126 | 4.88 | +0.15 | 6.13 | 7.70 | HIGH RISK | Vision Based Autonomous Navigation for Unmanned ... | Bharat Electronics Limited... | Smart Automation... | 6.5 | 7.0 | 5.5 | 4.5 | 6.5 | 5.0 | 5.0 | 4.5 | 7.5 |
| 148 | SIH26171 | 4.85 | +0.91 | 6.25 | 8.40 | HIGH RISK | On-device Visual Perception for Light-weight Bro... | Indian Space Research Organi... | Smart Automation... | 6.5 | 7.5 | 5.5 | 4.5 | 6.5 | 5.0 | 7.0 | 4.5 | 5.5 |
| 149 | SIH26051 | 4.84 | +0.60 | 6.05 | 8.20 | HIGH RISK | Software Based Model Development for Design of A... | DRDO... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 6.0 | 6.5 | 5.0 | 5.5 | 6.0 | 7.5 |
| 150 | SIH26071 | 4.83 | -0.22 | 6.23 | 7.95 | HIGH RISK | AI/ML-Based Integrated heavy rainfall Early Warn... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 4.5 | 6.5 | 5.0 | 5.0 | 4.5 | 7.0 |
| 151 | SIH26072 | 4.83 | -0.55 | 6.23 | 7.95 | HIGH RISK | AIML based Nowcasting of thunderstorm and lightn... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 4.5 | 6.5 | 5.0 | 5.0 | 4.5 | 7.0 |
| 152 | SIH26105 | 4.82 | -0.43 | 6.17 | 8.40 | HIGH RISK | AI-Powered Continuous Cyber Risk Quantification ... | All India Council for Techni... | Blockchain & Cybersecu... | 5.0 | 7.0 | 5.5 | 7.5 | 7.0 | 4.0 | 5.5 | 7.5 | 8.5 |
| 153 | SIH26164 | 4.82 | -0.18 | 6.05 | 8.10 | HIGH RISK | Enterprise Cryptographic Discovery & Analysis To... | National Technical Research ... | Blockchain & Cybersecu... | 6.5 | 6.0 | 6.0 | 6.0 | 5.0 | 4.0 | 8.0 | 6.0 | 4.5 |
| 154 | SIH26169 | 4.82 | +0.48 | 6.35 | 8.40 | HIGH RISK | Development of an AI-Based Virtual Camera Tracki... | Indian Space Research Organi... | Smart Automation... | 6.5 | 7.0 | 5.5 | 6.0 | 6.5 | 5.0 | 5.5 | 6.0 | 5.5 |
| 155 | SIH26067 | 4.80 | +0.45 | 6.23 | 7.75 | HIGH RISK | Develop a web-based interactive 3D visualization... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 5.5 | 8.0 | 6.0 | 7.0 | 4.0 | 5.0 | 6.0 | 7.0 |
| 156 | SIH26080 | 4.80 | +0.18 | 6.45 | 8.20 | HIGH RISK | Regime-Aware AI Post-Processing of Monsoon Rainf... | Ministry of Earth Sciences (... | Smart Automation... | 5.5 | 7.0 | 7.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |
| 157 | SIH26127 | 4.80 | +0.06 | 6.63 | 8.80 | HIGH RISK | City-Wide AI Engine for Multi-Camera ANPR Trajec... | Bharat Electronics Limited... | Smart Automation... | 6.5 | 7.0 | 5.5 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 7.5 |
| 158 | SIH26114 | 4.79 | +0.17 | 6.05 | 8.40 | HIGH RISK | Smart City Site Planning using Autodesk Forma Si... | Autodesk... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 8.5 |
| 159 | SIH26055 | 4.78 | +0.48 | 5.68 | 7.55 | HIGH RISK | Smart Scan strategy for Electronic Warfare... | DRDO... | Robotics and Drones... | 6.5 | 6.0 | 5.5 | 4.5 | 4.5 | 4.0 | 7.0 | 4.5 | 7.5 |
| 160 | SIH26153 | 4.78 | -0.68 | 6.58 | 8.70 | HIGH RISK | AI based Network Attack Forecasting from Network... | National Technical Research ... | Blockchain & Cybersecu... | 6.5 | 7.5 | 6.0 | 6.0 | 6.5 | 4.0 | 7.0 | 6.0 | 4.5 |
| 161 | SIH26122 | 4.76 | +0.73 | 5.90 | 8.60 | HIGH RISK | Intelligent Data Capture & Schedule-Linking Laye... | Oil India Limited... | Smart Automation... | 5.0 | 7.0 | 5.5 | 6.0 | 6.5 | 5.5 | 5.5 | 6.0 | 7.5 |
| 162 | SIH26148 | 4.74 | -0.32 | 5.78 | 7.40 | HIGH RISK | Creation of scripts/functions with new programmi... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 5.5 | 6.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |
| 163 | SIH26156 | 4.74 | -1.14 | 5.78 | 7.40 | HIGH RISK | Universal Log Pre-processing Framework... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 5.5 | 6.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |
| 164 | SIH26157 | 4.73 | -0.75 | 6.20 | 8.10 | HIGH RISK | Supervisory Analytics Tool for SOC Assessment (S... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 7.0 | 6.0 | 6.0 | 7.0 | 5.0 | 5.0 | 6.0 | 4.5 |
| 165 | SIH26159 | 4.73 | -0.61 | 5.95 | 8.50 | HIGH RISK | SecureMailScope: AI-Assisted Cryptographic Secur... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 6.0 | 6.0 | 6.0 | 7.0 | 5.0 | 7.0 | 6.0 | 4.5 |
| 166 | SIH26066 | 4.68 | +0.41 | 6.23 | 8.55 | HIGH RISK | OceanEmbed - Satellite Embedding-Based Deep Lear... | Ministry of Earth Sciences (... | Disaster Management... | 5.5 | 7.0 | 7.5 | 4.5 | 6.5 | 5.0 | 5.0 | 4.5 | 7.0 |
| 167 | SIH26173 | 4.68 | -0.41 | 6.08 | 8.00 | HIGH RISK | iTantra -Indian Multilingual TTS & STT Aided Neu... | Indian Space Research Organi... | Smart Automation... | 6.5 | 7.0 | 5.5 | 4.5 | 6.0 | 5.0 | 5.0 | 4.5 | 5.5 |
| 168 | SIH26170 | 4.65 | -0.57 | 6.05 | 8.40 | HIGH RISK | AI-Driven Anomaly Detection in Component Burn-In... | Indian Space Research Organi... | Smart Automation... | 5.5 | 7.0 | 5.5 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 5.5 |
| 169 | SIH26095 | 4.63 | -0.16 | 5.88 | 8.10 | HIGH RISK | Smart Real-Time Monitoring & Inspection Mobile A... | Ministry of Social Justice a... | Smart Automation... | 4.0 | 7.0 | 5.5 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 6.5 |
| 170 | SIH26117 | 4.62 | +0.26 | 5.80 | 8.60 | HIGH RISK | Sovereign On-Premise Agentic AI Workbench using ... | Mangalore Refinery and Petro... | Smart Automation... | 5.0 | 7.5 | 5.5 | 4.5 | 6.5 | 4.0 | 7.0 | 4.5 | 8.5 |
| 171 | SIH26145 | 4.62 | +0.09 | 5.80 | 8.10 | HIGH RISK | AI-Based Detection of Cyber Threats in Unidirect... | National Technical Research ... | Blockchain & Cybersecu... | 5.0 | 6.0 | 6.0 | 6.0 | 7.0 | 4.0 | 7.0 | 6.0 | 4.5 |
| 172 | SIH26135 | 4.60 | +0.14 | 6.05 | 8.20 | HIGH RISK | Difficulties in tracking employment outcomes,ski... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 6.0 | 6.5 | 4.0 | 5.0 | 6.0 | 6.5 |
| 173 | SIH26149 | 4.58 | -0.08 | 5.83 | 8.10 | HIGH RISK | Design and Development of an Integrated Secure D... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 5.5 | 6.0 | 6.0 | 7.0 | 5.0 | 5.0 | 6.0 | 4.5 |
| 174 | SIH26151 | 4.54 | -0.38 | 6.28 | 8.70 | HIGH RISK | Dark web threat actor de-anonymization... | National Technical Research ... | Blockchain & Cybersecu... | 5.0 | 7.0 | 6.0 | 7.5 | 7.0 | 4.0 | 5.0 | 7.5 | 4.5 |
| 175 | SIH26150 | 4.46 | -0.25 | 5.78 | 8.50 | HIGH RISK | Development of a Multi-Vendor DVR/NVR Forensic A... | National Technical Research ... | Blockchain & Cybersecu... | 5.5 | 5.5 | 6.0 | 6.0 | 6.5 | 5.0 | 5.0 | 6.0 | 4.5 |

---

## Biggest rank movers v2 vs v1 (raw-data correction signal)

### Most improved in v2 (v1 undervalued — text signals added)

| PS ID | v1 rank | v2 rank | Δ rank | WPS v1→v2 | CLS v1→v2 | Why v2 higher |
|-------|---------|---------|--------|-----------|-----------|---------------|
| SIH26227 | 151 | 20 | +131 | 4.60→5.85 | 7.10→5.65 | CLS −1.45 (Space Tech niche, MoD not hype) |
| SIH26168 | 124 | 14 | +110 | 4.83→5.96 | 6.05→6.05 | Q 5.68→6.75 (ISRO demo + dataset_link) |
| SIH26174 | 153 | 48 | +105 | 4.57→5.60 | 6.30→6.30 | Dataset 5.0→7.0 (link) |
| SIH26028 | 172 | 81 | +91 | 4.17→5.35 | 8.20→7.70 | Dataset 4.0→5.0 (link) |
| SIH26115 | 148 | 57 | +91 | 4.61→5.53 | 6.10→6.90 | Q 4.90→6.58 (feas/impact rebased) |
| SIH26099 | 173 | 86 | +87 | 4.10→5.29 | 8.10→8.40 | Dataset 5.0→7.0 (link) |
| SIH26176 | 108 | 24 | +84 | 4.96→5.80 | 6.30→6.20 | Dataset 4.0→6.0 (link) |
| SIH26035 | 127 | 44 | +83 | 4.80→5.62 | 7.10→7.50 | Dataset 4.0→7.0 (link) |
| SIH26034 | 154 | 80 | +74 | 4.55→5.37 | 7.50→7.50 | Dataset 4.0→7.0 (link) |
| SIH26078 | 163 | 89 | +74 | 4.36→5.25 | 8.10→8.35 | Dataset 5.0→6.0 (link) |

### Most dropped in v2 (v1 overvalued — feasibility/diff deflated)

| PS ID | v1 rank | v2 rank | Δ rank | WPS v1→v2 | CLS v1→v2 | Why v2 lower |
|-------|---------|---------|--------|-----------|-----------|--------------|
| SIH26156 | 17 | 163 | -146 | 5.88→4.74 | 7.50→7.40 | NTRO diff 6.0→5.0 + dataset 9.0→5.0 (no link) |
| SIH26157 | 49 | 164 | -115 | 5.48→4.73 | 6.25→8.10 | Dataset 9.0→5.0 (hard infra, no link) |
| SIH26153 | 50 | 160 | -110 | 5.46→4.78 | 7.50→8.70 | Q 5.95→6.58, diff 6.0→4.0 |
| SIH26159 | 61 | 165 | -104 | 5.34→4.73 | 7.40→8.50 | Q 6.35→5.95, diff 6.0→5.0 |
| SIH26068 | 47 | 145 | -98 | 5.48→4.89 | 8.25→7.85 | Q 7.73→6.50, diff 6.0→4.0 |
| SIH26161 | 31 | 128 | -97 | 5.66→5.03 | 6.50→8.15 | Q 5.28→6.48, diff 7.5→5.0 |
| SIH26170 | 71 | 168 | -97 | 5.22→4.65 | 7.70→8.40 | Q 6.73→6.05, diff 6.0→5.0 |
| SIH26072 | 57 | 151 | -94 | 5.38→4.83 | 7.95→7.95 | Q 6.93→6.23, diff 6.0→5.0 |
| SIH26192 | 44 | 131 | -87 | 5.50→5.01 | 7.95→7.55 | Q 6.65→6.63, diff 7.5→5.0 |
| SIH26105 | 68 | 152 | -84 | 5.25→4.82 | 7.80→8.40 | Q 6.13→6.17, diff 6.0→4.0 |

---

## Hidden Gems v2 — Lowest CLS (least crowded, submit ≤19 Sep safe)

| Rank | PS ID | CLS | WPS | Quality | Title | Org | Theme |
|------|-------|-----|-----|---------|-------|-----|-------|
|  1 | SIH26045 | 3.35 | 7.20 | 7.47 | IP-SAKTI Sahayak a multilingual, RAG-based (source-cited) ... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  2 | SIH26046 | 3.55 | 6.50 | 6.60 | AIIA Clinical Trials Dashboard - a real-time, cloud-based,... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  3 | SIH26047 | 3.85 | 6.86 | 7.42 | Patient Case-Taking Software... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  4 | SIH26128 | 4.35 | 6.11 | 6.88 | Efficient systems for early detection,prevention,and manag... | Government Of Maharashtra... | MedTech / BioTech / HealthTech |
|  5 | SIH26131 | 4.80 | 5.83 | 6.65 | Early detection and management of crop diseases and pest i... | Government Of Maharashtra... | Agriculture, FoodTech & Rural Development |
|  6 | SIH26195 | 4.90 | 5.77 | 6.30 | Student Innovation-Solutions could be in the form of waste... | AICTE... | Clean & Green Technology |
|  7 | SIH26208 | 4.90 | 5.77 | 6.30 | Student Innovation-Challenge your creative mind to concept... | AICTE... | Toys & Games |
|  8 | SIH26014 | 5.00 | 6.77 | 7.62 | An lntegrated GIS-based Digital Public lnfrastructure for ... | Ministry of Rural Development... | Agriculture, FoodTech & Rural Development |
|  9 | SIH26015 | 5.00 | 6.00 | 6.75 | Application of Geospatial Techniques for visualization and... | Ministry of Rural Development... | Agriculture, FoodTech & Rural Development |
| 10 | SIH26036 | 5.05 | 6.61 | 7.05 | Development of an Online Verification System for Weighing ... | Ministry of Consumer Affairs, Fo... | Miscellaneous |
| 11 | SIH26138 | 5.05 | 6.33 | 6.47 | Quantum-Inspired Fuel Consumption Prediction and Green Fle... | Egreen Quanta... | Clean & Green Technology |
| 12 | SIH26089 | 5.05 | 6.04 | 6.88 | Cooperative Gig Services Platform for Household & Communit... | Ministry of Cooperation... | Agriculture, FoodTech & Rural Development |
| 13 | SIH26021 | 5.05 | 5.75 | 6.35 | Honey Chain: A block chain-based system for honey traceabi... | Ministry of MSME... | Agriculture, FoodTech & Rural Development |
| 14 | SIH26074 | 5.20 | 5.55 | 6.45 | Downscaling of weather forecast from Block level to Pancha... | Ministry of Earth Sciences (MoES... | Agriculture, FoodTech & Rural Development |
| 15 | SIH26033 | 5.25 | 5.70 | 6.35 | Multiple intermediaries reduce farmers earnings and increa... | Ministry of Consumer Affairs, Fo... | Agriculture, FoodTech & Rural Development |
| 16 | SIH26042 | 5.30 | 5.75 | 6.50 | Al-Powered Vernacular Pedagogy and Real-Time Translation T... | Governmcnt of Jharkhand... | Smart Education |
| 17 | SIH26097 | 5.35 | 5.56 | 6.30 | AI-Driven voice Assistant for livelihood Mapping and NSQF-... | Ministry of Social Justice and E... | Agriculture, FoodTech & Rural Development |
| 18 | SIH26203 | 5.40 | 5.64 | 6.30 | Student Innovation-Creating intelligent devices to improve... | AICTE... | Smart Vehicles |
| 19 | SIH26002 | 5.45 | 5.82 | 6.58 | Al-Based Smart Logistics and Accessibility Intelligence Pl... | Ministry of Development of North... | Transportation & Logistics |
| 20 | SIH26193 | 5.50 | 5.78 | 6.70 | Student Innovation-Developing solutions, keeping in mind t... | AICTE... | Agriculture, FoodTech & Rural Development |

---

## Highest Quality v2 — Best technical merit regardless of crowd

| Rank | PS ID | Quality | WPS | CLS | Title | Org | Theme |
|------|-------|---------|-----|-----|-------|-----|-------|
|  1 | SIH26014 | 7.62 | 6.77 | 5.00 | An lntegrated GIS-based Digital Public lnfrastructure for ... | Ministry of Rural Development... | Agriculture, FoodTech & Rural Development |
|  2 | SIH26012 | 7.48 | 5.57 | 8.20 | AI-Based Automated Urban Parcel Mapping and Cadastral Feat... | Ministry of Rural Development... | Smart Automation |
|  3 | SIH26045 | 7.47 | 7.20 | 3.35 | IP-SAKTI Sahayak a multilingual, RAG-based (source-cited) ... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  4 | SIH26047 | 7.42 | 6.86 | 3.85 | Patient Case-Taking Software... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  5 | SIH26184 | 7.35 | 6.12 | 6.10 | Development of a Predictive Analytics Framework for Cyberc... | Ministry of Home Affairs... | Blockchain & Cybersecurity |
|  6 | SIH26176 | 7.30 | 5.80 | 6.20 | ORCA Marine EcOsystem Reasoning with Collaborative Agents... | Indian Space Research Organisati... | Disaster Management |
|  7 | SIH26019 | 7.25 | 5.75 | 7.40 | National Digital Platform for Research, Policy Innovation,... | Ministry of Rural Development... | Smart Automation |
|  8 | SIH26060 | 7.21 | 5.18 | 8.20 | Digital Platform for efficient remote management of Indian... | Ministry of Earth Sciences (MoES... | Smart Automation |
|  9 | SIH26101 | 7.20 | 6.11 | 5.90 | Develop an AI enabled learning platform that identifies co... | MoSPI... | Smart Education |
| 10 | SIH26018 | 7.18 | 5.65 | 7.70 | Intelligent Land Record Digitization and Validation System... | Ministry of Rural Development... | Smart Automation |
| 11 | SIH26001 | 7.18 | 5.56 | 7.85 | AI-Based early warning and landslide Risk Monitoring Syste... | Ministry of Development of North... | Disaster Management |
| 12 | SIH26017 | 7.13 | 5.91 | 5.85 | Predictive Analytics System for Early Detection of Land Ac... | Ministry of Rural Development... | Smart Automation |
| 13 | SIH26111 | 7.10 | 5.90 | 5.65 | Smart Al-Enabled Rapid Feed and Silage Quality Testing Sys... | Ministry of Fisheries, Animal Hu... | Agriculture, FoodTech & Rural Development |
| 14 | SIH26016 | 7.10 | 5.37 | 7.80 | Real-Time National Land Acquisition & Management System fo... | Ministry of Rural Development... | Smart Automation |
| 15 | SIH26057 | 7.10 | 5.03 | 8.55 | AI-Powered Automated Underwater Marine Debris and Anomaly ... | Ministry of Earth Sciences (MoES... | Disaster Management |

---

## Best PS per theme (v2)

| Theme | Best PS | WPS | Quality | CLS | Title | Org |
|-------|---------|-----|---------|-----|-------|-----|
| MedTech / BioTech / HealthTech | SIH26045 | 7.20 | 7.47 | 3.35 | IP-SAKTI Sahayak a multilingual, RAG-based (source-c... | Ministry of Ayush... |
| Agriculture, FoodTech & Rural Development | SIH26014 | 6.77 | 7.62 | 5.00 | An lntegrated GIS-based Digital Public lnfrastructur... | Ministry of Rural Development... |
| Miscellaneous | SIH26036 | 6.61 | 7.05 | 5.05 | Development of an Online Verification System for Wei... | Ministry of Consumer Affairs, Food &... |
| Clean & Green Technology | SIH26138 | 6.33 | 6.47 | 5.05 | Quantum-Inspired Fuel Consumption Prediction and Gre... | Egreen Quanta... |
| Blockchain & Cybersecurity | SIH26184 | 6.12 | 7.35 | 6.10 | Development of a Predictive Analytics Framework for ... | Ministry of Home Affairs... |
| Smart Education | SIH26101 | 6.11 | 7.20 | 5.90 | Develop an AI enabled learning platform that identif... | MoSPI... |
| Transportation & Logistics | SIH26137 | 6.00 | 6.40 | 6.15 | Quantum-Inspired Intelligent Traffic Route Optimizat... | Egreen Quanta... |
| Smart Vehicles | SIH26168 | 5.96 | 6.75 | 6.05 | AI-ML based Intelligent Dead Reckoning system for se... | Indian Space Research Organisation(I... |
| Smart Automation | SIH26011 | 5.92 | 7.07 | 6.75 | 3D ULPIN Generation and vertical Property Mapping SY... | Ministry of Rural Development... |
| Space Technology | SIH26167 | 5.85 | 6.72 | 5.85 | SatQuery AI - An Interactive Vision-Language Assista... | Indian Space Research Organisation(I... |
| Disaster Management | SIH26176 | 5.80 | 7.30 | 6.20 | ORCA Marine EcOsystem Reasoning with Collaborative A... | Indian Space Research Organisation(I... |
| Toys & Games | SIH26208 | 5.77 | 6.30 | 4.90 | Student Innovation-Challenge your creative mind to c... | AICTE... |
| Heritage & Culture | SIH26197 | 5.54 | 6.30 | 5.80 | Student Innovation-Ideas that showcase the rich cult... | AICTE... |
| Fitness & Sports | SIH26196 | 5.52 | 6.30 | 5.90 | Student Innovation-Ideas that can boost fitness acti... | AICTE... |
| Robotics and Drones | SIH26201 | 5.52 | 6.45 | 6.15 | Student Innovation-There is a need to design drones ... | AICTE... |
| Travel & Tourism | SIH26204 | 5.52 | 6.30 | 5.90 | Student Innovation-A solution/idea that can boost th... | AICTE... |
| Renewable / Sustainable Energy | SIH26200 | 5.39 | 6.30 | 6.40 | Student Innovation-Innovative ideas that help manage... | AICTE... |

---

## Best PS per org (v2, top 20 by WPS)

| Org | Best PS | WPS | Quality | CLS | Title | Theme |
|-----|---------|-----|---------|-----|-------|-------|
| Ministry of Ayush... | SIH26045 | 7.20 | 7.47 | 3.35 | IP-SAKTI Sahayak a multilingual, RAG-based (source... | MedTech / BioTech / HealthTech |
| Ministry of Rural Development... | SIH26014 | 6.77 | 7.62 | 5.00 | An lntegrated GIS-based Digital Public lnfrastruct... | Agriculture, FoodTech & Rural Development |
| Ministry of Consumer Affairs, Food & Public ... | SIH26036 | 6.61 | 7.05 | 5.05 | Development of an Online Verification System for W... | Miscellaneous |
| Egreen Quanta... | SIH26138 | 6.33 | 6.47 | 5.05 | Quantum-Inspired Fuel Consumption Prediction and G... | Clean & Green Technology |
| Ministry of Home Affairs... | SIH26184 | 6.12 | 7.35 | 6.10 | Development of a Predictive Analytics Framework fo... | Blockchain & Cybersecurity |
| MoSPI... | SIH26101 | 6.11 | 7.20 | 5.90 | Develop an AI enabled learning platform that ident... | Smart Education |
| Government Of Maharashtra... | SIH26128 | 6.11 | 6.88 | 4.35 | Efficient systems for early detection,prevention,a... | MedTech / BioTech / HealthTech |
| Ministry of Cooperation... | SIH26089 | 6.04 | 6.88 | 5.05 | Cooperative Gig Services Platform for Household & ... | Agriculture, FoodTech & Rural Development |
| MathWorks... | SIH26038 | 6.00 | 6.88 | 6.10 | Explainable AI for Diabetic Retinopathy Screening ... | MedTech / BioTech / HealthTech |
| Indian Space Research Organisation(ISRO)... | SIH26168 | 5.96 | 6.75 | 6.05 | AI-ML based Intelligent Dead Reckoning system for ... | Smart Vehicles |
| Ministry of Fisheries, Animal Husbandry & Da... | SIH26111 | 5.90 | 7.10 | 5.65 | Smart Al-Enabled Rapid Feed and Silage Quality Tes... | Agriculture, FoodTech & Rural Development |
| Ministry of Development of North Eastern Reg... | SIH26003 | 5.85 | 6.88 | 5.80 | AI-Based Cognitive Gaming and Memory Assistance Pl... | MedTech / BioTech / HealthTech |
| Ministry of defence (MoD)... | SIH26227 | 5.85 | 6.48 | 5.65 | Semantic Retrieval and Multi-Temporal Change Analy... | Space Technology |
| Governmcnt of Jharkhand... | SIH26041 | 5.81 | 6.53 | 5.60 | AR-Based Vocational Training Simulator for Industr... | Smart Education |
| AICTE... | SIH26193 | 5.78 | 6.70 | 5.50 | Student Innovation-Developing solutions, keeping i... | Agriculture, FoodTech & Rural Development |
| Ministry of MSME... | SIH26021 | 5.75 | 6.35 | 5.05 | Honey Chain: A block chain-based system for honey ... | Agriculture, FoodTech & Rural Development |
| Ministry of Mines (MoM)... | SIH26229 | 5.71 | 6.63 | 5.95 | Kabadiwala Connect – Bringing the Informal Collect... | Clean & Green Technology |
| Ministry of Social Justice and Empowerment (... | SIH26094 | 5.69 | 6.98 | 5.60 | AI-Powered Dynamic Mental Health Monitoring and Di... | MedTech / BioTech / HealthTech |
| Ministry of Steel... | SIH26006 | 5.61 | 6.63 | 6.35 | Development of an Intelligent Freight Forecasting ... | Transportation & Logistics |
| Ministry of Earth Sciences (MoES)... | SIH26074 | 5.55 | 6.45 | 5.20 | Downscaling of weather forecast from Block level t... | Agriculture, FoodTech & Rural Development |

---

## Strategic Recommendations v2 — For Shreyash's team

### 🎯 PRIMARY (lock at SIH portal TODAY)
**SIH26045 — IP-SAKTI Sahayak** (Ayush) · **WPS 7.20** (+0.46 vs v1) · **CLS 3.35** (hidden gem, ~167/500) · Q 7.47
- **Why v2 #1**: Only PS with innov 9.0 + mfit 8.5 + CLS 3.35. Niche treaty stack (GRATK 2024 / Nagoya / TKDL / Bhashini / WIPO+TRIPS) → suppressed AI hype = few teams can copy. Dataset 7.0 via TKDL/patent APIs. `ideas 0/500` in raw = still empty.
- **Differentiators to lock** (hit STRONG PICK 7.5): citation-or-abstain (every answer cites §), jurisdiction toggle India↔International, Bhashini multilingual, Neo4j knowledge graph for 7 Acts. Add 1 diagram: “Why generic RAG fails on Ayush IP” vs 3 baselines.
- **Submit**: **19 Sep safe** (CLS 3.35), but lock **by 16 Sep** anyway — internal hackathon needs prototype.
- **Risk**: Legal-domain learning curve (team_fit 6.5) — assign 1 member to read BD Act 2023 + WIPO GRATK 2024 this week.

### 🥈 SECONDARY (same ministry, if SIH26045 blocked by SPOC)

**SIH26047 — Patient Case-Taking Software** (Ayush) · **WPS 6.86** (+0.37) · CLS 3.85 · Q 7.42
- Workflow automation, offline-first mobile, NAMASTE/ICD-11 codes. Shares Ayush mentor, lower legal risk than SAKTI.
- Differentiator: structured FHIR-like Ayush record + drug formulary autocomplete + voice input via Bhashini.

### 🥉 TERTIARY (land-stack track — high Quality 7.62)

**SIH26014 — Integrated GIS Land Stack** (Rural Development) · **WPS 6.77** (+0.57) · CLS 5.00 · Q 7.62 (highest Q in top 5)
- Parcel-level GIS, ULPIN, RoR, open APIs, role-based access. MoRD has 9 PS (medium diffuse) but this one matches SVAMITVA/NAKSHA programme → mfit 8.0.
- Needs geospatial chops (QGIS, PostGIS). Demo: live parcel search + ownership verification + transaction tracker.

### Alternative #4 (if team wants portal track with quick demo)

**SIH26036 — Online Verification for Weighing/Measuring Instruments** (Consumer Affairs) · **WPS 6.61** (−0.37) → still WORKABLE
- Clear regulatory mandate (Legal Metrology), stakeholder directory dataset. Demo: scanner + verification portal + admin. Lower innov (6.5) but highest feas (7.5).

### Wildcard (quantum novelty, private org judge magnet)

**SIH26138 — Quantum-Inspired Fuel & Fleet Optimization** (Egreen Quanta) · **WPS 6.33** (+0.09) · CLS 5.05
- Private org = tech-focused judges, less bureaucratic. Needs telematics data story.

---

## Verdict changes — watch list

| PS | v1 → v2 | WPS | Action |
|----|---------|-----|--------|
| **SIH26046** | HIGH RISK → **WORKABLE** | 5.64 → 6.50 | **PROMOTED** — Ayush clinical trials dashboard, dataset_link, CLS 3.55 intact. Consider as 2nd backup. |
| **SIH26015** | HIGH RISK → **WORKABLE** | 5.70 → 6.00 | Promoted (geospatial, feasible) |
| **SIH26038** | HIGH RISK → **WORKABLE** | 5.74 → 6.00 | Promoted (MathWorks diabetic retinopathy, dataset 8.0) |
| **SIH26101** | HIGH RISK → **WORKABLE** | 5.54 → 6.11 | Promoted (MoSPI learning platform, high innov 8.0) |
| **SIH26128** | HIGH RISK → **WORKABLE** | 5.57 → 6.11 | Promoted (Maharashtra early detection) |
| **SIH26006** | WORKABLE → HIGH RISK | 6.03 → 5.61 | **DEMOTED** — feas/impact rebased, freight forecasting is harder than v1 templated |
| **SIH26011** | WORKABLE → HIGH RISK | 6.17 → 5.92 | Demoted (3D ULPIN needs Lidar/photogrammetry, feas 6.0 not 5.0) |
| **SIH26041** | WORKABLE → HIGH RISK | 6.39 → 5.81 | Demoted (AR vocational needs hardware) |
| **SIH26042** | WORKABLE → HIGH RISK | 6.37 → 5.75 | Demoted (vernacular pedagogy innov rebased 6.5) |
| **SIH26084 / SIH26167** | WORKABLE → HIGH RISK | 6.04→5.22 / 6.03→5.85 | MoES/ISRO disaster/space nowcasting deflated on dataset + diff |

---

## Timeline (unchanged)

| Date | Milestone | v2 action |
|------|-----------|-----------|
| **6 Sep 2026** | Team registration deadline | **Lock SIH26045 as primary, SIH26047 backup** on `sih.gov.in`; confirm ≥1 female, 6 members |
| **9–15 Sep** | Internal hackathons (BMS-style 10-factor rubric) | Ship MVP: RAG pipeline + 7-acts Neo4j + Bhashini + citation UI. Demo = 90s single-page. |
| **Sep–Oct** | National shortlisting (6-slide IDEA PPT) | Slide 2 = twist diagram vs 3 existing Ayush IP tools; Slide 4 = CLS moat (niche treaty = moat) |
| **Dec** | Grand Finale | Scale to jurisdiction toggle + TKDL sync |

Next 7 days: Day 1–2 read BD Act/WIPO/TKDL; Day 3 scaffold Qdrant+Neo4j; Day 4–5 Bhashini STT/TTS; Day 6 citation tests + safety abstention.

---

## Files

| Artifact | Path |
|----------|------|
| Raw 175 Software PS (canonical) | `projects/sih26/research/ps-evaluation/all-175-software-raw.json` · `reference/sih26/all-175-software-raw.json` |
| v2 evaluated JSON (sorted by WPS) | `projects/sih26/research/ps-evaluation/all-175-evaluated-v2.json` · `reference/sih26/all-175-evaluated-v2.json` |
| v2 CSV (Excel-ready) | `projects/sih26/research/ps-evaluation/all-175-evaluated-v2.csv` · `reference/sih26/all-175-evaluated-v2.csv` |
| v1 JSON/MD (preserved) | `all-175-evaluated.json` · `04-complete-ps-ranking.md` |
| Engine | `/tmp/eval_v2.py` (216 lines, no deps) |
| Skill mirror | `ps-evaluator` v Sep 2026 |

*All scores are raw-data-derived, deterministic, and auditable per PS `description` text — no LLM guesswork. Tweak `/tmp/eval_v2.py` weights and re-run to test sensitivity.*
