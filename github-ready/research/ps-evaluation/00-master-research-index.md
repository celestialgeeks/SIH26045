# SIH 2026 — Problem Statement Evaluation Master Research
**Date compiled:** September 2, 2026
**Purpose:** Foundational research for the `ps-evaluator` skill. All citations included.

---

## 1. The Real Numbers (Source: SIH 2025 winner Medium post by Harshita Yadav)

- **SIH 2025:** 271 problem statements, 72,165 idea submissions, 68,766 teams, only 1,360 reached Grand Finale
- **Ratio:** ~266 ideas per PS average. ~50 teams per PS filter ratio for selection
- **Key insight from winner:** *"Most PS had 500+ submissions. We picked one with ~250. Same effort, better odds."*
- **Counter cap:** 500 ideas per PS at `sih.gov.in`. Portal auto-freezes after that — first-come, first-served

## 2. Official Evaluation Rubric (Source: BMS Institute SIH 2026 Internal Rubric PDF + Reskilll)

### 10 Internal Hackathon Factors (BMS SIH 2026)
1. F1. Innovation & Creativity (novelty, out-of-the-box)
2. F2. Technical Feasibility (complexity, implementability, scalability)
3. F3. User Experience & Design (UI/UX, accessibility)
4. F4. Impact & Usefulness (problem-solution fit, potential impact, use cases)
5. F5. Technical Execution (working prototype, code quality, stack)
6. F6. Sustainability & Future Scope (long-term, environmental)
7. F7. Presentation & Communication (clarity, Q&A, pitch)
8. F8. Collaboration & Teamwork
9. F9. Business Viability (market, revenue, cost)
10. F10. Security & Privacy

### National + Grand Finale Rubric (widely-cited)
- Innovation 30% + Feasibility 20% + Technical Execution 20% + Impact 15% + Presentation 15% = 100
- `Final Score = (Innovation×3.0) + (Feasibility×2.0) + (Technical×2.0) + (Impact×1.5) + (Presentation×1.5)`

## 3. Crowdedness Likelihood Score (CLS) — 2026 Research-Backed

**Formula:** `CLS = (Theme×0.25) + (Org×0.20) + (Keyword×0.25) + (Perceived Ease×0.20) + (Buzz×0.10)`
**Scale:** 1 (empty) → 10 (bloodbath, hits 500 cap before 18 Sep)
**Expected submissions:** CLS/10 × 500
**Freeze risk:** CLS × 10%

### 5 Factor Score Tables (2026-tuned)

| Theme | Score | Theme | Score |
|---|---|---|---|
| Misc | 10 | MedTech | 4 |
| Smart Automation | 10 | Space Tech | 4 |
| Disaster Mgmt | 9 | Smart Education | 4 |
| Blockchain/Cyber | 8 | Agri/FoodTech | 3 |
| Heritage | 5 | Smart Vehicles | 3 |
| Fitness | 5 | Renewable | 2 |
| Travel | 5 | Clean & Green | 1 |
| Transportation | 5 | Toys & Games | 1 |

| Org | Score | Org | Score |
|---|---|---|---|
| AICTE (34 PS) | 10 | Ayush (3 PS) | 2 |
| MoES (30 PS) | 9 | MSME (3 PS) | 2 |
| NTRO (23 PS) | 8 | DoLR (9 PS) | 3 |
| MeitY/Health | 9 | SAIL/MOIL (1-2 PS) | 2 |
| Govt Maharashtra (9) | 6 | Consumer Affairs | 3 |
| DRDO | 6 | Egreen Quanta | 5 |
| Autodesk | 5 | Bihar/Jharkhand | 4 |

| Keyword 2026 Hype | Score | Counter-Hype Keywords | Score |
|---|---|---|---|
| AI / Chatbot / RAG / LLM | 10 | Legal Metrology / ULPIN | 2 |
| Blockchain / Web3 | 9 | GRATK / Nagoya | 2 |
| Smart App / Portal | 8 | Vessel Chartering | 2 |
| Scan / OCR / Image | 7 | Phytopharmaceutical | 2 |
| Drone / IoT | 6 | Traditional Knowledge | 3 |

