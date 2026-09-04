#!/usr/bin/env python3
"""
SIH 2026 v2 Evaluator — Raw-data-driven, fully reproducible
Fixes v1 issues:
- ORG fuzzy bug: MDoNER mis-scored as MoES (9 instead of ~3.5)
- Quality sub-scores were templated; now derived from raw PS text features
- Dataset score now uses dataset_link + description signals
- Ministry fit now uses PS-count-per-org (sharp vs diffuse intent) + mandate match
- Differentiation now measures headroom per PS text, not generic
- Demoability/feasibility differentiated by hardware/data/infra mentions
CLS still uses ps-evaluator's 5-factor formula but with corrected lookups.
WPS = Quality*0.40 + (10-CLS)*0.25 + Diff*0.15 + Dataset*0.10 + Demo*0.05 + MFit*0.05
Quality = Innov*0.30 + Feas*0.25 + Impact*0.20 + DemoAbility*0.15 + TeamFit*0.10
"""
import json, re, pathlib
from collections import Counter

RAW = "/tmp/sih260_all_software_full.json"
OUT_JSON = "/tmp/sih260_all_evaluated_v2.json"
OUT_CSV = "/tmp/sih260_all_evaluated_v2.csv"

# === Load ===
with open(RAW) as f:
    raw = json.load(f)

# === Org PS counts (for ministry fit sharpness) ===
org_counts = Counter([r["org"].strip() for r in raw])

# === Corrected Org score table (explicit, no fuzzy bleed) ===
# Key: normalized org string -> score. We match by exact substring, longest first.
ORG_TABLE = [
    ("ministry of earth sciences", 9), ("moes", 9),
    ("national technical research organisation", 8), ("ntro", 8),
    ("aicte", 10), ("all india council for technical education", 10),
    ("indian space research organisation", 7), ("isro", 7),
    ("ministry of home affairs", 7),
    ("bharat electronics limited", 6),
    ("drdo", 6),
    ("ministry of rural development", 4),
    ("ministry of consumer affairs", 3),
    ("ministry of ayush", 2),
    ("ministry of development of north eastern region", 3.5), ("mdoner", 3.5),
    ("governmcnt of jharkhand", 4), ("government of jharkhand", 4),
    ("government of maharashtra", 6),
    ("ministry of steel", 3),
    ("ministry of coal", 4),
    ("ministry of cooperation", 4),
    ("ministry of msme", 2),
    ("ministry of social justice", 6),
    ("ministry of fisheries", 4),
    ("ministry of petroleum", 5),
    ("oil india limited", 5),
    ("mangalore refinery", 5),
    ("egreen quanta", 5),
    ("autodesk", 5),
    ("mathworks", 4),
    ("mopsi", 4), ("mospi", 4),
    ("ministry of mines", 4),
    ("ministry of defence", 6),
    ("department of land resources", 3),
]

THEME_SCORES = {
    "miscellaneous": 10, "smart automation": 10, "disaster management": 9,
    "blockchain & cybersecurity": 8, "heritage & culture": 5, "fitness & sports": 5,
    "travel & tourism": 5, "transportation & logistics": 5, "medtech / biotech / healthtech": 4,
    "space technology": 4, "smart education": 4, "agriculture, foodtech & rural development": 3,
    "smart vehicles": 3, "renewable / sustainable energy": 2, "clean & green technology": 1,
    "toys & games": 1,
}

# === Helpers ===
def norm(s): return (s or "").strip().lower()

def org_score(org, dept):
    text = norm(org + " " + dept)
    # longest key first
    for key, score in sorted(ORG_TABLE, key=lambda x: len(x[0]), reverse=True):
        if key in text:
            return float(score), key
    # fallback: use ps-count heuristic: many PS = diffuse = higher CLS
    # counts: low count (1-4) => 3-4, medium (5-10) => 6, high (17-27) => 8-10
    cnt = org_counts.get(org.strip(), 5)
    if cnt <= 4: return 3.5, f"(fallback count={cnt})"
    if cnt <= 9: return 5.5, f"(fallback count={cnt})"
    if cnt <= 17: return 7.0, f"(fallback count={cnt})"
    return 9.0, f"(fallback count={cnt})"

