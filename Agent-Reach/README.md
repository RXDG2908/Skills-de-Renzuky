# Agent-Reach — Tool/App with a bundled skill

From <https://github.com/Panniantong/Agent-Reach> (MIT). **Type: Tool/App.** The
upstream repo is a Python CLI (`agent_reach` package) that reads/searches Twitter,
Reddit, YouTube, GitHub, Bilibili, and Xiaohongshu — one CLI, no per-platform API keys.
Only its embedded skill wrapper (`agent_reach/skill/`) was pulled, not the CLI
implementation itself (`agent_reach/`, `scripts/`, `tests/`).

`skill/SKILL.md` (+ `SKILL_en.md`) is the agent-facing entry point; `skill/references/`
holds per-domain playbooks: `career.md`, `dev.md`, `finance.md`, `search.md`,
`social.md`, `video.md`, `web.md`.

Note: using this skill for real still requires the `agent-reach` CLI/package installed
and configured — the SKILL.md documents how to call it, it doesn't vendor the tool.
