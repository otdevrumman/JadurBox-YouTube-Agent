# Platform notes

- **Claude Code**: `.claude/agents/*.md`, project subagents; open repo in VS Code with Claude Code installed; ask to use `jd-video-agent` by name. Custom agent tool permissions depend on Claude Code runtime.
- **Gemini CLI**: `.gemini/agents/*.md` plus `GEMINI.md`; check your installed Gemini CLI version supports local subagents. Ask the assistant to use an agent by role. If unsupported, include core role in prompt.
- **OpenAI Codex**: root `AGENTS.md` plus `.agents/skills/*/SKILL.md`; invoke `$jd-video-agent`, `$jd-video-qa`, etc. Installation/discovery depends on Codex CLI/VS Code extension.
- **ChatGPT**: existing private JadurBox plugins are managed independently; the skills in this repository can be packaged or installed in supported ChatGPT/Codex environments, **not automatically** synchronized by git. Standard ChatGPT web chats do not execute repository files simply because GitHub is connected.
- **Copilot VS Code**: `.github/copilot-instructions.md` provides broad project guidance; agent support and discovery differ from Claude/Codex/Gemini.
- **Any other editor**: give it `AGENTS.md` + `core/COMMON.md` + selected role; no automatic activation promised.
