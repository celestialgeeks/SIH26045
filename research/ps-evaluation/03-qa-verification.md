# QA Verification — ps-evaluator Skill
**Date:** 2026-09-03 03:10 IST  
**Skill:** `ps-evaluator` at `~/.hermes/profiles/sih26/skills/ps-evaluator/`  
**Vault mirror:** `my info/projects/sih26/research/ps-evaluation/`

## Checks

### 1. skill_view loads
```bash
skill_view(name='ps-evaluator')
→ success: true, readiness: available, linked_files: 4
```
**PASS**

### 2. Script runs on SIH26045 (canonical GEM)
```bash
python3 ~/.hermes/profiles/sih26/skills/ps-evaluator/scripts/evaluate.py
```
Output:
```
CLS Score: 2.6 / 10
Quality Score: 8.3 / 10
Verdict: STRONG PICK — Commit, build full prototype, push to internal as primary
Composite WPS: 8.02 / 10
Expected Submissions: ~130 / 500
Freeze Risk: 26.0%
breakdown: theme 1.0 + org 2.0 + keyword 5.0(NICHE-SUPPRESSED) + ease 2.0(HARD) + buzz 3.0(CAPPED)
```
**PASS** — matches spec: **8.3 quality, 2.6 CLS, Strong Pick**

### 3. Differentiation check (SIH26034)
```
SIH26034: CLS 5.0, Quality 6.8, Verdict WORKABLE, WPS 6.0
Expected Submissions 250/500, Submit by 18 Sep (MEDIUM)
```
Shows engine correctly separates GEM (2.6) vs TRAP/WORKABLE (5.0): delta = 2.4 points, 120 submissions gap.
**PASS**

### 4. Vault artifacts
```
my info/projects/sih26/research/ps-evaluation/
├── 00-master-research-index.md      (121 lines, 6.0K)
├── 01-team-thinking-patterns.md      (52 lines, 2.5K)
├── 02-six-bucket-framework.md        (95 lines, 3.4K)
└── 03-qa-verification.md             (this file)
plus PDF: my info/projects/sih26/ppt/SIH_2026_College_to_Finale_Guide.pdf
```
**PASS**

### 5. Skill folder structure
```
ps-evaluator/
├── SKILL.md (8790 bytes, frontmatter + routing)
├── scripts/evaluate.py (22K, no deps, deterministic)
└── references/ (3 md, mirrors vault)
```
**PASS**

### 6. Determinism
Script uses no network, no API key, pure table lookup + arithmetic. Reruns produce identical output.
**PASS**

## How to use in any future SIH session

```python
skill_view(name='ps-evaluator')                # load docs
skill_view(name='ps-evaluator', file_path='scripts/evaluate.py')  # read engine
skill_view(name='ps-evaluator', file_path='references/00-master-research-index.md')
```

```bash
# CLI
python3 ~/.hermes/profiles/sih26/skills/ps-evaluator/scripts/evaluate.py              # sample
python3 ~/.hermes/profiles/sih26/skills/ps-evaluator/scripts/evaluate.py --interactive
python3 ~/.hermes/profiles/sih26/skills/ps-evaluator/scripts/evaluate.py --from-json batch.json
```

## Calibration notes
- Niche suppression (GRATK/ayush/bhashini/trips) caps genai hype: 10→5 keyword, 10→3 buzz, prefers HARD ease signals.
- Without this, SIH26045 would falsely score CLS 5.15 (bloodbath) instead of true 2.6 (hidden gem).
- Quality 8.3 derived from 9.0*0.3 + 7.0*0.25 + 9.5*0.2 + 8.5*0.15 + 6.75*0.1 = 8.30 exact.
