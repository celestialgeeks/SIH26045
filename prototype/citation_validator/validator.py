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
    CitationPattern("Patents Act Sec 3(e)", r"Patents Act,?\s*Sec\.?\s*3\(e\)", "Sec 3(e)", "India"),
    CitationPattern("Patents Act Sec 3(i)", r"Patents Act,?\s*Sec\.?\s*3\(i\)", "Sec 3(i)", "India"),
    CitationPattern("Patents Act Sec 3(j)", r"Patents Act,?\s*Sec\.?\s*3\(j\)", "Sec 3(j)", "India"),
    CitationPattern("Patents Act Sec 3(k)", r"Patents Act,?\s*Sec\.?\s*3\(k\)", "Sec 3(k)", "India"),
    CitationPattern("Patents Act Sec 2(1)(j)", r"Patents Act,?\s*Section\s*2\(1\)\(j\)", "Section 2(1)(j)", "India"),
    CitationPattern("Patents Act Sec 2(1)(ja)", r"Patents Act,?\s*Sec\.?\s*2\(1\)\(ja\)", "Sec 2(1)(ja)", "India"),
    CitationPattern("Patents Act Sec 10", r"Patents Act,?\s*Sec\.?\s*10\b", "Sec 10", "India"),
    CitationPattern("Patents Act Sec 11A", r"Patents Act,?\s*Sec\.?\s*11A\b", "Sec 11A", "India"),
    CitationPattern("Patents Act Sec 25(1)(k)", r"Patents Act,?\s*Sec\.?\s*25\(1\)\(k\)", "Sec 25(1)(k)", "India"),
    CitationPattern("Patents Rules 2024 Rule 12", r"Patents \(Amendment\) Rules 2024,?\s*Rule\s*12\b", "Rule 12", "India"),
    CitationPattern("Patents Rules Rule 20", r"Patents Rules?,?\s*Rule\s*20\b", "Rule 20", "India"),
    CitationPattern("Patents Rules Rule 122E", r"Patents Rules?,?\s*Rule\s*122E\b", "Rule 122E", "India"),
    CitationPattern("BD Act Sec 3(2)", r"Biological Diversity \(Amendment\)? Act 2002,?\s*Sec\.?\s*3\(2\)", "Sec 3(2)", "India"),
    CitationPattern("BD Amendment Act 2023 Sec 6", r"Biological Diversity \(Amendment\) Act 2023,?\s*Sec\.?\s*6\b", "Sec 6", "India"),
    CitationPattern("BD Amendment Act 2023 Sec 5", r"Biological Diversity \(Amendment\) Act 2023,?\s*Sec\.?\s*5\b", "Sec 5", "India"),
    CitationPattern("BD Rules 2024 Rule 4", r"Biological Diversity Rules 2024,?\s*Rule\s*4\b", "Rule 4", "India"),
    CitationPattern("BD Rules 2024 Reg 4", r"Biological Diversity Rules 2024,?\s*Reg\.?\s*4\b", "Reg 4", "India"),
    CitationPattern("BD Rules 2024 Rule 12", r"Biological Diversity Rules 2024,?\s*Rule\s*12\b", "Rule 12", "India"),
    CitationPattern("BD Rules 2024 Form 1", r"Biological Diversity Rules 2024,?\s*Form\s*1\b", "Form 1", "India"),
    CitationPattern("BD Rules 2024 Form 2", r"Biological Diversity Rules 2024,?\s*Form\s*2\b", "Form 2", "India"),
    CitationPattern("GRATK Art 3", r"GRATK Treaty 2024,?\s*Art\.?\s*3\b", "Art 3", "International"),
    CitationPattern("GRATK Art 9", r"GRATK Treaty 2024,?\s*Art\.?\s*9\b", "Art 9", "International"),
    CitationPattern("GRATK Article 5.2", r"GRATK,?\s*Article\s*5\.2\b", "Article 5.2", "International"),
    CitationPattern("D&C Act Sec 3(a)", r"Drugs & Cosmetics Act 1940,?\s*Sec\.?\s*3\(a\)", "Sec 3(a)", "India"),
    CitationPattern("D&C Act Sec 3(aaa)", r"Drugs & Cosmetics Act 1940,?\s*Sec\.?\s*3\(aaa\)", "Sec 3(aaa)", "India"),
    CitationPattern("D&C Act Sec 7A", r"Drugs & Cosmetics Act 1940,?\s*Section\s*7A\b", "Section 7A", "India"),
    CitationPattern("D&C Act First Schedule", r"Drugs & Cosmetics Act 1940,?\s*First Schedule", "First Schedule", "India"),
    CitationPattern("NDCT Rules 2019 Rule 122E", r"NDCT Rules 2019,?\s*Rule\s*122E\b", "Rule 122E", "India"),
    CitationPattern("NDCT Rules 2019 Rule 21", r"NDCT Rules 2019,?\s*Rule\s*21\b", "Rule 21", "India"),
    CitationPattern("FSSAI Aahar Reg 5", r"FSSAI Ayurveda Aahar Regulations 2022,?\s*Reg\.?\s*5\b", "Reg 5", "India"),
    CitationPattern("FSSAI Aahar Reg 12", r"FSSAI Ayurveda Aahar Regulations 2022,?\s*Reg\.?\s*12\b", "Reg 12", "India"),
    CitationPattern("FSSAI Regulation 12", r"FSSAI,?\s*Regulation\s*12\b", "Regulation 12", "India"),
    CitationPattern("Schedule T GMP", r"Schedule T,?\s*GMP", "Schedule T", "India"),
    CitationPattern("TRIPS Art 27.3(b)", r"TRIPS,?\s*Art\.?\s*27\.3\(b\)", "Art 27.3(b)", "International"),
    CitationPattern("TRIPS Article 31", r"TRIPS Agreement,?\s*Article\s*31\b", "Article 31", "International"),
    CitationPattern("TRIPS Art 22", r"TRIPS,?\s*Art\.?\s*22\b", "Art 22", "International"),
    CitationPattern("Nagoya Art 15", r"Nagoya Protocol,?\s*Art\.?\s*15\b", "Art 15", "International"),
    CitationPattern("Nagoya Art 5", r"Nagoya Protocol,?\s*Art\.?\s*5\b", "Art 5", "International"),
    CitationPattern("CBD Art 8(j)", r"CBD,?\s*Art\.?\s*8\(j\)", "Art 8(j)", "International"),
    CitationPattern("CBD Art 15", r"CBD,?\s*Art\.?\s*15\b", "Art 15", "International"),
    CitationPattern("PCT Art 4", r"PCT,?\s*Art\.?\s*4\b", "Art 4", "International"),
    CitationPattern("PCT Article 22", r"Patent Cooperation Treaty,?\s*Article\s*22\b", "Article 22", "International"),
    CitationPattern("PCT Art 39", r"PCT,?\s*Art\.?\s*39\b", "Art 39", "International"),
    CitationPattern("Madrid Art 2", r"Madrid Protocol,?\s*Art\.?\s*2\b", "Art 2", "International"),
    CitationPattern("Hague Art 3", r"Hague Agreement,?\s*Art\.?\s*3\b", "Art 3", "International"),
    CitationPattern("GI Act Sec 2(e)", r"Geographical Indications Act 1999,?\s*Sec\.?\s*2\(e\)", "Sec 2(e)", "India"),
    CitationPattern("GI Act Sec 11", r"Geographical Indications Act 1999,?\s*Sec\.?\s*11\b", "Sec 11", "India"),
    CitationPattern("TM Act Sec 9", r"Trade Marks Act 1999,?\s*Sec\.?\s*9\b", "Sec 9", "India"),
    CitationPattern("TM Act Sec 11", r"Trade Marks Act 1999,?\s*Sec\.?\s*11\b", "Sec 11", "India"),
    CitationPattern("TM Act Sec 21", r"Trade Marks Act 1999,?\s*Sec\.?\s*21\b", "Sec 21", "India"),
    CitationPattern("TM Act Sec 29", r"Trade Marks Act 1999,?\s*Sec\.?\s*29\b", "Sec 29", "India"),
    CitationPattern("Designs Act Sec 2(d)", r"Designs Act 2000,?\s*Sec\.?\s*2\(d\)", "Sec 2(d)", "India"),
    CitationPattern("Designs Act Sec 11", r"Designs Act 2000,?\s*Sec\.?\s*11\b", "Sec 11", "India"),
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
            "jurisdiction_ok": True
        })
        if not valid:
            all_valid = False
    
    legal_advice_triggers = [
        "draft my patent", "write claim", "file application", 
        "legal opinion", "should i patent", "can you file",
        "here is your patent claim", "patent claim:", "claim 1.",
        "draft a claim", "write a claim", "prepare claim",
        "draft patent claim", "draft patent claims", "draft claims",
        "cannot draft patent", "cannot write claim", "cannot prepare claim"
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
        "abstain_present": has_abstain,
        "pattern_count": len(CITATION_PATTERNS)
    }

if __name__ == "__main__":
    test_answer = """
    Chyavanprash is a classical formulation under the First Schedule of the Drugs & Cosmetics Act 1940 [CIT: Drugs & Cosmetics Act 1940, First Schedule].
    Section 3(p) of the Patents Act bars patents on traditional knowledge [CIT: Patents Act, Sec 3(p)].
    Sec 3(e) mere admixture also applies [CIT: Patents Act, Sec 3(e)].
    For export, GRATK Treaty 2024 Article 9 sanity check [CIT: GRATK Treaty 2024, Art 9].
    """
    result = validate_answer(test_answer, "Both")
    import json
    print(json.dumps(result, indent=2))
