# SIH 2026 — Complete Software PS Evaluation v3 (All 175 PS) — Internal 5 Sep Freeze-Adjusted

**Generated**: 2026-09-03 · **Version**: v3 (internal hackathon 5 Sep) · **Previous**: v2 (`05-complete-ps-ranking-v2.md`, CLS weight 0.25) · **Base**: same raw-text v2 scores (175 Software from 229 total)
**Source**: `vedantchalke36/sih-2026-problem-statements` · `all-175-software-raw.json` (0/500 pre-freeze snapshot 21 Aug)
**Why v3**: College internal is **5 Sept** → 500-idea portal freeze (hits ~17-20 Sept) is **irrelevant for internal selection**. v2 penalized high-CLS PS 15% too harshly for this timeline. v3 re-weights to judge execution over crowd avoidance *for internal*, while keeping national freeze note.

---

## TL;DR v3 for IPS Academy (internal 5 Sep)

| Priority | PS ID | WPS v3 | Δ v2→v3 | Q | CLS | Verdict v3 | Title — Org |
|----------|-------|--------|---------|---|-----|------------|-------------|
| **#1** | **SIH26045** | **7.33** | +0.13 | 7.47 | 3.35 | WORKABLE | IP-SAKTI Sahayak a multilingual, RAG-based (source-cited) AI a... — Ministry of Ayush |
| **#2** | **SIH26014** | **7.14** | +0.37 | 7.62 | 5.00 | WORKABLE | An lntegrated GIS-based Digital Public lnfrastructure for Land... — Ministry of Rural Development |
| **#3** | **SIH26047** | **7.03** | +0.17 | 7.42 | 3.85 | WORKABLE | Patient Case-Taking Software... — Ministry of Ayush |
| **#4** | **SIH26036** | **6.92** | +0.31 | 7.05 | 5.05 | WORKABLE | Development of an Online Verification System for Weighing and ... — Ministry of Consumer Affairs,  |
| **#5** | **SIH26184** | **6.62** | +0.50 | 7.35 | 6.10 | WORKABLE | Development of a Predictive Analytics Framework for Cybercrime... — Ministry of Home Affairs |
| **#6** | **SIH26138** | **6.58** | +0.25 | 6.47 | 5.05 | WORKABLE | Quantum-Inspired Fuel Consumption Prediction and Green Fleet O... — Egreen Quanta |

**Change**: v3 avg WPS 5.78 vs v2 5.33 (++0.45). **WORKABLE count 13 → 37** (+24). If SPOC blocks #1, chain is `SIH26045 → SIH26014 → SIH26047 → SIH26036` (note SIH26014 jumps to #2 on quality).

---

## What changed: v2 → v3 weighting (only WPS formula, scores unchanged)

