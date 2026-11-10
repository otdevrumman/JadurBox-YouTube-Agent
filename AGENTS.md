# JadurBox — Cross-platform Agents

This repo holds **platform-portable instructions**, not a running autonomous agent service. Read `core/COMMON.md` and the relevant department in `core/` before work. `jadurbox-main` coordinates subagents and requires creator approval at script, preview, render and publication gates.

Agents: `jadurbox-main`, `jd-growth-agent`, `jd-growth-qa`, `jd-research-agent`, `jd-research-qa`, `jd-script-agent`, `jd-script-qa`, `jd-asset-agent`, `jd-asset-qa`, `jd-video-agent`, `jd-video-qa`.

**Important:** no GitHub `push`, publication, rendering, destructive operations, or plugin installation without explicit approval. Treat QA PASS as recommendation, not creator approval. Each task must report what was not verified.

For Codex, use `.agents/skills/<agent>/SKILL.md`; for Claude Code use `.claude/agents/<agent>.md`; for Gemini CLI use `.gemini/agents/<agent>.md`. Generate/validate adapters with `python scripts/sync_agents.py`.