def theme_score(theme):
    t = norm(theme)
    for k, v in THEME_SCORES.items():
        if k == t:
            return float(v), k
    return 5.0, "(default)"

# CLS sub-scorers (reuse evaluate.py logic but with fixed org)
import sys
sys.path.insert(0, "/Users/shreyashsingh/.hermes/profiles/sih26/skills/ps-evaluator/scripts")
from evaluate import compute_cls as orig_compute_cls, PSInput, evaluate, THEME_SCORES as THEME2, ORG_SCORES, KEYWORD_HYPE, NICHE_DOMAIN_KEYWORDS, NICHE_DOMAIN_SIGNALS, PERCEIVED_EASE, BUZZ_2026

def compute_cls_v2(ps):
    # Theme
    ts, tk = theme_score(ps.theme)
    # Org corrected
    os, ok = org_score(ps.org, ps.department)
    combined = ps.title + " " + ps.description
    cnorm = norm(combined)
    is_niche = any(sig in cnorm for sig in NICHE_DOMAIN_SIGNALS)
    # Keyword
    if is_niche:
        niche_hits = [(k, v) for k, v in NICHE_DOMAIN_KEYWORDS.items() if k in cnorm]
        generic_non_ai_hits = [(k, v) for k, v in KEYWORD_HYPE.items() if k in cnorm and k not in ("ai","rag","llm","genai","chatbot","ayush","ayurveda","gratk","nagoya","phytopharmaceutical","metrology","ulpin","lidar")]
        suppressed_ai_score = 5.0 if any(k in cnorm for k in ("rag","ai","chatbot","llm","genai")) else None
        niche_low = max((v for _, v in niche_hits), default=None)
        candidates = []
        if generic_non_ai_hits:
            candidates.append(max(v for _, v in generic_non_ai_hits))
        if suppressed_ai_score is not None:
            candidates.append(suppressed_ai_score)
        if niche_low is not None and niche_low < 5:
            if not candidates or max(candidates) < 5:
                candidates.append(niche_low)
        if candidates:
            ks = max(candidates)
            parts=[]
            if generic_non_ai_hits: parts.append(", ".join(f"{k}:{v}" for k,v in generic_non_ai_hits[:2]))
            if suppressed_ai_score is not None: parts.append("rag/ai(suppressed):5")
            kk = " + ".join(parts) + " (NICHE-SUPPRESSED)" if is_niche else ", ".join(parts)
        else:
            ks=5.0; kk="(none, niche domain)"
    else:
        generic_hits=[(k,v) for k,v in KEYWORD_HYPE.items() if k in cnorm]
        if generic_hits:
            ks=max(v for _,v in generic_hits)
            kk=", ".join(f"{k}:{v}" for k,v in generic_hits[:3])
        else:
            ks=5.0; kk="(none)"
    # Perceived ease
    perceived_hits=[(k,v) for k,v in PERCEIVED_EASE.items() if k in cnorm]
    if is_niche:
        hard=[(k,v) for k,v in perceived_hits if v<=3]
        easy=[(k,v) for k,v in perceived_hits if v>=7]
        if hard:
            ps_score=min(v for _,v in hard); pk=", ".join(f"{k}:{v}" for k,v in hard[:2])+" (HARD)"
        elif easy:
            ps_score=max(v for _,v in easy); pk=", ".join(f"{k}:{v}" for k,v in easy[:2])+" (EASY)"
        else:
            ps_score=5.0; pk="(no hard/easy hit)"
    else:
        ps_score=max((v for _,v in perceived_hits), default=5.0)
        pk=", ".join(f"{k}:{v}" for k,v in perceived_hits[:2]) if perceived_hits else "(none)"
    # Buzz
    buzz_hits=[(k,v) for k,v in BUZZ_2026.items() if k in cnorm]
    if is_niche:
        capped=[]
        for k,v in buzz_hits:
            if k in ("genai","rag","agentic ai","on-device ai"): capped.append((k,3))
            else: capped.append((k,v))
        bs=max((v for _,v in capped), default=3.0) if capped else 3.0
        bk=", ".join(f"{k}:{v}" for k,v in capped[:2])+" (CAPPED)" if capped else "(none, niche=>3)"
    else:
        bs=max((v for _,v in buzz_hits), default=4.0) if buzz_hits else 4.0
        bk=", ".join(f"{k}:{v}" for k,v in buzz_hits[:2]) if buzz_hits else "(none)"
    cls=round(ts*0.25 + os*0.20 + ks*0.25 + ps_score*0.20 + bs*0.10, 2)
    breakdown={"theme":{"score":ts,"key":tk,"weight":"25%"},"org":{"score":os,"key":ok,"weight":"20%"},"keyword":{"score":ks,"key":kk,"weight":"25%"},"perceived_ease":{"score":ps_score,"key":pk,"weight":"20%"},"buzz_2026":{"score":bs,"key":bk,"weight":"10%"},"raw_cls":cls}
    return cls, breakdown

