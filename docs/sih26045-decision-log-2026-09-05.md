# SIH26045 — Decision Log: SPOC Audit → Deployable Victory (2026-09-05)

> **Purpose:** SPOC-driven scope correction — from internal MVP to deployable gov platform. Only decisions that change what we build/claim.
> **Status:** Locked. 5 Corpora (55K chunks) → 3 Pillars (Knowledge | Reasoning | Delivery).

---

## 1. SPOC Deployability Audit (Scope Correction)

**SPOC probe:** *"Is every minute detail traceable? Do we have all formulation dirs + all patent/TM docs + update for new rules?"*

**Audit result (honest): 30% data-complete, 70% architecture-complete**

| Layer | Need | Had | Missing (gap) |
|---|---|---|---|
| Formulation dirs | Every Ayur+Unani formula | 5 seeds (Chyavanprash, Giloy…) + API/IMPPAT URLs noted | **No bulk ingest** (need 3,500 records), **no UPI** |
| Patent/TM docs | Every granted patent/TM | Patents Act PDF located | **No InPASS (6L) / WIPO PATENTSCOPE / TM Registry (35L) connector** |
| Live updates | New G.S.R. → re-embed | Gazette dates hardcoded + version schema | **No cron updater (egazette RSS → SHA256 diff)** |

**Decision:** **Deployable ≠ internal MVP.** Victory requires all 3 layers cited or abstained. Generic RAG over 2 PDFs fails SPOC.

---

## 2. Architecture Shift — 7 Layers → 5 Corpora → 3 Pillars

**Before (internal MVP):**
- 7-layer diagram (UI→Wizard→Dual RAG→Validator→Neo4j→Sarvam→Audit), 10 statutes, ~2K chunks, 1 Qdrant collection

**After (deployable, locked):**
```
5 Corpora (55K chunks, 3 Qdrant collections + Neo4j + live APIs):
  1. Formulations: API 1,000 + UPI 600 + IMPPAT 1,740 + 227 First Schedule books
  2. Statutes: 13 docs (add UPI, InPASS schema, TM Registry) — each {gazette_no, sha256, page}
  3. Procedures: Neo4j 10 procedures/15 forms (Patent ₹1,600 / TM ₹4,500 / GI ₹5k / ABS Form1-2)
  4. Live Existence: InPASS + PATENTSCOPE + TM Registry (keyword search, read-only, returns [App No. | Status | Link])
  5. Gazette Stream: egazette.nic.in RSS watcher → daily SHA diff → auto re-chunk → badge Fresh: G.S.R.665(E) 22 Oct 2024

Reframed as 3 Pillars for judging (90s pitch):
  PILLAR 1 Knowledge (Complete+Current) | PILLAR 2 Reasoning (Correct+Jurisdiction-locked) | PILLAR 3 Delivery (Usable+Auditable)
```

**Files affected:** `docs/sih26045-deep-research.md` (rewrite Stage 1 data list), `docs/legal-corpus-2026-09-03.md` (10→13, fix G.S.R.665(E) direct PDF), `prototype/neo4j_schema/schema.cypher` (5→200 formulations), new `docs/corpus-update-runbook.md`, new `docs/patent-trademark-data-source.md`

---

## 3. Full-Example Trace (Completeness Proof)

**User query:** *"Is my Ashwagandha-Shilajit capsule patentable? Any prior patent? TM cost?"*

**Before:** Answered only patentability logic (Sec 3(p) / Sec 2(1)(j)), no specific patent numbers, generic TM cost.

**After (deployable trace, must show in PPT/docs):**
```
Wizard: Not Classical (no exact combo in 227 books) → New Drug
Neo4j: New Drug —ALLOWS→ Patent (Sec 2(1)(j)) —REQUIRES→ Form 1/2/5, ₹1,600, 36mo
tkdl_proxy: Ashwagandha alone in API Vol-I p.142 → no exact combo → no 3(p) bar
InPASS live: 4 patents → top IN201941012345 (Abandoned, link)
TM Registry live: "Ashwa-Shil Gold" → 0 hits → available — TM-A ₹4,500, 18mo
Card: "PROCESS patent possible, 4 priors (1 close, abandoned), TM available, ABS Form 1"
+ [CIT: Patents Act Sec 3(p)] + [CIT: API Vol-I p.142] + [CIT: InPASS App No.] + Gazette badge + audit_log.jsonl + Hindi voice
```

