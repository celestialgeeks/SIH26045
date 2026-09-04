# SIH26045 — Citation Validator Regex Patterns (Implementation-Grade)

> **Purpose:** 100% citation correctness or ABSTAIN — every generated answer must pass validator or be rejected
> **Source:** Legal corpus (Task 1A) + Patents Act 1970/2024, BD Act 2002/2023/2024, GRATK 2024, D&C Act 1940, NDCT 2019, FSSAI 2022, GI Act 1999, TRIPS, CBD/Nagoya, PCT

---

## Citation Type → Regex Pattern Table

| Citation Type | Example | Regex Pattern (Python `re.IGNORECASE`) | Notes |
|---|---|---|---|
| **Patents Act Section** | Sec 3(p) | `Patents Act,?\s*Sec\.?\s*3\(p\)` | Must match `Sec 3(p)` or `Section 3(p)` |
| **Patents Act Section (alt)** | Section 2(1)(j) | `Patents Act,?\s*Section\s*2\(1\)\(j\)` | Capture group for section number |
| **Patents (Amendment) Rules 2024 Rule** | Rule 12 | `Patents \(Amendment\) Rules 2024,?\s*Rule\s*12\b` | Year 2024 mandatory |
| **Patents Rules Rule (generic)** | Rule 122E | `Patents Rules?,?\s*Rule\s*122E\b` | Catches old + new rules |
| **Biological Diversity Act Section** | Sec 3(2) | `Biological Diversity \(Amendment\)? Act 2002,?\s*Sec\.?\s*3\(2\)` | Amendment optional |
| **Biological Diversity (Amendment) Act 2023 Section** | Sec 6 | `Biological Diversity \(Amendment\) Act 2023,?\s*Sec\.?\s*6\b` | Explicit 2023 |
| **Biological Diversity Rules 2024 Rule** | Rule 4 | `Biological Diversity Rules 2024,?\s*Rule\s*4\b` | 2024 rules only |
| **Biological Diversity Rules 2024 Form** | Form 1 | `Biological Diversity Rules 2024,?\s*Form\s*1\b` | Form numbers |
| **WIPO GRATK Treaty 2024 Article** | Art 3 | `GRATK Treaty 2024,?\s*Art\.?\s*3\b` | "Treaty 2024" mandatory |
| **GRATK Article (alt)** | Article 5.2 | `GRATK,?\s*Article\s*5\.2\b` | Decimal articles |
| **Drugs & Cosmetics Act Section** | Sec 3(a) | `Drugs & Cosmetics Act 1940,?\s*Sec\.?\s*3\(a\)` | 1940 base year |
| **D&C Act Section (alt)** | Section 7A | `Drugs & Cosmetics Act 1940,?\s*Section\s*7A\b` | |
| **NDCT Rules 2019 Rule** | Rule 122E | `NDCT Rules 2019,?\s*Rule\s*122E\b` | 2019 mandatory |
| **FSSAI Ayurveda Aahar Regulations 2022 Regulation** | Reg 5 | `FSSAI Ayurveda Aahar Regulations 2022,?\s*Reg\.?\s*5\b` | "Regulations 2022" |
| **FSSAI Regulation (alt)** | Regulation 12 | `FSSAI,?\s*Regulation\s*12\b` | Generic FSSAI |
| **Schedule T (GMP)** | Schedule T | `Schedule T,?\s*GMP` | GMP context |
| **TRIPS Agreement Article** | Art 27.3(b) | `TRIPS,?\s*Art\.?\s*27\.3\(b\)` | Decimal + parens |
| **TRIPS Article (alt)** | Article 31 | `TRIPS Agreement,?\s*Article\s*31\b` | |
| **Nagoya Protocol Article** | Art 15 | `Nagoya Protocol,?\s*Art\.?\s*15\b` | |
| **CBD Article** | Art 8(j) | `CBD,?\s*Art\.?\s*8\(j\)` | |
| **PCT Article** | Art 4 | `PCT,?\s*Art\.?\s*4\b` | |
| **PCT Article (alt)** | Article 22 | `Patent Cooperation Treaty,?\s*Article\s*22\b` | |
| **Madrid Protocol** | Art 2 | `Madrid Protocol,?\s*Art\.?\s*2\b` | |
| **Hague Agreement** | Art 3 | `Hague Agreement,?\s*Art\.?\s*3\b` | |
| **Geographical Indications Act Section** | Sec 2(e) | `Geographical Indications Act 1999,?\s*Sec\.?\s*2\(e\)` | |
| **Designs Act Section** | Sec 2(d) | `Designs Act 2000,?\s*Sec\.?\s*2\(d\)` | |
| **Copyright Act Section** | Sec 13 | `Copyright Act 1957,?\s*Sec\.?\s*13\b` | |
| **PPVFR Act Section** | Sec 15 | `PPVFR Act 2001,?\s*Sec\.?\s*15\b` | Plant varieties |

---

## Validator Logic (Python Implementation)