# === Text-derived Quality sub-scores ===
# We derive 9 scores from raw text signals, each 1-10

HARD_TECH = ["quantum","knowledge graph","neo4j","bhashini","tkdl","gratk","nagoya","ulpin","lidar","photogrammetry","gis","satellite imagery","isro","bhuvan","digital twin","generative ai","rag","vector database","blockchain","iot","sensor","drone","robotics","computer vision","nlp","multilingual","agentic"]
EASY_PORTAL = ["portal","dashboard","website","mobile app","attendance","proctoring","scan","ocr","extract text","verification system","cataloging"]
DATASET_SIGNALS_PUBLIC = ["dataset link","open data","public dataset","api available","kaggle","data.gov.in","isro bhuvan","imd","satellite imagery","ulpin","land records","tkdl"]
HARD_INFRA = ["quantum hardware","lidar sensor","satellite launch","field collection","hardware kit","₹","cost >","drone hardware","underwater","polar expedition","antarctic","marine debris","autonomous vehicle","lidar mapping","electronic warfare"]
BENEFICIARY_SCALE = {"nationwide":9,"national":8,"pan-india":8,"all states":8,"farmers":7,"students":6,"citizens":7,"healthcare":7,"disaster":8,"isro":7,"ntro":7,"mha":8,"consumer":7,"rural":7}
DEMO_HARD = ["hardware","sensor","satellite","drone","underwater","polar","lidar","quantum processor","on-device","electronic warfare","forensic","real-time gis","3d cadastre"]
DIFF_TWIST = ["knowledge graph","citation","source-cited","bhashini","persona switch","citizen mode","whistleblower","cross-system","reconciliation","physical reference","coin","scale from photo","e-commerce mirror","safety abstention","uncertain","neo4j","graph database"]

def score_innovation(ps):
    text = norm(ps.title + " " + ps.description)
    # Base on theme + hard-tech density
    score = 5.0
    hard = sum(1 for k in HARD_TECH if k in text)
    easy = sum(1 for k in EASY_PORTAL if k.lower() in text)
    # Hard tech pushes innovation up, pure portal pushes down
    if hard >= 4: score = 8.0
    elif hard >= 2: score = 6.5
    elif easy >= 3 and hard == 0: score = 4.0
    elif easy >= 2: score = 5.0
    else: score = 5.5
    # Niche domain bonus (Ayush/GRATK/ULPIN) = high innovation headroom if you connect dots
    if any(s in text for s in ["gratk","nagoya","phytopharmaceutical","ulpin","tkdl","bhashini","jurisdiction","treaty","wipo","trips"]):
        score = min(9.0, score + 1.5)
    # Quantum / novel algo bonus
    if "quantum" in text: score = min(9.0, score + 1.0)
    if "digital twin" in text: score = min(8.5, score + 0.8)
    # Simple CRUD without AI = low
    if "student innovation" in norm(ps.title) and hard == 0:
        score = max(4.0, min(score, 5.0))
    return round(max(1, min(10, score)), 1)

