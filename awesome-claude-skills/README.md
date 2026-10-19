# awesome-claude-skills

864 skills from <https://github.com/ComposioHQ/awesome-claude-skills>. Three tiers:

1. **28 standalone general-purpose skills** (top-level folders below) — no special
   dependency, use directly.
2. **`document-skills/`** (4) — the standard `docx` / `pdf` / `pptx` / `xlsx` skills.
3. **`composio-skills/`** (832) — one tiny templated skill per SaaS integration
   ("`<app>-automation`": Ably, Adobe, Ahrefs, Slack, Notion, Gmail, …), plus
   `connect` / `connect-apps` / `connect-apps-plugin` / `skill-share`. **All of these
   require the Rube MCP server connected** (`RUBE_SEARCH_TOOLS` / `RUBE_MANAGE_CONNECTIONS`)
   — they are prompts that call Composio's MCP tools, not standalone workflows. Check the
   MCP is available before applying one; if it isn't, say so instead of pretending to run it.

## The 28 standalone skills

- **artifacts-builder** — Multi-component claude.ai HTML artifacts (React, Tailwind, shadcn/ui) for complex state/routing needs beyond a single-file artifact.
- **brand-guidelines** — Applies Anthropic's official brand colors/typography to an artifact. Reference for shaping your own brand skill.
- **canvas-design** — Original visual art (poster/design) as PNG/PDF via design philosophy; ships its own `canvas-fonts/`.
- **changelog-generator** — Git commits → customer-facing changelog, categorized and rewritten in plain language.
- **competitive-ads-extractor** — Pulls competitors' ads from ad libraries (Meta, LinkedIn, …) to read messaging/creative approach.
- **connect** / **connect-apps** / **connect-apps-plugin** — Take real actions in Gmail/Slack/GitHub/Notion/1000+ apps. *(Rube MCP)*
- **content-research-writer** — Research + citations + outline iteration + section feedback for long-form writing.
- **developer-growth-analysis** — Mines Claude Code chat history for coding patterns/gaps, curates learning links, posts a report to Slack.
- **domain-name-brainstormer** — Domain-name ideas + multi-TLD availability check.
- **file-organizer** — Understands context to de-dupe and restructure files/folders.
- **image-enhancer** — Upscales/sharpens screenshots for docs/slides/social.
- **internal-comms** — Status reports, leadership updates, newsletters, incident reports in a company's house format.
- **invoice-organizer** — Extracts fields from messy invoices/receipts, renames + sorts for tax prep.
- **langsmith-fetch** — Pulls LangChain/LangGraph execution traces from LangSmith Studio for debugging. *(needs the `langsmith-fetch` CLI)*
- **lead-research-assistant** — Finds and qualifies leads for a product/service with contact strategy.
- **mcp-builder** — Guide for building well-designed MCP servers (Python FastMCP or Node/TS SDK).
- **meeting-insights-analyzer** — Transcripts → communication/behavioral patterns (filler words, interruption, conflict avoidance).
- **raffle-winner-picker** — Fair random winner selection from a list/spreadsheet/Google Sheet.
- **skill-creator** — Guide for authoring or updating a Claude skill.
- **skill-share** — Creates a skill and posts it to Slack for team discovery. *(Rube MCP)*
- **slack-gif-creator** — Composable animation primitives + size validators for Slack-ready GIFs.
- **tailored-resume-generator** — Job description → resume tuned to that posting.
- **template-skill** — Blank scaffold for writing a new skill.
- **theme-factory** — 10 preset themes (or generate one) to style any artifact — slides, docs, landing pages.
- **twitter-algorithm-optimizer** — Rewrites tweets against the published open-source ranking-algorithm signals.
- **video-downloader** — YouTube download at a chosen quality/format, or audio-only MP3.
- **webapp-testing** — Playwright toolkit: exercise a local web app, screenshot, read console/logs.

See [`UPSTREAM-README.md`](UPSTREAM-README.md) for the original repo overview.
Dropped `.github/`, `CONTRIBUTING.md` (repo meta).
