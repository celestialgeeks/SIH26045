# 6-Bucket Evaluation Framework for SIH 2026 PS Selection

## Bucket 1 — QUALITY (40%)
**Question:** Will this PS, even if executed brilliantly, score >7.5/10 on official rubric?

| Sub-criterion | Weight | Score 1-10 | What it Measures |
|---|---|---|---|
| Innovation Headroom | 30% | ? | Can we add a real twist that isn't in PS description? |
| Technical Feasibility | 25% | ? | Can 6 students build working prototype in 36 hrs? |
| Impact | 20% | ? | Who benefits? How many? Real ministry deployment? |
| Demo-ability | 15% | ? | Can a judge see it work in 90 seconds? |
| Team Fit | 10% | ? | Do we already have 60% of skills in our team? |

**Verdict thresholds:**
- >8.0 = STRONG PICK (target this)
- 6.5-8.0 = WORKABLE (need strong execution)
- <6.5 = HIGH RISK (skip unless desperation)

## Bucket 2 — CROWDEDNESS (25%)
**Question:** How many teams will compete for the same PS? Lower = higher win %.

**CLS Formula:** `CLS = (Theme×0.25) + (Org×0.20) + (Keyword×0.25) + (Perceived Ease×0.20) + (Buzz×0.10)`
- 1-3 = Hidden gem (submit anytime)
- 4-6 = Moderate (submit by 18 Sep)
- 7-10 = Bloodbath (submit by 17 Sep, prepare backup)

## Bucket 3 — DIFFERENTIATION POTENTIAL (15%)
**Question:** Can we add 1+ measurable novelty that beats existing solutions?

| Differentiation Pattern | Example |
|---|---|
| Twist on saturated theme | Use coin-reference to measure mm from photo |
| Persona switch | Add citizen/whistleblower mode |
| Cross-system reconciliation | Compare physical vs e-commerce listing |
| Citation-grounded AI | Every answer cites statute § |
| Safety abstention | Correctly handle adversarial queries |
| Native infrastructure | Bhashini, ONDC, Aadhaar, UPI |

Score: 1 = No headroom (just build checklist), 10 = 3+ differentiators ready

## Bucket 4 — DATASET & INFRASTRUCTURE (10%)
**Question:** Can we get the data/hardware in time?

| Data type | Difficulty | Score |
|---|---|---|
| Public API free, immediate | 1 | 10 |
| Public dataset downloadable | 2 | 9 |
| Synthesize from rules/sample | 3 | 7 |
| Need org MoU | 4 | 4 |
| Paywalled (Clarksons, LexisNexis) | 5 | 3 |
| Need field collection | 6 | 2 |
| Need special hardware (₹>50k) | 7 | 1 |

## Bucket 5 — DEMOABILITY (5%)
**Question:** Can a judge see it work in 90 seconds?

- Live demo on mobile/laptop with real data
- Single-page clarity (no menu diving)
- 1 wow moment in first 10 seconds
- Handles judge's "what if" live
- Deployable URL accessible from nodal center WiFi

Score: 1-10

## Bucket 6 — MINISTRY FIT (5%)
**Question:** Does our solution align with the ministry's actual KPI?

- Read PS org's recent Annual Report
- Find their stated goals (Digital India, Make in India, etc.)
- Speak their language (₹ saved, beneficiaries, districts)
- Connect to a program they have funded (NAMASTE portal, SVAMITVA, NAKSHA)

Score: 1-10

## COMPOSITE WIN-PROBABILITY SCORE (WPS)

```
WPS = (Quality × 0.40) + ((10-CLS) × 0.25) + (Differentiation × 0.15) + (Dataset × 0.10) + (Demoability × 0.05) + (Ministry Fit × 0.05)
```

**WPS Thresholds:**
- >7.5 = Strong Pick (commit, build full prototype)
- 6.0-7.5 = Workable (commit but maintain backup)
- <6.0 = Skip or backup only

**Final Output:**
- Quality Score (0-10)
- CLS Crowdedness (0-10)
- Differentiation Score (0-10)
- Dataset Score (0-10)
- Demoability Score (0-10)
- Ministry Fit Score (0-10)
- WPS Composite (0-10)
- Verdict: Strong Pick / Workable / High Risk
- Strategic Action: Submit-by date + 3 differentiator moves