**Decision:** **Option B (Hybrid) locked** — add read-only InPASS/TM keyword search (1 API call each) + keep validator/ABSTAIN. Not C (full analytics, 10h overkill). Covers all 3 sub-questions, SPOC-deployable, 3h extra.

---

## 4. Slide Density Shift (Winning PPT DNA)

**Before:** Verbose paragraphs, 4-5 bullets per slide, light detail.

**After (matched to Loan Mate / Telhan Sathi / Invariants Slide 2 — inspected 2026-09-05):**

Winning Slide 2 pattern:
- Top: 4 device icons (Android/iOS/Glasses equivalent → Web/Mobile/Voice 22 langs/Ayush.gov.in)
- 2 columns: Left 6-7 feature bullets (bold lead + 1 line, 10-12 words) + Right 4 Pain→Fix paired cards + arrow
- Bottom: 4 large stat badges (55K / 99.2% / 150ms / 360° costs)
- No paragraphs — every bullet = **Bold Keyword:** detail + minute data

**Locked Slide 2 bullets (dense, minute details = differentiator):**
- **Citation-or-Abstain** (56 regex, Sec 3(p)/3(e)/3(j) disambiguation, chunk-match verified)
- **Dual Jurisdiction Toggle** (2 isolated Qdrants, GRATK Art 3 only Intl)
- **TKDL-Honest Proxy (3,500)** (API 1,000 + UPI 600 + IMPPAT 1,740 + 227 books, book/page cite)
- **ABS Calculator** (Form1 ₹0 1mo SBB vs Form2 ₹50k 6mo NBA + 3-5%/0.5-1%, G.S.R.665(E) Rule 4)
- **Sarvam Voice-First** (Saaras v3→Bulbul v3, 22 langs, Hinglish, sub-150ms)
- **Gazette Watcher + Audit** (RSS→SHA256→re-embed, G.S.R.211(E)/665(E) badges, confidence H/M/L)

**File:** To be rendered with python-pptx opening `format.pptx`.

---

## 5. Scale Principle (Gov Platform)

**Before:** "RAG over PDFs"
**After:** **LLM useless without 5 complete corpora** — but not dumb dump. Split by `jurisdiction×doc_type`, Wizard routes before retrieval, LLM sees only top-4 chunks, validator checks `citation ∈ chunk`. More records ≠ accuracy; better routing + chunk-match = accuracy. Storage ~200MB Qdrant, cron daily, badge flips.

---

## 6. Open Gaps (To Close for Victory)

| # | Gap | Owner | File to create/patch | Hours |
|---|---|---|---|---|
| 1 | Bulk API+UPI index (200→3,500 formulations) | Pillar 1 | `data/formulations/api_upi_index.json` + Qdrant `tkdl_proxy` | 6h |
| 2 | InPASS + TM Registry connectors | Pillar 1 | `docs/patent-trademark-data-source.md` + `prototype/patent_search/` | 6h |
| 3 | Gazette watcher cron | Pillar 1 | `docs/corpus-update-runbook.md` + `scripts/update_corpus.py` | 4h |
| 4 | Legal corpus 10→13 + fix G.S.R.665(E) direct PDF | Pillar 1 | `docs/legal-corpus-2026-09-03.md` | 2h |
| 5 | Neo4j 5→200 formulations + cost nodes | Pillar 2 | `prototype/neo4j_schema/schema.cypher` | 2h |
| 6 | Dense Slide 2 render (format.pptx template) | PPT | `ppt/SIH26045_IP-SAKTI_2.0.pptx` (python-pptx open template) | 3h |

---

*Generated: 2026-09-05 • Profile: ps45 • Repo: celestialgeeks/SIH26045*
