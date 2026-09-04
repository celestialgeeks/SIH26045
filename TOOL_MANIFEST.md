# SIH26 Bot — Tool Manifest

| Capability | Tool / Skill | How to invoke |
|---|---|---|
| Scrape SIH PS | kimi-webbridge | `curl http://127.0.0.1:10086/command -d '{..."action":"navigate",...}' --session sih26-discover` + snapshot/evaluate |
| Search + enrich | web-research, web-search, parallel-cli | `skill_view('web-research')`, `parallel-cli` for bulk |
| Papers | arxiv | `arxiv` skill |
| Grounded claims | grounded-citations | cite every research note |
| Prototype build | plan, spike, github, codebase-inspection, systematic-debugging | `skill_view('plan')` → scaffold → github |
| PPT (primary) | slide-skill (competition/free-design) | `slide-skill quickstart outline.md --mode ai` + QA gates |
| PPT (fallback) | ppt-master, agentbuff-presentation | alternative pipelines |
| Design | claude-design, sketch, deck-design, jaw-dropping-website | prototype UI + slide visuals |
| Integrations | composio (gmail, notion, sheets, github, figma) | `COMPOSIO_SEARCH_TOOLS` → `COMPOSIO_MULTI_EXECUTE_TOOL` |
| Vault | obsidian, notion, google-workspace | save to `my info/` only |
| Browser extension | Kimi WebBridge (daemon :10086) | requires Chrome extension connected; fallback to cookieless-web-fetch / web_extract |