def score_feasibility(ps):
    text = norm(ps.title + " " + ps.description)
    # Start feasible, subtract for hard infra
    score = 7.0
    # Hard infra penalties
    if any(k in text for k in ["quantum","lidar 3d","photogrammetry","ulpin 3d cadastre","electronic warfare","underwater","polar expedition","autonomous vehicle collision avoidance","lidar mapping","forensic","cryptographic discovery","blockchain"]):
        score -= 1.5
    if "satellite imagery" in text and "isro" in norm(ps.org):
        score -= 0.5  # ISRO data is accessible but processing heavy
    if any(k in text for k in ["real-time gis","nationwide land stack","multi-radar nowcasting","hydrodynamic modelling"]):
        score -= 1.0
    if "student innovation" in norm(ps.title):
        score += 1.0  # open-ended = feasible by definition
    if "portal" in text and "dashboard" in text and "api" in text:
        score += 0.5
    # Dataset link available boosts feasibility
    raw_entry = next((r for r in raw if r["ps_number"]==ps.ps_id), None)
    if raw_entry and raw_entry.get("dataset_link"):
        score += 0.5
    # Too many integrations = lower feasibility
    integrations = text.count("integration") + text.count("interoperab")
    if integrations >= 3: score -= 1.0
    return round(max(1, min(10, score)), 1)

def score_impact(ps):
    text = norm(ps.title + " " + ps.description + " " + ps.org)
    # Base on org scale + theme
    score = 5.5
    if "moes" in text or "earth sciences" in text: score = 7.5  # disaster affects millions
    if "mha" in text or "home affairs" in text: score = 8.0
    if "rural development" in text: score = 7.5
    if "consumer affairs" in text: score = 7.0
    if "ayush" in text: score = 6.0
    if "aicte" in text and "student innovation" in text: score = 5.0
    if "disaster management" in norm(ps.theme): score = max(score, 7.5)
    if "medtech" in norm(ps.theme): score = max(score, 7.0)
    if "agriculture" in norm(ps.theme): score = max(score, 7.0)
    if "isro" in text and "space technology" in norm(ps.theme): score = 6.5
    if "smart education" in norm(ps.theme): score = max(score, 6.5)
    # Scale words
    if "nationwide" in text or "pan-india" in text or "national" in text: score = min(9.0, score + 0.5)
    if "all states" in text: score = min(9.0, score + 0.5)
    return round(max(1, min(10, score)), 1)

def score_demo_ability(ps):
    text = norm(ps.title + " " + ps.description)
    # Easy if web/mobile/dashboard/portal
    if any(k in text for k in ["portal","dashboard","mobile app","website","platform","visualization"]):
        base = 7.5
    else:
        base = 6.0
    if any(k in text for k in DEMO_HARD):
        base -= 1.5
    if "student innovation" in norm(ps.title):
        base = 7.0  # usually demoable
    if "gis" in text and "dashboard" in text: base = max(base, 7.5)
    if "ar-based" in text or "quantum-inspired" in text: base = max(base, 7.0)
    if "hardware" in norm(ps.category): base -= 2.0
    return round(max(1, min(10, base)), 1)

def score_team_fit(ps):
    text = norm(ps.title + " " + ps.description + " " + ps.org)
    # Typical 7th sem BTech: web, python, ML, mobile
    fit = 6.5
    if "quantum" in text: fit -= 1.5
    if "lidar" in text or "photogrammetry" in text or "electronic warfare" in text: fit -= 2.0
    if "satellite imagery" in text and "isro" in text: fit -= 0.5
    if "bhashini" in text or "multilingual" in text: fit -= 0.5  # doable but needs integration
    if "gratk" in text or "nagoya" in text or "phytopharmaceutical" in text or "treaty" in text: fit -= 1.0  # legal domain learning curve
    if "portal" in text or "dashboard" in text or "mobile app" in text: fit += 0.5
    if "student innovation" in text: fit += 1.0
    if "aicte" in text and "student innovation" in text: fit = min(8.0, fit)
    return round(max(1, min(10, fit)), 1)

