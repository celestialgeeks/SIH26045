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

def test_bd_rules_2024_form():
    ans = "ABS requires Form 1 [CIT: Biological Diversity Rules 2024, Form 1]."
    result = validate_answer(ans, "India")
    assert result["all_valid"] == True

def test_ndct_rules():
    ans = "Clinical trial under Rule 122E [CIT: NDCT Rules 2019, Rule 122E]."
    result = validate_answer(ans, "India")
    assert result["all_valid"] == True

def test_fssai_aahar():
    ans = "Ayurveda Aahar regulated under Reg 5 [CIT: FSSAI Ayurveda Aahar Regulations 2022, Reg 5]."
    result = validate_answer(ans, "India")
    assert result["all_valid"] == True

def test_trips_article():
    ans = "TRIPS Art 27.3(b) allows exclusions [CIT: TRIPS, Art 27.3(b)]."
    result = validate_answer(ans, "International")
    assert result["all_valid"] == True

def test_pct_article():
    ans = "PCT filing deadline Art 22 [CIT: Patent Cooperation Treaty, Article 22]."
    result = validate_answer(ans, "International")
    assert result["all_valid"] == True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])