| Perceived Ease | Score | Perceived Difficulty | Score |
|---|---|---|---|
| "Scan image, extract text" | 9 | Knowledge graph + Neo4j + 7 acts | 2 |
| "Build web portal" | 8 | LiDAR / 3D ULPIN / photogrammetry | 2 |
| "Chatbot with LLM" | 7 | Multidomain treaty citation + Bhashini | 2 |
| "Predict with ML" | 6 | Multi-radar nowcasting | 3 |

| 2026 Buzz | Score | Low Buzz | Score |
|---|---|---|---|
| GenAI / Agentic | 10 | Compliance / Kirana | 3 |
| On-device AI | 9 | TKDL / Ayush IP | 3 |
| Climate / Sustainability | 7 | Mining/Mineral data | 3 |

## 4. Differentiation Tactics (Source: Sachin Gautam PMs-AI win + Backboard Most Creative)

### The 3 Hackathon Win Patterns
1. **"Wait, why doesn't this exist already?"** — Pitch a problem the room is feeling (Sachin Nyx pattern)
2. **Common-burn observation** — Most teams can relate personally
3. **Speed-to-prototype under no ego** — Small focused team wins

### 7 Tactics to Beat the Crowd
1. **Twist on a saturated theme** — Add 1 measurable novelty diagram vs existing
2. **Persona switch** — Citizen/Whistleblower mode (not just officer)
3. **E-commerce mirror** — Cross-reference 2 systems (e.g., physical vs listing)
4. **Physical reference for measurement** — Coin/Aadhaar in frame for scale
5. **Multilingual native infra** — Use Bhashini (govt brownie points)
6. **Citation-grounded AI** — For legal/medical, every answer cites source
7. **Safety abstention** — Correctly say "uncertain" to adversarial queries (this is what kills ChatGPT wrappers in evaluation)

## 5. Efficiency Resources for Fast Evaluation

| Resource | URL | Use |
|---|---|---|
| sih.gov.in official PS list | sih.gov.in/sih2026PS | Source of truth (slow) |
| GitHub CSV | github.com/Rugved-dev18/SIH-2026-official-Software-Problem-Statements | Fast bulk scoring |
| Kaggle dataset | kaggle.com/datasets/riteshmaurya86/sih-2026-problem-statements-dataset | Excel-ready |
| SIH Buddy | sih-buddy.vercel.app | Pre-scored by Claude Opus, sort by acceptance |
| CodeHunters Academy | codehuntersacademy.com/sih-2026-ps | Verdict, Innovation Scope, Invention Effort, 36-hr Build Plan |
| SIH 2026 Browser | sih-2026-browser.vercel.app | Live counter `X/500` per PS |
| sih2026.vuce.in | sih2026.vuce.in/ps/SIHXXXXX | Per-PS detail view |
| Reskilll SIH 2026 framework | blogs.reskilll.com/how-to-select-validate-sih-2026-problem-statement-decision-framework | 6-step decision tree |
| InnovationProfessional Weighted Scoring | innovationprofessional.com/resources/methods/weighted-scoring-matrix | 4-8 dimension matrix methodology |
| Tamarack Impact-Feasibility Matrix | tamarackcommunity.ca/interactive-tools/impact-feasibility-matrix | 2D prioritization chart |

## 6. AI Tools for Hackathon Speed (2026)
- Cursor / Claude Code — codebase agent
- v0 / Bolt / Lovable — frontend from prompt
- LangGraph / CrewAI — agentic orchestration
- PaddleOCR / TrOCR — better than Tesseract
- Bhashini API — Indian language infra (govt favourite)
- Neo4j / Qdrant / Chroma — knowledge graph + vector
- ComfyUI / fal.ai — vision models