def score_differentiation(ps):
    text = norm(ps.title + " " + ps.description)
    # Count twist signals already in PS (headroom if twist is invited)
    twists = sum(1 for k in DIFF_TWIST if k in text)
    # Base
    if twists >= 3: score = 7.5
    elif twists >= 2: score = 6.5
    elif twists >= 1: score = 5.5
    else: score = 5.0
    # PS that explicitly says "compare existing solutions" or "novel approach" = high headroom
    if "novel" in text or "innovative" in text: score += 0.5
    # Commodity traps: pure scan/ocr/portal without twist mention = low
    if score <= 5.0 and any(k in text for k in ["scan","ocr","extract text","portal","attendance"]) and twists==0:
        score = 4.0
    # Niche domain naturally differentiated
    if any(s in text for s in ["gratk","nagoya","ulpin","tkdl","bhashini","jurisdiction"]):
        score = max(score, 7.0)
    if "quantum-inspired" in text: score = max(score, 7.0)
    if "student innovation" in text and twists==0: score = 5.0  # open = you define diff
    return round(max(1, min(10, score)), 1)

def score_dataset(ps, raw_entry):
    text = norm(ps.title + " " + ps.description)
    # Raw dataset_link is strongest signal
    if raw_entry and raw_entry.get("dataset_link"):
        link = norm(raw_entry["dataset_link"])
        if "drive.google" in link or "kaggle" in link or "github" in link:
            base = 8.0
        else:
            base = 7.0
    else:
        base = 5.0
        # Check if PS mentions open data availability
        if any(k in text for k in ["public dataset","open data","api available","data.gov.in","isro bhuvan","imd","satellite data","land records","tkdl","ulpin","geospatial data"]):
            base += 1.0
        if "synthetic" in text or "simulate" in text: base += 0.5
        if "will be provided" in text: base -= 1.0
        if "field collection" in text or "crowdsource" in text: base -= 1.0
        if "paywalled" in text or "clarksons" in text or "lexisnexis" in text: base -= 2.0
        if "student innovation" in text: base = 6.0  # you define your own data
    return round(max(1, min(10, base)), 1)

def score_ministry_fit(ps, raw_entry):
    # Sharp intent = few PS per org = higher fit
    cnt = org_counts.get(ps.org.strip(), 5)
    if cnt <= 3: base = 8.5
    elif cnt <= 5: base = 7.5
    elif cnt <= 9: base = 6.5
    elif cnt <= 17: base = 5.5
    else: base = 4.5
    text = norm(ps.title + " " + ps.description + " " + ps.org)
    # Check mandate keywords match org
    org_l = norm(ps.org)
    if "consumer affairs" in org_l and any(k in text for k in ["legal metrology","weighing","measuring","consumer","packaged commodity","compliance"]):
        base = max(base, 8.5)
    if "ayush" in org_l and any(k in text for k in ["ayurveda","ayush","traditional","clinical","case-taking","ip","patent","gratk"]):
        base = max(base, 8.5)
    if "rural development" in org_l and any(k in text for k in ["land","gis","ulpin","cadastral","land stack"]):
        base = max(base, 8.0)
    if "isro" in org_l and "space technology" in norm(ps.theme): base = max(base, 7.5)
    if "moes" in org_l and "disaster" in norm(ps.theme): base = max(base, 7.0)
    if "student innovation" in text: base = 5.5  # generic by definition
    return round(max(1, min(10, base)), 1)

