# JadurBox AI Agents — Cross-platform Starter Kit

Five portable specialized **instruction agents** for JadurBox video productions, with a source-of-truth in `core/`. **Nothing in this repo automatically posts to GitHub, YouTube or edits media.** You must supply local authorized tools to run media commands.

## Hierarchy

```text
JadurBox-Agent (Director)
├── JD-Script-agent (Writer)
│   └── JD-Script-QA (Independent Script Review)
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

- `core/` — canonical policies and five role files
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