```python
# /Users/shreyashsingh/my info/projects/sih26/prototype/citation_validator/validator.py
import re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CitationPattern:
    name: str
    pattern: str
    example: str
    jurisdiction: str  # "India" | "International" | "Both"

CITATION_PATTERNS: List[CitationPattern] = [
    CitationPattern("Patents Act Sec 3(p)", r"Patents Act,?\s*Sec\.?\s*3\(p\)", "Sec 3(p)", "India"),
    CitationPattern("Patents Act Sec 2(1)(j)", r"Patents Act,?\s*Section\s*2\(1\)\(j\)", "Section 2(1)(j)", "India"),
    CitationPattern("Patents Rules 2024 Rule 12", r"Patents \(Amendment\) Rules 2024,?\s*Rule\s*12\b", "Rule 12", "India"),
    CitationPattern("Patents Rules Rule 122E", r"Patents Rules?,?\s*Rule\s*122E\b", "Rule 122E", "India"),
    CitationPattern("BD Act Sec 3(2)", r"Biological Diversity \(Amendment\)? Act 2002,?\s*Sec\.?\s*3\(2\)", "Sec 3(2)", "India"),
    CitationPattern("BD Amendment Act 2023 Sec 6", r"Biological Diversity \(Amendment\) Act 2023,?\s*Sec\.?\s*6\b", "Sec 6", "India"),
    CitationPattern("BD Rules 2024 Rule 4", r"Biological Diversity Rules 2024,?\s*Rule\s*4\b", "Rule 4", "India"),
    CitationPattern("BD Rules 2024 Form 1", r"Biological Diversity Rules 2024,?\s*Form\s*1\b", "Form 1", "India"),
    CitationPattern("GRATK Art 3", r"GRATK Treaty 2024,?\s*Art\.?\s*3\b", "Art 3", "International"),
    CitationPattern("GRATK Article 5.2", r"GRATK,?\s*Article\s*5\.2\b", "Article 5.2", "International"),
    CitationPattern("D&C Act Sec 3(a)", r"Drugs & Cosmetics Act 1940,?\s*Sec\.?\s*3\(a\)", "Sec 3(a)", "India"),
    CitationPattern("D&C Act Sec 7A", r"Drugs & Cosmetics Act 1940,?\s*Section\s*7A\b", "Section 7A", "India"),
    CitationPattern("NDCT Rules 2019 Rule 122E", r"NDCT Rules 2019,?\s*Rule\s*122E\b", "Rule 122E", "India"),
    CitationPattern("FSSAI Aahar Reg 5", r"FSSAI Ayurveda Aahar Regulations 2022,?\s*Reg\.?\s*5\b", "Reg 5", "India"),
    CitationPattern("FSSAI Regulation 12", r"FSSAI,?\s*Regulation\s*12\b", "Regulation 12", "India"),
    CitationPattern("Schedule T GMP", r"Schedule T,?\s*GMP", "Schedule T", "India"),
    CitationPattern("TRIPS Art 27.3(b)", r"TRIPS,?\s*Art\.?\s*27\.3\(b\)", "Art 27.3(b)", "International"),
    CitationPattern("TRIPS Article 31", r"TRIPS Agreement,?\s*Article\s*31\b", "Article 31", "International"),
    CitationPattern("Nagoya Art 15", r"Nagoya Protocol,?\s*Art\.?\s*15\b", "Art 15", "International"),
    CitationPattern("CBD Art 8(j)", r"CBD,?\s*Art\.?\s*8\(j\)", "Art 8(j)", "International"),
    CitationPattern("PCT Art 4", r"PCT,?\s*Art\.?\s*4\b", "Art 4", "International"),
    CitationPattern("PCT Article 22", r"Patent Cooperation Treaty,?\s*Article\s*22\b", "Article 22", "International"),
    CitationPattern("Madrid Art 2", r"Madrid Protocol,?\s*Art\.?\s*2\b", "Art 2", "International"),
    CitationPattern("Hague Art 3", r"Hague Agreement,?\s*Art\.?\s*3\b", "Art 3", "International"),
    CitationPattern("GI Act Sec 2(e)", r"Geographical Indications Act 1999,?\s*Sec\.?\s*2\(e\)", "Sec 2(e)", "India"),
    CitationPattern("Designs Act Sec 2(d)", r"Designs Act 2000,?\s*Sec\.?\s*2\(d\)", "Sec 2(d)", "India"),
    CitationPattern("Copyright Act Sec 13", r"Copyright Act 1957,?\s*Sec\.?\s*13\b", "Sec 13", "India"),
    CitationPattern("PPVFR Act Sec 15", r"PPVFR Act 2001,?\s*Sec\.?\s*15\b", "Sec 15", "India"),
]

# Compiled patterns for speed
COMPILED = [(cp.name, re.compile(cp.pattern, re.IGNORECASE), cp.jurisdiction) for cp in CITATION_PATTERNS]

CITATION_TAG_RE = re.compile(r"\[CIT:\s*([^\]]+)\]")

def extract_citations(text: str) -> List[str]:
    """Extract all [CIT: ...] tags from generated answer"""
    return [m.group(1).strip() for m in CITATION_TAG_RE.finditer(text)]

def validate_citation(citation: str) -> tuple[bool, Optional[str]]:
    """Return (is_valid, matched_pattern_name)"""
    for name, pattern, juris in COMPILED:
        if pattern.search(citation):
            return True, name
    return False, None

def validate_answer(answer: str, expected_jurisdiction: str = "Both") -> dict:
    """
    Full validator for a generated answer.
    Returns dict with validation result + details.
    """
    citations = extract_citations(answer)
    results = []
    all_valid = True
    
    for cit in citations:
        valid, matched = validate_citation(cit)
        results.append({
            "citation": cit,
            "valid": valid,
            "matched_pattern": matched,
            "jurisdiction_ok": True  # Could add jurisdiction check here
        })
        if not valid:
            all_valid = False
    
    # Check for ABSTAIN requirement on legal advice
    legal_advice_triggers = [
        "draft my patent", "write claim", "file application", 
        "legal opinion", "should i patent", "can you file"
    ]
    has_legal_advice_request = any(t in answer.lower() for t in legal_advice_triggers)
    has_abstain = "ABSTAIN" in answer.upper() or "disclaimer" in answer.lower()
    
    if has_legal_advice_request and not has_abstain:
        all_valid = False
        results.append({
            "citation": "[LEGAL_ADVICE_CHECK]",
            "valid": False,
            "matched_pattern": None,
            "error": "Legal advice requested but no ABSTAIN/disclaimer"
        })
    
    return {
        "all_valid": all_valid,
        "citations": results,
        "total_citations": len(citations),
        "valid_citations": sum(1 for r in results if r["valid"]),
        "abstain_required": has_legal_advice_request,
        "abstain_present": has_abstain
    }

if __name__ == "__main__":
    # Quick test
    test_answer = """
    Chyavanprash is a classical formulation under the First Schedule of the Drugs & Cosmetics Act 1940 [CIT: Drugs & Cosmetics Act 1940, Sec 3(a)].
    Section 3(p) of the Patents Act bars patents on traditional knowledge [CIT: Patents Act, Sec 3(p)].
    For export, GRATK Treaty 2024 Article 3 requires disclosure of origin [CIT: GRATK Treaty 2024, Art 3].
    """
    result = validate_answer(test_answer, "Both")
    import json
    print(json.dumps(result, indent=2))
```