# === Evaluate all ===
results=[]
for r in raw:
    ps = PSInput(
        ps_id=r["ps_number"], title=r["title"], org=r["org"],
        department=r.get("department",""), theme=r.get("theme",""),
        category=r.get("category","Software"), description=r.get("description","")
    )
    # CLS v2
    cls, breakdown = compute_cls_v2(ps)
    # Quality text-derived
    innov = score_innovation(ps)
    feas = score_feasibility(ps)
    impact = score_impact(ps)
    demo_ab = score_demo_ability(ps)
    team = score_team_fit(ps)
    diff = score_differentiation(ps)
    ds = score_dataset(ps, r)
    demox = demo_ab  # same
    mfit = score_ministry_fit(ps, r)

    quality_score = round(innov*0.30 + feas*0.25 + impact*0.20 + demo_ab*0.15 + team*0.10, 2)
    quality = {"score": quality_score, "parts": [
        {"key":"innovation_headroom","score":innov,"weight":0.30,"source":"(v2-text)"},
        {"key":"technical_feasibility","score":feas,"weight":0.25,"source":"(v2-text)"},
        {"key":"impact","score":impact,"weight":0.20,"source":"(v2-text)"},
        {"key":"demo_ability","score":demo_ab,"weight":0.15,"source":"(v2-text)"},
        {"key":"team_fit","score":team,"weight":0.10,"source":"(v2-text)"},
    ]}
    wps = round(quality_score*0.40 + (10-cls)*0.25 + diff*0.15 + ds*0.10 + demox*0.05 + mfit*0.05, 2)
    if wps >= 7.5: verdict="STRONG PICK — Commit, build full prototype, push to internal as primary"
    elif wps >= 6.0: verdict="WORKABLE — Commit but maintain a backup PS"
    else: verdict="HIGH RISK — Skip or keep only as backup"
    exp = int(cls/10*500)
    if cls>=7: submit="Submit by 17 Sep (HIGH freeze risk)"
    elif cls>=5: submit="Submit by 18 Sep (MEDIUM freeze risk)"
    elif cls>=3: submit="Submit by 19 Sep (LOW freeze risk)"
    else: submit="Submit by 20 Sep (NEGLIGIBLE freeze risk)"
    results.append({
        "ps_id": ps.ps_id, "title": ps.title, "org": ps.org, "theme": ps.theme,
        "cls": cls, "quality": quality_score, "wps": wps, "verdict": verdict,
        "expected_submissions": exp, "submit_by": submit,
        "quality_parts": quality["parts"], "cls_breakdown": breakdown,
        "scores": {"innovation_headroom":innov,"technical_feasibility":feas,"impact":impact,"demo_ability":demo_ab,"team_fit":team,"differentiation":diff,"dataset_score":ds,"demoability":demox,"ministry_fit":mfit}
    })

# Sort by WPS
results_sorted = sorted(results, key=lambda x: x["wps"], reverse=True)

# Save JSON
with open(OUT_JSON, "w") as f:
    json.dump(results_sorted, f, indent=2, ensure_ascii=False)
print(f"Saved {len(results_sorted)} to {OUT_JSON}")

# Save CSV
import csv
with open(OUT_CSV, "w", newline="") as f:
    w=csv.writer(f)
    w.writerow(["rank","ps_id","wps","quality","cls","verdict","title","org","theme","innov","feas","impact","demo_ab","team","diff","dataset","demox","mfit","expected","submit_by"])
    for i,r in enumerate(results_sorted,1):
        s=r["scores"]
        w.writerow([i,r["ps_id"],r["wps"],r["quality"],r["cls"],r["verdict"],r["title"],r["org"],r["theme"],s["innovation_headroom"],s["technical_feasibility"],s["impact"],s["demo_ability"],s["team_fit"],s["differentiation"],s["dataset_score"],s["demoability"],s["ministry_fit"],r["expected_submissions"],r["submit_by"]])
print(f"Saved CSV to {OUT_CSV}")

# Quick stats
import statistics
print(f"quality {min(x['quality'] for x in results):.2f}-{max(x['quality'] for x in results):.2f} avg {statistics.mean(x['quality'] for x in results):.2f}")
print(f"cls {min(x['cls'] for x in results):.2f}-{max(x['cls'] for x in results):.2f} avg {statistics.mean(x['cls'] for x in results):.2f}")
print(f"wps {min(x['wps'] for x in results):.2f}-{max(x['wps'] for x in results):.2f} avg {statistics.mean(x['wps'] for x in results):.2f}")
print(f"verdicts: {Counter(x['verdict'] for x in results)}")
print("\nTop 15:")
for r in results_sorted[:15]:
    print(f"{r['ps_id']} WPS {r['wps']:.2f} Q {r['quality']:.2f} CLS {r['cls']:.2f} | {r['title'][:60]} | {r['org'][:30]}")

print("\nMDoNER fix check:")
for r in results_sorted:
    if "MDoNER" in r["org"]:
        print(r["ps_id"], r["cls"], r["cls_breakdown"]["org"], r["wps"], r["verdict"])