```
v2 (general/national): WPS = Q×0.40 + (10-CLS)×0.25 + Diff×0.15 + Dataset×0.10 + Demo×0.05 + MFit×0.05
v3 (internal 5 Sep)  : WPS = Q×0.50 + (10-CLS)×0.10 + Diff×0.20 + Dataset×0.10 + Demo×0.05 + MFit×0.05
                         ▲+0.10 Quality      ▼-0.15 CLS       ▲+0.05 Differentiation
Rationale: Internal judges score prototype + innovation (Quality+Diff), not portal popularity. CLS still matters 10% for SPOC advice + national backup choice, but not 25% when internal is 12 days before freeze.
Reproducible: `python3 /tmp/eval_v2.py && python3 <<'PY' # recompute wps_v3 as above`
```

**Ranges unchanged** (scores derived identically): Quality 5.68–7.62 avg 6.51 · CLS 3.35–8.80 avg 7.01  
**WPS ranges**: v2 4.46–7.20 → **v3 5.06–7.33** · verdicts WORKABLE 13 → 37 (37 PS now viable for internal pitch).

---

## Top 25 v3 (freeze-adjusted for 5 Sep internal)

| Rank | PS ID | WPS v3 | Δ | Q | CLS | Verdict v3 | Title | Org | Theme |
|------|-------|--------|---|---|-----|------------|-------|-----|-------|
|  1 | SIH26045 | 7.33 | +0.13 | 7.47 | 3.35 | WORKABLE | IP-SAKTI Sahayak a multilingual, RAG-based (source-cited... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  2 | SIH26014 | 7.14 | +0.37 | 7.62 | 5.00 | WORKABLE | An lntegrated GIS-based Digital Public lnfrastructure fo... | Ministry of Rural Development... | Agriculture, FoodTech & Rural Development |
|  3 | SIH26047 | 7.03 | +0.17 | 7.42 | 3.85 | WORKABLE | Patient Case-Taking Software... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
|  4 | SIH26036 | 6.92 | +0.31 | 7.05 | 5.05 | WORKABLE | Development of an Online Verification System for Weighin... | Ministry of Consumer Affairs, ... | Miscellaneous |
|  5 | SIH26184 | 6.62 | +0.50 | 7.35 | 6.10 | WORKABLE | Development of a Predictive Analytics Framework for Cybe... | Ministry of Home Affairs... | Blockchain & Cybersecurity |
|  6 | SIH26138 | 6.58 | +0.25 | 6.47 | 5.05 | WORKABLE | Quantum-Inspired Fuel Consumption Prediction and Green F... | Egreen Quanta... | Clean & Green Technology |
|  7 | SIH26011 | 6.49 | +0.57 | 7.07 | 6.75 | WORKABLE | 3D ULPIN Generation and vertical Property Mapping SYstem... | Ministry of Rural Development... | Smart Automation |
|  8 | SIH26101 | 6.46 | +0.35 | 7.20 | 5.90 | WORKABLE | Develop an AI enabled learning platform that identifies ... | MoSPI... | Smart Education |
|  9 | SIH26046 | 6.45 | -0.05 | 6.60 | 3.55 | WORKABLE | AIIA Clinical Trials Dashboard - a real-time, cloud-base... | Ministry of Ayush... | MedTech / BioTech / HealthTech |
| 10 | SIH26137 | 6.41 | +0.41 | 6.40 | 6.15 | WORKABLE | Quantum-Inspired Intelligent Traffic Route Optimization ... | Egreen Quanta... | Transportation & Logistics |
| 11 | SIH26019 | 6.36 | +0.61 | 7.25 | 7.40 | WORKABLE | National Digital Platform for Research, Policy Innovatio... | Ministry of Rural Development... | Smart Automation |
| 12 | SIH26038 | 6.35 | +0.35 | 6.88 | 6.10 | WORKABLE | Explainable AI for Diabetic Retinopathy Screening in Rur... | MathWorks... | MedTech / BioTech / HealthTech |
| 13 | SIH26168 | 6.32 | +0.36 | 6.75 | 6.05 | WORKABLE | AI-ML based Intelligent Dead Reckoning system for seamle... | Indian Space Research Organisa... | Smart Vehicles |
| 14 | SIH26018 | 6.29 | +0.64 | 7.18 | 7.70 | WORKABLE | Intelligent Land Record Digitization and Validation Syst... | Ministry of Rural Development... | Smart Automation |
| 15 | SIH26012 | 6.29 | +0.72 | 7.48 | 8.20 | WORKABLE | AI-Based Automated Urban Parcel Mapping and Cadastral Fe... | Ministry of Rural Development... | Smart Automation |
| 16 | SIH26017 | 6.26 | +0.35 | 7.13 | 5.85 | WORKABLE | Predictive Analytics System for Early Detection of Land ... | Ministry of Rural Development... | Smart Automation |
| 17 | SIH26089 | 6.24 | +0.20 | 6.88 | 5.05 | WORKABLE | Cooperative Gig Services Platform for Household & Commun... | Ministry of Cooperation... | Agriculture, FoodTech & Rural Development |
| 18 | SIH26128 | 6.21 | +0.10 | 6.88 | 4.35 | WORKABLE | Efficient systems for early detection,prevention,and man... | Government Of Maharashtra... | MedTech / BioTech / HealthTech |
| 19 | SIH26111 | 6.21 | +0.31 | 7.10 | 5.65 | WORKABLE | Smart Al-Enabled Rapid Feed and Silage Quality Testing S... | Ministry of Fisheries, Animal ... | Agriculture, FoodTech & Rural Development |
| 20 | SIH26176 | 6.21 | +0.41 | 7.30 | 6.20 | WORKABLE | ORCA Marine EcOsystem Reasoning with Collaborative Agent... | Indian Space Research Organisa... | Disaster Management |
| 21 | SIH26001 | 6.20 | +0.64 | 7.18 | 7.85 | WORKABLE | AI-Based early warning and landslide Risk Monitoring Sys... | Ministry of Development of Nor... | Disaster Management |
| 22 | SIH26141 | 6.18 | +0.49 | 6.10 | 6.90 | WORKABLE | Quantum-Inspired Cyber Threat Detection for Digital Sign... | Egreen Quanta... | Blockchain & Cybersecurity |
| 23 | SIH26015 | 6.17 | +0.17 | 6.75 | 5.00 | WORKABLE | Application of Geospatial Techniques for visualization a... | Ministry of Rural Development... | Agriculture, FoodTech & Rural Development |
| 24 | SIH26167 | 6.17 | +0.32 | 6.72 | 5.85 | WORKABLE | SatQuery AI - An Interactive Vision-Language Assistant f... | Indian Space Research Organisa... | Space Technology |
| 25 | SIH26035 | 6.17 | +0.55 | 6.85 | 7.50 | WORKABLE | Development of a Software Program/Application for Genera... | Ministry of Consumer Affairs, ... | Miscellaneous |

---

## Complete Ranked List v3 — All 175 (freeze-adjusted)

| Rank | PS ID | WPS v3 | Δ v2→v3 | Q | CLS | Verdict v3 | Title | Org | Theme | Innov | Feas | Diff | Data | MFit | Demo |
|------|-------|--------|---------|---|-----|------------|-------|-----|-------|-------|------|------|------|------|------|
|   1 | SIH26045 | 7.33 | +0.13 | 7.47 | 3.35 | WORKABLE | IP-SAKTI Sahayak a multilingual, RAG-based (... | Ministry of Ayush... | MedTech / BioTech / ... | 9.0 | 7.5 | 7.5 | 7.0 | 8.5 | 6.0 |
|   2 | SIH26014 | 7.14 | +0.37 | 7.62 | 5.00 | WORKABLE | An lntegrated GIS-based Digital Public lnfra... | Ministry of Rural Developm... | Agriculture, FoodTec... | 9.0 | 6.0 | 7.0 | 6.5 | 8.0 | 7.5 |
|   3 | SIH26047 | 7.03 | +0.17 | 7.42 | 3.85 | WORKABLE | Patient Case-Taking Software... | Ministry of Ayush... | MedTech / BioTech / ... | 9.0 | 6.0 | 7.0 | 5.0 | 8.5 | 7.5 |
|   4 | SIH26036 | 6.92 | +0.31 | 7.05 | 5.05 | WORKABLE | Development of an Online Verification System... | Ministry of Consumer Affai... | Miscellaneous... | 6.5 | 7.5 | 7.0 | 7.0 | 8.5 | 7.5 |
|   5 | SIH26184 | 6.62 | +0.50 | 7.35 | 6.10 | WORKABLE | Development of a Predictive Analytics Framew... | Ministry of Home Affairs... | Blockchain & Cyberse... | 6.5 | 7.5 | 7.0 | 5.0 | 5.5 | 7.5 |
|   6 | SIH26138 | 6.58 | +0.25 | 6.47 | 5.05 | WORKABLE | Quantum-Inspired Fuel Consumption Prediction... | Egreen Quanta... | Clean & Green Techno... | 7.5 | 6.0 | 7.0 | 7.0 | 7.5 | 7.5 |
|   7 | SIH26011 | 6.49 | +0.57 | 7.07 | 6.75 | WORKABLE | 3D ULPIN Generation and vertical Property Ma... | Ministry of Rural Developm... | Smart Automation... | 9.0 | 7.0 | 7.0 | 6.0 | 8.0 | 4.5 |
|   8 | SIH26101 | 6.46 | +0.35 | 7.20 | 5.90 | WORKABLE | Develop an AI enabled learning platform that... | MoSPI... | Smart Education... | 8.0 | 6.5 | 5.0 | 7.0 | 7.5 | 7.5 |
|   9 | SIH26046 | 6.45 | -0.05 | 6.60 | 3.55 | WORKABLE | AIIA Clinical Trials Dashboard - a real-time... | Ministry of Ayush... | MedTech / BioTech / ... | 5.5 | 6.5 | 5.0 | 7.0 | 8.5 | 7.5 |
|  10 | SIH26137 | 6.41 | +0.41 | 6.40 | 6.15 | WORKABLE | Quantum-Inspired Intelligent Traffic Route O... | Egreen Quanta... | Transportation & Log... | 7.5 | 6.0 | 7.0 | 7.0 | 7.5 | 7.0 |
|  11 | SIH26019 | 6.36 | +0.61 | 7.25 | 7.40 | WORKABLE | National Digital Platform for Research, Poli... | Ministry of Rural Developm... | Smart Automation... | 6.5 | 7.5 | 5.5 | 6.0 | 8.0 | 7.5 |
|  12 | SIH26038 | 6.35 | +0.35 | 6.88 | 6.10 | WORKABLE | Explainable AI for Diabetic Retinopathy Scre... | MathWorks... | MedTech / BioTech / ... | 6.5 | 7.5 | 5.0 | 8.0 | 8.5 | 6.0 |
|  13 | SIH26168 | 6.32 | +0.36 | 6.75 | 6.05 | WORKABLE | AI-ML based Intelligent Dead Reckoning syste... | Indian Space Research Orga... | Smart Vehicles... | 6.5 | 7.5 | 5.5 | 8.0 | 5.5 | 7.5 |
|  14 | SIH26018 | 6.29 | +0.64 | 7.18 | 7.70 | WORKABLE | Intelligent Land Record Digitization and Val... | Ministry of Rural Developm... | Smart Automation... | 8.0 | 6.0 | 5.5 | 6.0 | 8.0 | 7.5 |
|  15 | SIH26012 | 6.29 | +0.72 | 7.48 | 8.20 | WORKABLE | AI-Based Automated Urban Parcel Mapping and ... | Ministry of Rural Developm... | Smart Automation... | 8.0 | 7.0 | 5.0 | 6.0 | 8.0 | 7.5 |
|  16 | SIH26017 | 6.26 | +0.35 | 7.13 | 5.85 | WORKABLE | Predictive Analytics System for Early Detect... | Ministry of Rural Developm... | Smart Automation... | 6.5 | 7.0 | 5.0 | 5.0 | 8.0 | 7.5 |
|  17 | SIH26089 | 6.24 | +0.20 | 6.88 | 5.05 | WORKABLE | Cooperative Gig Services Platform for Househ... | Ministry of Cooperation... | Agriculture, FoodTec... | 6.5 | 7.0 | 5.0 | 5.0 | 8.5 | 7.5 |
|  18 | SIH26128 | 6.21 | +0.10 | 6.88 | 4.35 | WORKABLE | Efficient systems for early detection,preven... | Government Of Maharashtra... | MedTech / BioTech / ... | 6.5 | 7.0 | 5.0 | 5.0 | 6.5 | 7.5 |
|  19 | SIH26111 | 6.21 | +0.31 | 7.10 | 5.65 | WORKABLE | Smart Al-Enabled Rapid Feed and Silage Quali... | Ministry of Fisheries, Ani... | Agriculture, FoodTec... | 8.0 | 7.0 | 5.0 | 5.0 | 8.5 | 6.0 |
|  20 | SIH26176 | 6.21 | +0.41 | 7.30 | 6.20 | WORKABLE | ORCA Marine EcOsystem Reasoning with Collabo... | Indian Space Research Orga... | Disaster Management... | 8.0 | 7.0 | 5.0 | 6.0 | 5.5 | 6.0 |
|  21 | SIH26001 | 6.20 | +0.64 | 7.18 | 7.85 | WORKABLE | AI-Based early warning and landslide Risk Mo... | Ministry of Development of... | Disaster Management... | 8.0 | 6.0 | 5.0 | 6.0 | 8.5 | 7.5 |
|  22 | SIH26141 | 6.18 | +0.49 | 6.10 | 6.90 | WORKABLE | Quantum-Inspired Cyber Threat Detection for ... | Egreen Quanta... | Blockchain & Cyberse... | 6.5 | 6.0 | 7.0 | 7.0 | 7.5 | 7.0 |
|  23 | SIH26015 | 6.17 | +0.17 | 6.75 | 5.00 | WORKABLE | Application of Geospatial Techniques for vis... | Ministry of Rural Developm... | Agriculture, FoodTec... | 6.5 | 7.0 | 5.0 | 6.0 | 8.0 | 6.0 |
|  24 | SIH26167 | 6.17 | +0.32 | 6.72 | 5.85 | WORKABLE | SatQuery AI - An Interactive Vision-Language... | Indian Space Research Orga... | Space Technology... | 8.0 | 7.0 | 5.5 | 7.0 | 7.5 | 4.5 |
|  25 | SIH26035 | 6.17 | +0.55 | 6.85 | 7.50 | WORKABLE | Development of a Software Program/Applicatio... | Ministry of Consumer Affai... | Miscellaneous... | 5.5 | 7.5 | 5.0 | 7.0 | 8.5 | 7.5 |
|  26 | SIH26003 | 6.16 | +0.31 | 6.88 | 5.80 | WORKABLE | AI-Based Cognitive Gaming and Memory Assista... | Ministry of Development of... | MedTech / BioTech / ... | 6.5 | 7.0 | 5.0 | 5.0 | 8.5 | 7.5 |
|  27 | SIH26186 | 6.11 | +0.47 | 6.90 | 6.90 | WORKABLE | AI-Based Predictive Personnel Stress and Wel... | Ministry of Home Affairs... | MedTech / BioTech / ... | 5.0 | 7.5 | 5.0 | 7.0 | 5.5 | 7.5 |
|  28 | SIH26227 | 6.10 | +0.25 | 6.48 | 5.65 | WORKABLE | Semantic Retrieval and Multi-Temporal Change... | Ministry of defence (MoD)... | Space Technology... | 6.5 | 7.5 | 5.0 | 7.0 | 8.5 | 6.0 |
|  29 | SIH26119 | 6.08 | +0.55 | 6.58 | 7.40 | WORKABLE | Indigenous GPU-Accelerated Optimization Solv... | Mangalore Refinery and Pet... | Smart Automation... | 6.5 | 7.5 | 5.5 | 7.0 | 8.5 | 6.0 |
|  30 | SIH26041 | 6.05 | +0.24 | 6.53 | 5.60 | WORKABLE | AR-Based Vocational Training Simulator for I... | Governmcnt of Jharkhand... | Smart Education... | 5.5 | 7.0 | 5.0 | 5.5 | 8.5 | 7.5 |
|  31 | SIH26002 | 6.04 | +0.22 | 6.58 | 5.45 | WORKABLE | Al-Based Smart Logistics and Accessibility I... | Ministry of Development of... | Transportation & Log... | 6.5 | 7.0 | 5.0 | 5.0 | 8.5 | 7.5 |
|  32 | SIH26193 | 6.03 | +0.25 | 6.70 | 5.50 | WORKABLE | Student Innovation-Developing solutions, kee... | AICTE... | Agriculture, FoodTec... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  33 | SIH26229 | 6.02 | +0.31 | 6.63 | 5.95 | WORKABLE | Kabadiwala Connect – Bringing the Informal C... | Ministry of Mines (MoM)... | Clean & Green Techno... | 6.5 | 7.0 | 5.0 | 5.0 | 8.5 | 7.5 |
|  34 | SIH26198 | 6.01 | +0.27 | 6.70 | 5.65 | WORKABLE | Student Innovation-Cutting-edge technology i... | AICTE... | MedTech / BioTech / ... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  35 | SIH26133 | 6.01 | +0.38 | 6.88 | 6.30 | WORKABLE | Accessibility and quality of public healthca... | Government Of Maharashtra... | MedTech / BioTech / ... | 6.5 | 7.0 | 5.0 | 5.0 | 6.5 | 7.5 |
|  36 | SIH26139 | 6.00 | +0.38 | 6.55 | 6.50 | WORKABLE | Hybrid Quantum Machine Learning Platform for... | Egreen Quanta... | MedTech / BioTech / ... | 7.5 | 6.0 | 5.0 | 7.0 | 7.5 | 6.0 |
|  37 | SIH26115 | 6.00 | +0.47 | 6.58 | 6.90 | WORKABLE | Design and Develop a Smart Mobile Medical-Wa... | Autodesk... | MedTech / BioTech / ... | 5.5 | 7.0 | 5.5 | 5.0 | 8.5 | 7.5 |
|  38 | SIH26032 | 5.99 | +0.48 | 6.58 | 7.00 | HIGH RISK | Farmers often face long waiting times, lack ... | Ministry of Consumer Affai... | Smart Automation... | 5.5 | 7.0 | 5.5 | 5.0 | 8.5 | 7.5 |
|  39 | SIH26006 | 5.98 | +0.37 | 6.63 | 6.35 | HIGH RISK | Development of an Intelligent Freight Foreca... | Ministry of Steel... | Transportation & Log... | 6.5 | 7.0 | 5.0 | 5.0 | 8.5 | 7.5 |
|  40 | SIH26162 | 5.98 | +0.54 | 6.98 | 7.30 | HIGH RISK | AI-Based Detection and Classification of Ind... | National Technical Researc... | Disaster Management... | 6.5 | 7.5 | 5.0 | 7.0 | 4.5 | 6.0 |
|  41 | SIH26078 | 5.98 | +0.73 | 7.03 | 8.35 | HIGH RISK | AI-Driven Spatio-Temporal Tracking of Extrem... | Ministry of Earth Sciences... | Smart Automation... | 6.5 | 7.0 | 5.5 | 6.0 | 4.5 | 7.5 |
|  42 | SIH26131 | 5.97 | +0.14 | 6.65 | 4.80 | HIGH RISK | Early detection and management of crop disea... | Government Of Maharashtra... | Agriculture, FoodTec... | 6.5 | 7.0 | 5.0 | 5.0 | 6.5 | 6.0 |
|  43 | SIH26140 | 5.97 | +0.37 | 6.50 | 6.50 | HIGH RISK | AI-Based Interactive Quantum Algorithm Learn... | Egreen Quanta... | Smart Education... | 7.5 | 6.0 | 5.0 | 7.0 | 7.5 | 6.0 |
|  44 | SIH26207 | 5.96 | +0.26 | 6.60 | 5.65 | HIGH RISK | Student Innovation-Smart education,a concept... | AICTE... | Smart Education... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  45 | SIH26103 | 5.96 | +0.57 | 6.98 | 7.80 | HIGH RISK | Use case on web-based integrated project-mon... | MoSPI... | Smart Automation... | 6.5 | 8.0 | 4.0 | 7.0 | 7.5 | 7.5 |
|  46 | SIH26099 | 5.96 | +0.67 | 6.60 | 8.40 | HIGH RISK | AI-Driven Standardization and Harmonization ... | Ministry of Petroleum & Na... | Smart Automation... | 6.5 | 6.5 | 5.0 | 7.0 | 8.5 | 7.5 |
|  47 | SIH26042 | 5.95 | +0.20 | 6.50 | 5.30 | HIGH RISK | Al-Powered Vernacular Pedagogy and Real-Time... | Governmcnt of Jharkhand... | Smart Education... | 6.5 | 7.0 | 5.0 | 5.0 | 8.5 | 6.0 |
|  48 | SIH26043 | 5.95 | +0.31 | 6.48 | 5.90 | HIGH RISK | A digital platform to crowdsource societal c... | Governmcnt of Jharkhand... | Smart Education... | 5.0 | 7.0 | 5.5 | 4.0 | 8.5 | 7.5 |
|  49 | SIH26016 | 5.95 | +0.58 | 7.10 | 7.80 | HIGH RISK | Real-Time National Land Acquisition & Manage... | Ministry of Rural Developm... | Smart Automation... | 6.5 | 6.5 | 4.0 | 6.0 | 8.0 | 7.5 |
|  50 | SIH26174 | 5.94 | +0.34 | 6.38 | 6.30 | HIGH RISK | AI Human Activity Recognition for On-board B... | Indian Space Research Orga... | Space Technology... | 5.5 | 7.5 | 5.0 | 7.0 | 7.5 | 6.0 |
|  51 | SIH26206 | 5.94 | +0.47 | 6.80 | 6.90 | HIGH RISK | Student Innovation-Disaster management inclu... | AICTE... | Disaster Management... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  52 | SIH26028 | 5.94 | +0.59 | 6.63 | 7.70 | HIGH RISK | Dynamic Forecast of Expected Time of Arrival... | Ministry of Railways... | Smart Automation... | 6.5 | 7.0 | 5.5 | 5.0 | 8.5 | 7.5 |
|  53 | SIH26084 | 5.94 | +0.72 | 7.03 | 8.45 | HIGH RISK | Convective scale nowcasting for Thunderstorm... | Ministry of Earth Sciences... | Disaster Management... | 6.5 | 7.0 | 5.0 | 5.5 | 7.0 | 7.5 |
|  54 | SIH26094 | 5.93 | +0.24 | 6.98 | 5.60 | HIGH RISK | AI-Powered Dynamic Mental Health Monitoring ... | Ministry of Social Justice... | MedTech / BioTech / ... | 6.5 | 7.0 | 4.0 | 5.0 | 6.5 | 7.5 |
|  55 | SIH26093 | 5.92 | +0.25 | 6.98 | 5.70 | HIGH RISK | AI-Based Real-Time Stress and Trauma Assessm... | Ministry of Social Justice... | MedTech / BioTech / ... | 6.5 | 7.0 | 4.0 | 5.0 | 6.5 | 7.5 |
|  56 | SIH26175 | 5.92 | +0.47 | 6.50 | 7.10 | HIGH RISK | DepthWizard - Single-View Height Estimation ... | Indian Space Research Orga... | Disaster Management... | 6.5 | 7.0 | 5.0 | 8.0 | 5.5 | 6.0 |
|  57 | SIH26158 | 5.91 | +0.50 | 6.81 | 7.15 | HIGH RISK | Single-Pass Drone Video to Accurate 3D Model... | National Technical Researc... | Robotics and Drones... | 7.3 | 7.5 | 5.0 | 7.0 | 4.5 | 6.0 |
|  58 | SIH26102 | 5.90 | +0.57 | 6.45 | 7.80 | HIGH RISK | Development of an AI-powered system to detec... | MoSPI... | Smart Automation... | 5.5 | 7.5 | 5.0 | 7.0 | 7.5 | 7.5 |
|  59 | SIH26021 | 5.89 | +0.14 | 6.35 | 5.05 | HIGH RISK | Honey Chain: A block chain-based system for ... | Ministry of MSME... | Agriculture, FoodTec... | 5.5 | 7.0 | 5.0 | 5.0 | 8.5 | 6.0 |
|  60 | SIH26195 | 5.88 | +0.11 | 6.30 | 4.90 | HIGH RISK | Student Innovation-Solutions could be in the... | AICTE... | Clean & Green Techno... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  61 | SIH26208 | 5.88 | +0.11 | 6.30 | 4.90 | HIGH RISK | Student Innovation-Challenge your creative m... | AICTE... | Toys & Games... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  62 | SIH26033 | 5.88 | +0.18 | 6.35 | 5.25 | HIGH RISK | Multiple intermediaries reduce farmers earni... | Ministry of Consumer Affai... | Agriculture, FoodTec... | 5.5 | 7.0 | 5.0 | 5.0 | 8.5 | 6.0 |
|  63 | SIH26205 | 5.88 | +0.24 | 6.45 | 5.65 | HIGH RISK | Student Innovation-Submit your ideas to addr... | AICTE... | Transportation & Log... | 5.5 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  64 | SIH26013 | 5.88 | +0.42 | 6.50 | 6.75 | HIGH RISK | Automated lntegration and lntelligent Harmon... | Ministry of Rural Developm... | Smart Automation... | 6.5 | 6.0 | 5.0 | 6.0 | 8.0 | 6.0 |
|  65 | SIH26060 | 5.88 | +0.70 | 7.21 | 8.20 | HIGH RISK | Digital Platform for efficient remote manage... | Ministry of Earth Sciences... | Smart Automation... | 7.3 | 7.0 | 5.0 | 5.0 | 4.5 | 7.5 |
|  66 | SIH26037 | 5.87 | +0.29 | 6.05 | 6.05 | HIGH RISK | Adaptive Path Planning and Collision Avoidan... | MathWorks... | Smart Vehicles... | 6.5 | 7.5 | 5.5 | 7.0 | 8.5 | 4.5 |
|  67 | SIH26031 | 5.87 | +0.52 | 6.62 | 7.40 | HIGH RISK | Quality assessment and grading of onions are... | Ministry of Consumer Affai... | Smart Automation... | 5.5 | 7.0 | 5.0 | 5.0 | 8.5 | 7.5 |
|  68 | SIH26082 | 5.86 | +0.41 | 6.73 | 6.55 | HIGH RISK | Air Pollution–Weather Coupled Forecasting Sy... | Ministry of Earth Sciences... | Clean & Green Techno... | 5.5 | 7.0 | 5.0 | 5.5 | 4.5 | 7.5 |
|  69 | SIH26077 | 5.86 | +0.60 | 6.80 | 7.85 | HIGH RISK | AI-Driven Hyper-Local Early Warning System f... | Ministry of Earth Sciences... | Disaster Management... | 6.5 | 7.0 | 5.0 | 6.0 | 7.0 | 6.0 |
|  70 | SIH26166 | 5.85 | +0.39 | 6.45 | 6.70 | HIGH RISK | Multi-modal, Sun angle and scale invariant i... | Indian Space Research Orga... | Space Technology... | 6.5 | 7.5 | 5.0 | 7.0 | 7.5 | 4.5 |
|  71 | SIH26054 | 5.85 | +0.46 | 6.64 | 6.95 | HIGH RISK | AI-Enabled Real-Time Digital Twin System for... | DRDO... | Robotics and Drones... | 7.3 | 7.0 | 5.0 | 5.5 | 7.5 | 6.0 |
|  72 | SIH26034 | 5.85 | +0.48 | 6.60 | 7.50 | HIGH RISK | Software System to check compliance of Packa... | Ministry of Consumer Affai... | Miscellaneous... | 5.0 | 7.5 | 4.0 | 7.0 | 8.5 | 7.5 |
|  73 | SIH26201 | 5.84 | +0.32 | 6.45 | 6.15 | HIGH RISK | Student Innovation-There is a need to design... | AICTE... | Robotics and Drones... | 5.5 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  74 | SIH26203 | 5.83 | +0.19 | 6.30 | 5.40 | HIGH RISK | Student Innovation-Creating intelligent devi... | AICTE... | Smart Vehicles... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  75 | SIH26209 | 5.81 | +0.23 | 6.30 | 5.65 | HIGH RISK | Student Innovation-Space technology refers t... | AICTE... | Space Technology... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  76 | SIH26142 | 5.80 | +0.35 | 6.35 | 6.25 | HIGH RISK | Deep Learning Based Super Resolution Mapping... | National Technical Researc... | Space Technology... | 6.5 | 7.5 | 5.5 | 7.0 | 4.5 | 4.5 |
|  77 | SIH26132 | 5.80 | +0.38 | 6.65 | 6.45 | HIGH RISK | Strengthening market linkages and price disc... | Government Of Maharashtra... | Agriculture, FoodTec... | 6.5 | 7.0 | 5.0 | 5.0 | 6.5 | 6.0 |
|  78 | SIH26085 | 5.80 | +0.60 | 6.73 | 7.85 | HIGH RISK | Urban Flood Nowcasting System (Drainage and ... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.0 | 5.0 | 7.0 | 7.5 |
|  79 | SIH26069 | 5.80 | +0.69 | 6.67 | 8.55 | HIGH RISK | National Weather Big Data Analytics Platform... | Ministry of Earth Sciences... | Disaster Management... | 5.0 | 7.0 | 5.0 | 6.0 | 7.0 | 7.5 |
|  80 | SIH26197 | 5.79 | +0.25 | 6.30 | 5.80 | HIGH RISK | Student Innovation-Ideas that showcase the r... | AICTE... | Heritage & Culture... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  81 | SIH26196 | 5.79 | +0.27 | 6.30 | 5.90 | HIGH RISK | Student Innovation-Ideas that can boost fitn... | AICTE... | Fitness & Sports... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  82 | SIH26204 | 5.79 | +0.27 | 6.30 | 5.90 | HIGH RISK | Student Innovation-A solution/idea that can ... | AICTE... | Travel & Tourism... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  83 | SIH26191 | 5.79 | +0.57 | 6.78 | 7.55 | HIGH RISK | Intelligent Identification of Hazard-Based R... | Ministry of Home Affairs... | Disaster Management... | 5.5 | 7.0 | 5.0 | 5.0 | 5.5 | 7.5 |
|  84 | SIH26163 | 5.79 | +0.69 | 6.50 | 8.60 | HIGH RISK | Security Assessment of the World Monitor app... | National Technical Researc... | Smart Automation... | 5.5 | 7.5 | 5.0 | 8.0 | 4.5 | 7.5 |
|  85 | SIH26100 | 5.76 | +0.37 | 6.30 | 6.90 | HIGH RISK | AI-Powered Integrated Bid Compliance Verific... | Ministry of Petroleum & Na... | Smart Automation... | 5.0 | 7.5 | 4.0 | 7.0 | 8.5 | 7.5 |
|  86 | SIH26083 | 5.76 | +0.66 | 6.73 | 8.25 | HIGH RISK | Extreme Heatwave Early Warning and Human The... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.0 | 5.0 | 7.0 | 7.5 |
|  87 | SIH26090 | 5.75 | +0.51 | 6.58 | 7.35 | HIGH RISK | AI-Driven Market Linkage and Smart Catalogin... | Ministry of Social Justice... | Heritage & Culture... | 6.5 | 7.0 | 5.0 | 5.0 | 6.5 | 7.5 |
|  88 | SIH26124 | 5.75 | +0.65 | 6.63 | 8.20 | HIGH RISK | AI-Powered Mobile Urban Intelligence Platfor... | Bharat Electronics Limited... | Smart Automation... | 6.5 | 7.0 | 5.0 | 5.0 | 7.5 | 7.5 |
|  89 | SIH26081 | 5.75 | +0.67 | 6.73 | 8.35 | HIGH RISK | Hybrid AI–NWP Multi-Model Forecast Blending ... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.0 | 5.0 | 7.0 | 7.5 |
|  90 | SIH26079 | 5.75 | +0.68 | 6.73 | 8.20 | HIGH RISK | AI-Based Forecast Bust Detection for Medium-... | Ministry of Earth Sciences... | Smart Automation... | 5.5 | 7.0 | 5.5 | 5.0 | 4.5 | 7.5 |
|  91 | SIH26097 | 5.74 | +0.18 | 6.30 | 5.35 | HIGH RISK | AI-Driven voice Assistant for livelihood Map... | Ministry of Social Justice... | Agriculture, FoodTec... | 5.5 | 7.0 | 5.0 | 5.0 | 6.5 | 6.0 |
|  92 | SIH26056 | 5.74 | +0.53 | 6.53 | 7.80 | HIGH RISK | Development of a Real-time Airfare Price Ind... | MoSPI... | Smart Automation... | 5.0 | 8.0 | 4.0 | 7.0 | 7.5 | 7.5 |
|  93 | SIH26074 | 5.73 | +0.18 | 6.45 | 5.20 | HIGH RISK | Downscaling of weather forecast from Block l... | Ministry of Earth Sciences... | Agriculture, FoodTec... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 6.0 |
|  94 | SIH26200 | 5.73 | +0.34 | 6.30 | 6.40 | HIGH RISK | Student Innovation-Innovative ideas that hel... | AICTE... | Renewable / Sustaina... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
|  95 | SIH26107 | 5.73 | +0.35 | 6.58 | 6.60 | HIGH RISK | Al-powered Intelligent Assistant for Indian ... | Ministry of Consumer Affai... | Smart Automation... | 5.5 | 7.0 | 4.0 | 5.0 | 8.5 | 7.5 |
|  96 | SIH26108 | 5.73 | +0.35 | 6.58 | 6.60 | HIGH RISK | AI-Powered Recommendation Engine for Identif... | Ministry of Consumer Affai... | Smart Automation... | 5.5 | 7.0 | 4.0 | 5.0 | 8.5 | 7.5 |
|  97 | SIH26009 | 5.72 | +0.18 | 6.10 | 5.50 | HIGH RISK | Using AI/ML and Space Technology to Identify... | Ministry of Steel... | Space Technology... | 5.5 | 7.0 | 5.0 | 5.0 | 8.5 | 6.0 |
|  98 | SIH26073 | 5.72 | +0.66 | 6.50 | 8.25 | HIGH RISK | AI/ML-Based Intelligent Anomaly Detection fo... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.5 | 5.5 | 7.0 | 6.0 |
|  99 | SIH26057 | 5.72 | +0.69 | 7.10 | 8.55 | HIGH RISK | AI-Powered Automated Underwater Marine Debri... | Ministry of Earth Sciences... | Disaster Management... | 8.0 | 5.5 | 4.0 | 5.0 | 7.0 | 7.5 |
| 100 | SIH26194 | 5.71 | +0.38 | 6.30 | 6.65 | HIGH RISK | Student Innovation-Provide ideas in a decent... | AICTE... | Blockchain & Cyberse... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
| 101 | SIH26187 | 5.71 | +0.62 | 6.85 | 7.90 | HIGH RISK | AI-Based Intelligent Video Analytics Platfor... | Ministry of Home Affairs... | Blockchain & Cyberse... | 6.5 | 7.0 | 5.0 | 5.0 | 5.5 | 6.0 |
| 102 | SIH26189 | 5.71 | +0.62 | 6.85 | 7.90 | HIGH RISK | AI-Powered Criminal Network Analysis System... | Ministry of Home Affairs... | Blockchain & Cyberse... | 6.5 | 7.0 | 5.0 | 5.0 | 5.5 | 6.0 |
| 103 | SIH26092 | 5.70 | +0.65 | 6.63 | 8.20 | HIGH RISK | AI-Driven Scheme Matching for Marginalized E... | Ministry of Social Justice... | Smart Automation... | 6.5 | 7.0 | 5.0 | 5.0 | 6.5 | 7.5 |
| 104 | SIH26182 | 5.69 | +0.57 | 6.42 | 7.70 | HIGH RISK | Automated Attribution of Unknown Cryptocurre... | Ministry of Home Affairs... | Blockchain & Cyberse... | 5.0 | 6.0 | 5.5 | 5.0 | 5.5 | 7.5 |
| 105 | SIH26165 | 5.67 | +0.49 | 6.33 | 7.40 | HIGH RISK | AI/NLP Engine to Detect Serious Injury & Fat... | Oil India Limited... | Smart Automation... | 5.5 | 7.0 | 5.0 | 5.0 | 7.5 | 7.5 |
| 106 | SIH26027 | 5.66 | +0.23 | 6.05 | 5.85 | HIGH RISK | Al-Powered Automatic Block Planning to Maxim... | Ministry of Railways... | Transportation & Log... | 5.5 | 7.0 | 5.0 | 5.0 | 8.5 | 6.0 |
| 107 | SIH26202 | 5.66 | +0.45 | 6.30 | 7.15 | HIGH RISK | Student Innovation-Ideas focused on the inte... | AICTE... | Smart Automation... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
| 108 | SIH26228 | 5.66 | +0.59 | 6.25 | 8.10 | HIGH RISK | Trustworthy Computer Vision Integrity Assura... | Ministry of defence (MoD)... | Blockchain & Cyberse... | 6.5 | 7.5 | 5.0 | 7.0 | 8.5 | 4.5 |
| 109 | SIH26106 | 5.65 | +0.55 | 6.25 | 7.80 | HIGH RISK | AI-Powered Email Threat Detection, GeoLocati... | All India Council for Tech... | Blockchain & Cyberse... | 6.5 | 5.5 | 5.0 | 5.0 | 8.5 | 7.5 |
| 110 | SIH26161 | 5.65 | +0.62 | 6.48 | 8.15 | HIGH RISK | Dam Break Inundation Modelling Using Hydrody... | National Technical Researc... | Disaster Management... | 5.5 | 6.5 | 5.0 | 7.0 | 4.5 | 6.0 |
| 111 | SIH26143 | 5.65 | +0.74 | 6.75 | 8.75 | HIGH RISK | Leveraging satellite imagery to determine Oi... | National Technical Researc... | Disaster Management... | 6.5 | 7.5 | 5.0 | 7.0 | 4.5 | 4.5 |
| 112 | SIH26152 | 5.63 | +0.63 | 6.68 | 8.10 | HIGH RISK | Social Media Analytics... | National Technical Researc... | Blockchain & Cyberse... | 6.5 | 7.0 | 5.0 | 5.0 | 4.5 | 7.5 |
| 113 | SIH26076 | 5.63 | +0.66 | 6.73 | 8.30 | HIGH RISK | Development of personalized homepage for 'Ma... | Ministry of Earth Sciences... | Smart Automation... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 7.5 |
| 114 | SIH26136 | 5.62 | +0.34 | 6.05 | 6.35 | HIGH RISK | Startup friendly public procurement mechanis... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 5.0 | 6.5 | 6.0 |
| 115 | SIH26155 | 5.61 | +0.55 | 6.33 | 7.80 | HIGH RISK | AI-Driven Multi-Vendor Network Security Comp... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 7.5 | 5.0 | 7.0 | 4.5 | 6.0 |
| 116 | SIH26188 | 5.60 | +0.57 | 6.88 | 7.90 | HIGH RISK | Al-Based Fake Identity & Document Screening ... | Ministry of Home Affairs... | Blockchain & Cyberse... | 5.5 | 7.0 | 4.0 | 5.0 | 5.5 | 7.5 |
| 117 | SIH26091 | 5.58 | +0.33 | 6.60 | 6.45 | HIGH RISK | AI-Driven Hyper-Local Business Advisory and ... | Ministry of Social Justice... | Agriculture, FoodTec... | 6.5 | 7.0 | 4.0 | 5.0 | 6.5 | 6.0 |
| 118 | SIH26086 | 5.58 | +0.41 | 6.45 | 6.75 | HIGH RISK | Hyperlocal Monsoon Onset & Break Prediction ... | Ministry of Earth Sciences... | Agriculture, FoodTec... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 6.0 |
| 119 | SIH26120 | 5.58 | +0.49 | 6.29 | 7.40 | HIGH RISK | Digital Twin for Well-to-Surface Optimizatio... | Oil India Limited... | Smart Automation... | 6.3 | 7.0 | 5.0 | 5.0 | 7.5 | 6.0 |
| 120 | SIH26134 | 5.58 | +0.52 | 6.28 | 7.60 | HIGH RISK | Challenges in aligning skill development pro... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 5.0 | 5.0 | 6.5 | 7.5 |
| 121 | SIH26130 | 5.58 | +0.57 | 6.33 | 7.90 | HIGH RISK | Efficiency in streamlining industrial approv... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 5.0 | 5.0 | 6.5 | 7.5 |
| 122 | SIH26024 | 5.58 | +0.62 | 6.65 | 8.40 | HIGH RISK | AI-Based Smart Governance and Compliance Mon... | Ministry of Coal... | Smart Automation... | 8.0 | 5.5 | 4.0 | 5.0 | 8.5 | 7.5 |
| 123 | SIH26160 | 5.57 | +0.50 | 6.42 | 7.40 | HIGH RISK | AI-Powered IPsec VPN Protocol Analyzer and S... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 7.5 |
| 124 | SIH26190 | 5.57 | +0.53 | 6.48 | 7.50 | HIGH RISK | Secure Digital Document Management System fo... | Ministry of Home Affairs... | Blockchain & Cyberse... | 6.5 | 5.5 | 5.0 | 5.0 | 5.5 | 6.0 |
| 125 | SIH26044 | 5.56 | +0.35 | 6.28 | 6.80 | HIGH RISK | Portal for Academia - Industry collaboration... | Ministry of Ayush... | Smart Automation... | 5.0 | 7.0 | 4.0 | 5.0 | 8.5 | 7.5 |
| 126 | SIH26192 | 5.56 | +0.55 | 6.63 | 7.55 | HIGH RISK | Flash Flood Prediction System for Hilly Regi... | Ministry of Home Affairs... | Disaster Management... | 6.5 | 7.0 | 5.0 | 5.0 | 5.5 | 4.5 |
| 127 | SIH26059 | 5.55 | +0.43 | 6.45 | 6.95 | HIGH RISK | AI-Enabled Antarctic Sea-Ice, Iceberg Trajec... | Ministry of Earth Sciences... | Transportation & Log... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 6.0 |
| 128 | SIH26104 | 5.54 | +0.58 | 6.15 | 8.10 | HIGH RISK | AI-Powered Real-Time Detection and Preventio... | All India Council for Tech... | Blockchain & Cyberse... | 6.5 | 6.0 | 5.0 | 5.5 | 8.5 | 6.0 |
| 129 | SIH26116 | 5.54 | +0.60 | 6.05 | 8.10 | HIGH RISK | Urban Mixed-Use Design Challenge-Design a ce... | Autodesk... | Miscellaneous... | 5.5 | 7.0 | 5.5 | 5.0 | 8.5 | 6.0 |
| 130 | SIH26199 | 5.54 | +0.65 | 6.30 | 8.40 | HIGH RISK | Student Innovation-Technology ideas in terti... | AICTE... | Miscellaneous... | 5.0 | 8.0 | 5.0 | 6.0 | 5.5 | 7.0 |
| 131 | SIH26075 | 5.52 | +0.36 | 6.58 | 6.70 | HIGH RISK | Participants are invited to design and devel... | Ministry of Earth Sciences... | Smart Education... | 5.0 | 7.0 | 4.0 | 5.0 | 4.5 | 7.5 |
| 132 | SIH26183 | 5.52 | +0.46 | 6.20 | 7.30 | HIGH RISK | Real-Time Identification of Fraud-Linked Cry... | Ministry of Home Affairs... | Blockchain & Cyberse... | 5.5 | 4.5 | 5.0 | 5.0 | 5.5 | 7.5 |
| 133 | SIH26154 | 5.52 | +0.58 | 6.42 | 7.90 | HIGH RISK | Gen AI Platform for Automated Content Transf... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 7.5 |
| 134 | SIH26053 | 5.50 | +0.21 | 5.83 | 5.85 | HIGH RISK | Adaptive Variable Resolution 2.5D Lidar Mapp... | DRDO... | Smart Vehicles... | 6.5 | 5.5 | 5.0 | 5.0 | 7.5 | 6.0 |
| 135 | SIH26125 | 5.49 | +0.40 | 5.90 | 7.10 | HIGH RISK | Blockchain-Based Secure Platform for Identit... | Bharat Electronics Limited... | Blockchain & Cyberse... | 5.5 | 5.5 | 5.0 | 5.0 | 7.5 | 7.5 |
| 136 | SIH26070 | 5.49 | +0.56 | 6.23 | 7.95 | HIGH RISK | To develop an Artificial Intelligence (AI) /... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.0 | 6.0 | 7.0 | 4.5 |
| 137 | SIH26171 | 5.49 | +0.64 | 6.25 | 8.40 | HIGH RISK | On-device Visual Perception for Light-weight... | Indian Space Research Orga... | Smart Automation... | 6.5 | 7.5 | 5.0 | 7.0 | 5.5 | 4.5 |
| 138 | SIH26127 | 5.49 | +0.69 | 6.63 | 8.80 | HIGH RISK | City-Wide AI Engine for Multi-Camera ANPR Tr... | Bharat Electronics Limited... | Smart Automation... | 6.5 | 7.0 | 4.0 | 5.0 | 7.5 | 7.5 |
| 139 | SIH26129 | 5.48 | +0.50 | 6.50 | 7.70 | HIGH RISK | System integration and interoperability amon... | Government Of Maharashtra... | Miscellaneous... | 6.5 | 6.5 | 4.0 | 5.0 | 6.5 | 7.5 |
| 140 | SIH26061 | 5.47 | +0.27 | 6.23 | 5.95 | HIGH RISK | AI-Driven Smart Energy Management System for... | Ministry of Earth Sciences... | Clean & Green Techno... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 4.5 |
| 141 | SIH26023 | 5.47 | +0.48 | 6.28 | 7.70 | HIGH RISK | AI-Powered Geological, Mining and other Repo... | Ministry of Coal... | Smart Automation... | 5.5 | 7.0 | 4.0 | 5.0 | 8.5 | 7.5 |
| 142 | SIH26123 | 5.47 | +0.48 | 6.10 | 7.50 | HIGH RISK | Edge-AI Based Distributed Fleet Coordination... | Bharat Electronics Limited... | Smart Automation... | 5.5 | 7.0 | 5.0 | 5.0 | 7.5 | 6.0 |
| 143 | SIH26169 | 5.46 | +0.64 | 6.35 | 8.40 | HIGH RISK | Development of an AI-Based Virtual Camera Tr... | Indian Space Research Orga... | Smart Automation... | 6.5 | 7.0 | 5.0 | 5.5 | 5.5 | 6.0 |
| 144 | SIH26153 | 5.44 | +0.66 | 6.58 | 8.70 | HIGH RISK | AI based Network Attack Forecasting from Net... | National Technical Researc... | Blockchain & Cyberse... | 6.5 | 7.5 | 4.0 | 7.0 | 4.5 | 6.0 |
| 145 | SIH26146 | 5.43 | +0.49 | 6.05 | 7.40 | HIGH RISK | AI-Powered Monitoring & Analysis of Bitcoin ... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 5.5 | 5.5 | 4.5 | 4.5 | 7.5 |
| 146 | SIH26051 | 5.43 | +0.59 | 6.05 | 8.20 | HIGH RISK | Software Based Model Development for Design ... | DRDO... | Miscellaneous... | 5.5 | 7.0 | 5.0 | 5.5 | 7.5 | 6.0 |
| 147 | SIH26080 | 5.43 | +0.63 | 6.45 | 8.20 | HIGH RISK | Regime-Aware AI Post-Processing of Monsoon R... | Ministry of Earth Sciences... | Smart Automation... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 6.0 |
| 148 | SIH26121 | 5.42 | +0.39 | 6.17 | 7.15 | HIGH RISK | eRTMAC-NWIS (Nearby Wells Intelligence Syste... | Oil India Limited... | Smart Automation... | 5.0 | 7.0 | 4.0 | 5.0 | 7.5 | 7.5 |
| 149 | SIH26122 | 5.42 | +0.66 | 5.90 | 8.60 | HIGH RISK | Intelligent Data Capture & Schedule-Linking ... | Oil India Limited... | Smart Automation... | 5.0 | 7.0 | 5.5 | 5.5 | 7.5 | 6.0 |
| 150 | SIH26068 | 5.41 | +0.52 | 6.50 | 7.85 | HIGH RISK | WeatherGPT: Conversational AI for Weather Fo... | Ministry of Earth Sciences... | Disaster Management... | 6.5 | 6.0 | 4.0 | 5.0 | 7.0 | 6.0 |
| 151 | SIH26114 | 5.41 | +0.62 | 6.05 | 8.40 | HIGH RISK | Smart City Site Planning using Autodesk Form... | Autodesk... | Miscellaneous... | 5.5 | 7.0 | 5.0 | 5.0 | 8.5 | 6.0 |
| 152 | SIH26062 | 5.39 | +0.36 | 6.08 | 6.70 | HIGH RISK | Integrated Polar Expedition Logistics and As... | Ministry of Earth Sciences... | Smart Automation... | 5.5 | 5.5 | 5.0 | 5.0 | 4.5 | 6.0 |
| 153 | SIH26126 | 5.39 | +0.51 | 6.13 | 7.70 | HIGH RISK | Vision Based Autonomous Navigation for Unman... | Bharat Electronics Limited... | Smart Automation... | 6.5 | 7.0 | 5.0 | 5.0 | 7.5 | 4.5 |
| 154 | SIH26071 | 5.39 | +0.56 | 6.23 | 7.95 | HIGH RISK | AI/ML-Based Integrated heavy rainfall Early ... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.0 | 5.0 | 7.0 | 4.5 |
| 155 | SIH26072 | 5.39 | +0.56 | 6.23 | 7.95 | HIGH RISK | AIML based Nowcasting of thunderstorm and li... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.0 | 5.0 | 7.0 | 4.5 |
| 156 | SIH26105 | 5.39 | +0.57 | 6.17 | 8.40 | HIGH RISK | AI-Powered Continuous Cyber Risk Quantificat... | All India Council for Tech... | Blockchain & Cyberse... | 5.0 | 7.0 | 4.0 | 5.5 | 8.5 | 7.5 |
| 157 | SIH26063 | 5.38 | +0.27 | 6.35 | 6.20 | HIGH RISK | Integrated Polar Science Outreach, Knowledge... | Ministry of Earth Sciences... | Smart Education... | 5.0 | 7.0 | 4.0 | 5.0 | 4.5 | 6.0 |
| 158 | SIH26159 | 5.35 | +0.62 | 5.95 | 8.50 | HIGH RISK | SecureMailScope: AI-Assisted Cryptographic S... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 6.0 | 5.0 | 7.0 | 4.5 | 6.0 |
| 159 | SIH26164 | 5.34 | +0.52 | 6.05 | 8.10 | HIGH RISK | Enterprise Cryptographic Discovery & Analysi... | National Technical Researc... | Blockchain & Cyberse... | 6.5 | 6.0 | 4.0 | 8.0 | 4.5 | 6.0 |
| 160 | SIH26066 | 5.33 | +0.65 | 6.23 | 8.55 | HIGH RISK | OceanEmbed - Satellite Embedding-Based Deep ... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 7.0 | 5.0 | 5.0 | 7.0 | 4.5 |
| 161 | SIH26157 | 5.31 | +0.58 | 6.20 | 8.10 | HIGH RISK | Supervisory Analytics Tool for SOC Assessmen... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 6.0 |
| 162 | SIH26067 | 5.29 | +0.49 | 6.23 | 7.75 | HIGH RISK | Develop a web-based interactive 3D visualiza... | Ministry of Earth Sciences... | Disaster Management... | 5.5 | 5.5 | 4.0 | 5.0 | 7.0 | 6.0 |
| 163 | SIH26147 | 5.26 | +0.32 | 5.92 | 6.50 | HIGH RISK | Automated model for analysis of .IQ and .wav... | National Technical Researc... | Space Technology... | 5.5 | 7.0 | 5.0 | 5.0 | 4.5 | 4.5 |
| 164 | SIH26170 | 5.26 | +0.61 | 6.05 | 8.40 | HIGH RISK | AI-Driven Anomaly Detection in Component Bur... | Indian Space Research Orga... | Smart Automation... | 5.5 | 7.0 | 5.0 | 5.0 | 5.5 | 6.0 |
| 165 | SIH26173 | 5.24 | +0.56 | 6.08 | 8.00 | HIGH RISK | iTantra -Indian Multilingual TTS & STT Aided... | Indian Space Research Orga... | Smart Automation... | 6.5 | 7.0 | 5.0 | 5.0 | 5.5 | 4.5 |
| 166 | SIH26117 | 5.19 | +0.57 | 5.80 | 8.60 | HIGH RISK | Sovereign On-Premise Agentic AI Workbench us... | Mangalore Refinery and Pet... | Smart Automation... | 5.0 | 7.5 | 4.0 | 7.0 | 8.5 | 4.5 |
| 167 | SIH26055 | 5.18 | +0.40 | 5.68 | 7.55 | HIGH RISK | Smart Scan strategy for Electronic Warfare... | DRDO... | Robotics and Drones... | 6.5 | 6.0 | 4.0 | 7.0 | 7.5 | 4.5 |
| 168 | SIH26148 | 5.17 | +0.43 | 5.78 | 7.40 | HIGH RISK | Creation of scripts/functions with new progr... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 5.5 | 5.0 | 5.0 | 4.5 | 6.0 |
| 169 | SIH26156 | 5.17 | +0.43 | 5.78 | 7.40 | HIGH RISK | Universal Log Pre-processing Framework... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 5.5 | 5.0 | 5.0 | 4.5 | 6.0 |
| 170 | SIH26151 | 5.17 | +0.63 | 6.28 | 8.70 | HIGH RISK | Dark web threat actor de-anonymization... | National Technical Researc... | Blockchain & Cyberse... | 5.0 | 7.0 | 4.0 | 5.0 | 4.5 | 7.5 |
| 171 | SIH26095 | 5.13 | +0.50 | 5.88 | 8.10 | HIGH RISK | Smart Real-Time Monitoring & Inspection Mobi... | Ministry of Social Justice... | Smart Automation... | 4.0 | 7.0 | 4.0 | 5.0 | 6.5 | 7.5 |
| 172 | SIH26135 | 5.13 | +0.53 | 6.05 | 8.20 | HIGH RISK | Difficulties in tracking employment outcomes... | Government Of Maharashtra... | Miscellaneous... | 5.5 | 7.0 | 4.0 | 5.0 | 6.5 | 6.0 |
| 173 | SIH26149 | 5.13 | +0.55 | 5.83 | 8.10 | HIGH RISK | Design and Development of an Integrated Secu... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 5.5 | 5.0 | 5.0 | 4.5 | 6.0 |
| 174 | SIH26145 | 5.11 | +0.49 | 5.80 | 8.10 | HIGH RISK | AI-Based Detection of Cyber Threats in Unidi... | National Technical Researc... | Blockchain & Cyberse... | 5.0 | 6.0 | 4.0 | 7.0 | 4.5 | 6.0 |
| 175 | SIH26150 | 5.06 | +0.60 | 5.78 | 8.50 | HIGH RISK | Development of a Multi-Vendor DVR/NVR Forens... | National Technical Researc... | Blockchain & Cyberse... | 5.5 | 5.5 | 5.0 | 5.0 | 4.5 | 6.0 |

---

## Biggest movers v2 → v3 (quality > crowd for 5 Sep)

### Most improved (high Q, high CLS — penalized in v2, rewarded in v3)

| PS ID | v2 rank | v3 rank | Δ rank | WPS v2→v3 | Q | CLS | Why |
|-------|---------|---------|--------|-----------|---|-----|-----|
| SIH26078 | 89 | 41 | +48 | 5.25→5.98 | 7.03 | 8.35 | Q 7.03 overcomes CLS |
| SIH26099 | 86 | 46 | +40 | 5.29→5.96 | 6.60 | 8.40 | Q 6.60 overcomes CLS |
| SIH26084 | 92 | 53 | +39 | 5.22→5.94 | 7.03 | 8.45 | Q 7.03 overcomes CLS |
| SIH26012 | 51 | 15 | +36 | 5.57→6.29 | 7.48 | 8.20 | Q 7.48 overcomes CLS |
| SIH26060 | 99 | 65 | +34 | 5.18→5.88 | 7.21 | 8.20 | Q 7.21 overcomes CLS |
| SIH26143 | 144 | 111 | +33 | 4.91→5.65 | 6.75 | 8.75 | Q 6.75 overcomes CLS |
| SIH26001 | 52 | 21 | +31 | 5.56→6.20 | 7.18 | 7.85 | Q 7.18 overcomes CLS |
| SIH26103 | 75 | 45 | +30 | 5.39→5.96 | 6.98 | 7.80 | Q 6.98 overcomes CLS |
| SIH26016 | 79 | 49 | +30 | 5.37→5.95 | 7.10 | 7.80 | Q 7.10 overcomes CLS |
| SIH26119 | 58 | 29 | +29 | 5.53→6.08 | 6.58 | 7.40 | Q 6.58 overcomes CLS |
| SIH26162 | 69 | 40 | +29 | 5.44→5.98 | 6.98 | 7.30 | Q 6.98 overcomes CLS |
| SIH26028 | 81 | 52 | +29 | 5.35→5.94 | 6.63 | 7.70 | Q 6.63 overcomes CLS |

### Most dropped (low Q, low CLS — v2 hidden gems lose edge in v3)

| PS ID | v2 rank | v3 rank | Δ rank | WPS v2→v3 | Q | CLS | Why |
|-------|---------|---------|--------|-----------|---|-----|-----|
| SIH26063 | 105 | 157 | -52 | 5.11→5.38 | 6.35 | 6.20 | Low Q, low-CLS moat devalued |
| SIH26053 | 85 | 134 | -49 | 5.29→5.50 | 5.83 | 5.85 | Low Q, low-CLS moat devalued |
| SIH26061 | 97 | 140 | -43 | 5.20→5.47 | 6.23 | 5.95 | Low Q, low-CLS moat devalued |
| SIH26009 | 55 | 97 | -42 | 5.54→5.72 | 6.10 | 5.50 | Low Q, low-CLS moat devalued |
| SIH26074 | 54 | 93 | -39 | 5.55→5.73 | 6.45 | 5.20 | Low Q, low-CLS moat devalued |
| SIH26097 | 53 | 91 | -38 | 5.56→5.74 | 6.30 | 5.35 | Low Q, low-CLS moat devalued |
| SIH26027 | 70 | 106 | -36 | 5.43→5.66 | 6.05 | 5.85 | Low Q, low-CLS moat devalued |
| SIH26195 | 26 | 60 | -34 | 5.77→5.88 | 6.30 | 4.90 | Low Q, low-CLS moat devalued |

---

## Spotlight re-evaluation: SIH26171 (your URL) under v3

**SIH26171 — On-device Visual Perception for Light-weight Browser Agents · ISRO · Miscellaneous**

*Spec*: extension (WebGPU/WASM + ONNX Runtime Web, Transformers.js) local ViT reads screen → DOM-aware PII filter (blur faces / blackout passwords / mask PII) → anonymized to server LLM/VLM → returns UI action. Eval: visual 25% + PII recall 20% + redaction 20% + resource 20% + latency 15%.

| Engine | Q | CLS | WPS v2 | WPS v3 | Verdict | Expected/500 | Rank |
|--------|---|-----|--------|--------|---------|--------------|------|
| **v2 truncated raw (all-175 JSON)** | 6.25 | 8.40 | 4.85 | **5.49** (+0.64) | HIGH RISK | 420 | v2 #148 → v3 #137 |
| **v3 live full spec (your URL, this eval)** | 5.95 | 7.80 | 4.88 | **5.40** (+0.52) | HIGH RISK | 390 | ~#152 /175 |

**CLS breakdown (live)**: Theme 10.0 (miscellaneous) ×25% + Org 7.0 (ISRO) ×20% + Keyword 10 (ai/llm) ×25% + Ease 5.0 ×20% + Buzz 4.0 ×10% = **7.8–8.4** (CRITICAL). Miscellaneous is the *most crowded theme* (10), ISRO is hyped (7), `agentic ai` is 2026 buzz peak.

**Why still HIGH RISK even in v3 (internal-friendly)**:
- Demo 4.5 + MinistryFit 5.5 drag Quality to 5.95 (below v3 avg 6.51). ISRO diffuse intent (10 PS) + browser-privacy ≠ core ISRO KPI (earth/space data).
- Diff 5.0 — every team will demo bbox blur; rubric demands 40% on redaction precision, but PS gives no proprietary data — you synthesize screens.
- Even with CLS de-weighted 15%, (10-7.8)×0.10 = 0.22 vs (10-7.8)×0.25 = 0.55 — gain only +0.52 WPS. High-Q PS (7.3–7.6) gain +0.37 to +0.72 and leapfrog it.
- Rank **137–152/175** in both v2 and v3 — bottom 15%. Internal judges on 5 Sep will still compare you to SIH26014 (7.14, Q 7.62) or SIH26167 SatQuery (5.85→~6.3 v3) which demo clearer ISRO value.

**If you must pitch SIH26171 at internal (only if team owns WebGPU/privacy)**:
1. **Differentiator**: server-aware `mask_map.json` (client sends redaction coordinates so server LLM reasons over `[REDACTED]` tokens, not pixels) + live resource telemetry overlay (GPU mem/latency) — hits the 20% resource + 40% privacy rubric directly.
2. **Dataset**: generate 500 synthetic screens with injected PII (faces/passwords/PAN/cards) + DOM ground truth; show recall/precision curve live.
3. **Submission note**: internal 5 Sep is safe, but if you clear internal, **national portal still freezes ~17 Sep** — switch primary to SIH26045/SIH26014 for nationals if needed (SPOC allows backup).

---

## Strategy for 5 Sep internal (v3 lens)

**Lock primary by 2 Sep**: `SIH26045 IP-SAKTI (7.33) → SIH26014 Land Stack (7.14) → SIH26036 Verification (6.92)`. All three are WORKABLE in both v2 and v3 — you are safe whether SPOC judges on crowd or quality.

**If you love ISRO/browser**: prefer `SIH26168 Dead Reckoning (6.32, +0.36 v3)` or `SIH26167 SatQuery (5.85→~6.2)` over SIH26171 — same org, +0.6–0.9 WPS, clearer ISRO mandate and easier demo (GIS vs privacy split).

**National backup still matters**: v2 ranking (CLS-aware) still guides nationals after internal. Keep SIH26045 as ultimate fallback — it is #1 in both v2 and v3.

---

## Files

| Artifact | Path |
|----------|------|
| v3 JSON+CSV (WPS v3 freeze-adjusted) | `projects/sih26/research/ps-evaluation/all-175-evaluated-v3.json` + `.csv` · `reference/sih26/` mirror |
| v3 Report | `projects/sih26/research/ps-evaluation/06-complete-ps-ranking-v3.md` · `reference/sih26/` mirror |
| v2 (preserved) | `05-complete-ps-ranking-v2.md` + `all-175-evaluated-v2.json` |
| Engine | `/tmp/eval_v2.py` (v2 scores) + `all-175-evaluated-v3.json` = `wps_v3 = Q×0.50 + (10-CLS)×0.10 + Diff×0.20 + Dataset×0.10 + Demo×0.05 + MFit×0.05` |

*Internal 5 Sep ≠ ignore CLS forever — use v3 to win internal, v2 to survive nationals.*