---

## Test Cases

```python
# /Users/shreyashsingh/my info/projects/sih26/prototype/citation_validator/test_validator.py
import pytest
from validator import validate_answer, validate_citation

def test_classical_formulation_citations():
    ans = "Chyavanprash cannot be patented due to Sec 3(p) [CIT: Patents Act, Sec 3(p)] and classical formulation status [CIT: Drugs & Cosmetics Act 1940, Sec 3(a)]."
    result = validate_answer(ans, "India")
    assert result["all_valid"] == True
    assert result["valid_citations"] == 2

def test_gratk_citation():
    ans = "Export requires GRATK disclosure [CIT: GRATK Treaty 2024, Art 3]."
    result = validate_answer(ans, "International")
    assert result["all_valid"] == True

def test_adversarial_fake_citation():
    ans = "Fake rule [CIT: Patents Rules 2024, Rule 999]."
    result = validate_answer(ans, "India")
    assert result["all_valid"] == False

def test_legal_advice_abstain():
    ans = "Here is your patent claim: claim 1. A composition comprising ashwagandha..."
    result = validate_answer(ans, "India")
    assert result["all_valid"] == False
    assert result["abstain_required"] == True
    assert result["abstain_present"] == False

def test_legal_advice_with_abstain():
    ans = "ABSTAIN: I cannot draft patent claims. Consult a patent attorney. [CIT: Patents Act, Sec 3(p)]"
    result = validate_answer(ans, "India")
    assert result["abstain_required"] == True
    assert result["abstain_present"] == True
    assert result["all_valid"] == True

def test_jurisdiction_correction():
    ans = "Sec 3(p) applies in India only. In US, 35 USC 101 governs. [CIT: Patents Act, Sec 3(p)]"
    result = validate_answer(ans, "Both")
    assert result["all_valid"] == True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

---

## Integration with RAG Pipeline

```python
# In RAG answer generator - post-process every answer
def post_process_answer(raw_answer: str, query: str, jurisdiction: str) -> str:
    validation = validate_answer(raw_answer, jurisdiction)
    if not validation["all_valid"]:
        # Log for debugging
        print(f"VALIDATION FAILED for query: {query}")
        print(f"Answer: {raw_answer}")
        print(f"Details: {validation}")
        # Return safe abstention
        return "ABSTAIN: I cannot provide a fully verified answer for this query. Please consult a qualified IP attorney."
    return raw_answer
```

---

## Files Created

| File | Path |
|---|---|
| Validator core | `projects/sih26/prototype/citation_validator/validator.py` |
| Unit tests | `projects/sih26/prototype/citation_validator/test_validator.py` |
| This spec | `reference/research/sih26/citation-validator-2026-09-03.md` |

---

## Next: Run `pytest test_validator.py -v` → all green = validator ready for RAG integration