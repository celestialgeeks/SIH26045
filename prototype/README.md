# Prototype — 3 Modules

All runnable. See top-level README for quickstart.

| Module | File | What it does (1 line) |
|---|---|---|
| **citation_validator** | `citation_validator/validator.py` | 56 regex — validates every `[CIT: ...]` or ABSTAIN |
| **eval_harness** | `eval_harness/gold_qa.json` + `adversarial.json` | 20 gold + 5 adversarial (→ 40+10 in Iter3) |
| **neo4j_schema** | `neo4j_schema/schema.cypher` | Formulation → IP → Regulatory graph + 6 traversals |

Run smoke tests:
```bash
python prototype/citation_validator/validator.py
pytest prototype/citation_validator/test_validator.py -v
cat prototype/eval_harness/gold_qa.json | head -n 30
cat prototype/neo4j_schema/schema.cypher | head -n 40
```
