# JadurBox AI Agents — Cross-platform Starter Kit

Eleven portable specialized **instruction agents** for JadurBox video productions, with a source-of-truth in `core/`. **Nothing in this repo automatically posts to GitHub, YouTube or edits media.** You must supply local authorized tools to run media commands.

## Hierarchy

```text
JadurBox-Agent (Director)
├── JD-Growth-agent (YouTube Growth)
│   └── JD-Growth-QA (Independent Growth Review)
├── JD-Research-agent (Evidence Research)
│   └── JD-Research-QA (Independent Fact Review)
├── JD-Script-agent (Writer)
│   └── JD-Script-QA (Independent Script Review)
├── JD-Asset-agent (Asset Sourcing)
│   └── JD-Asset-QA (Independent Asset Review)
└── JD-Video-agent (HyperFrames Editor)
    └── JD-Video-QA (Independent Video Review)
```

## Install/use

1. Download/extract or clone this repository and open it in VS Code.
2. For a new production project, copy `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `core/`, and the agent folders for the tools you actually use. Include `scripts/` if you want to synchronize adapter files.
3. **Claude Code**: agents in `.claude/agents/`. Ask `Use jd-video-agent for a preview-only editing plan`.
4. **Codex**: roles in `.agents/skills/`, invoke `$jd-video-agent` or `$jd-video-qa` in a Codex chat.
5. **Gemini CLI**: agents in `.gemini/agents/`. Ask `Use jd-video-agent`; support varies with CLI version.
6. **ChatGPT**: select the existing JD private plugins, or install/package these skills in a supported host; repository alone isn't an automatic plugin install.
7. Modify **only** `core/` for common role rule changes; run `python scripts/sync_agents.py`; verify `python scripts/sync_agents.py --check`.
8. QA reports always include evidence and unknowns. Human must explicitly approve script, render and publish.

## Folder map

- `core/` — canonical policies and eleven role files
- `.claude/agents/` — Claude Code subagent copies generated from core
- `.gemini/agents/` — Gemini CLI subagent copies generated from core
- `.agents/skills/` — Codex skills generated from core
- `.github/copilot-instructions.md` — Copilot generic policy
- `docs/HANDOFF.md` — explicit department routing & approval record
- `knowledge/CHANGELOG.md` — versioned, creator-approved lessons

## Data security
No API keys, `.env` files, paid footage, voiceovers, music, video exports, customer data, GitHub credentials or private asset libraries in Git. `.gitignore` is a safety measure, not a substitute for reviewing each file before sharing.

## Push policy
**DO NOT PUSH until the creator explicitly approves and specifies destination repository and visibility.** Review the complete diff first. If authorized, use an available connected GitHub tool / CLI. A newly connected GitHub account is not blanket permission to push.

## Asset department

- `jd-asset-agent` and `jd-asset-qa` are additional canonical roles in `core/` with adapters for Claude, Gemini, Codex.
- Optional local `tools/asset_cli.py` can search Pixabay photos/videos and Unsplash photos; Pollinations generation requires creator authorization.
- Copy `.env.example` to `.env` **locally**, add newly rotated credentials, and never commit `.env`.
- QA should check direct source links, licensing, AI/archival labels and actual media dimensions before asset use.

## Research department

- `jd-research-agent` builds a source-backed research brief, evidence ledger and precise chronology before writing.
- `jd-research-qa` separately checks source authenticity, dates, numbers, causality and uncertainty; marks PASS / REVISE / NOT VERIFIED with evidence.
- QA PASS does not grant creator approval or permission to render, publish or push.

## Growth department

- `jd-growth-agent` uses dated YouTube Studio/authorized vidIQ evidence for content and SEO plans, separating Shorts vs long-form.
- `jd-growth-qa` independently verifies numbers, periods, sources, competitor estimates and title claims. Neither QA nor growth claims guarantee virality.
- Private analytics and credentials are excluded from public GitHub. Private ChatGPT Plugins are not auto-synced.
