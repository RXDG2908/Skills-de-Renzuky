# Skills library

Reusable skills collected for future design/frontend/content generations. Each was
stripped to its skill payload (app source, websites, preview galleries, `.git` removed
unless noted).

**[`CATALOG.md`](CATALOG.md)** — flat one-line index of all 2066 entries (skills +
design-systems + templates). Grep it by keyword, then open the `SKILL.md` / `DESIGN.md`
at the path shown. Regenerate with `python .catalog/build_catalog.py`.
Say **"usa skills"** in any project to have the right one picked and applied automatically.

**Type** column: **Skill** = the folder is only agent-skill payload. **Tool+Skill** = the
upstream repo is primarily a standalone application/CLI/product; only a thin companion
skill was extracted, and using it for real may require that tool installed/running/MCP-connected.
**Not skills** = kept for reference only, nothing here is invocable as a skill.

| Folder | Type | What | Count | Size |
|---|---|---|---|---|
| [`eng-review-skills/`](eng-review-skills/) | Skill (authored) | 32 engineering review/audit skills written for this library: database, testing, reliability (idempotency/outbox), API, frontend, concurrency — checklist + red-flags + fix, grounded in `reference-docs/` | 32 | 140K |
| [`reference-docs/`](reference-docs/) | Not skills | Authoritative source docs for the above (OWASP CheatSheets/ASVS/WSTG/API-Security, Google eng-practices, system-design-primer, clean-code-js, redis-doc) — reference only | — | 41M |
| [`ant-design/`](ant-design/) | Skill | Sparse-checked out from ant-design/ant-design (MIT, ~280MB repo): `usage-skills/` (component lookup, v4→v5 migration, theme tokens) + `maintainer-skills/` (repo-specific, mostly Chinese) | 9 | 96K |
| [`awesome-claude-skills/`](awesome-claude-skills/) | Skill (+ Tool for composio-skills/) | 28 standalone skills + `document-skills/` (docx/pdf/pptx/xlsx) + `composio-skills/` (832 `<app>-automation` stubs, **need Rube MCP**) (ComposioHQ) | 864 | 14M |
| [`caveman/`](caveman/) | Skill | Coding-agent methodology: explore, refactor, migrate, review with evidence, terse "caveman mode" (JuliusBrussee) — the skills/ dir is MIT; the Caveman engine app itself is BSL-1.1 and wasn't brought in | 20 | 408K |
| [`brag/`](brag/) | Skill | Turns a project's own code into a shareable launch video via Hyperframes (latent-spaces) | 1 | 17M |
| [`emilkowalski-skills/`](emilkowalski-skills/) | Skill | Animation/UI craft from Emil Kowalski (Vercel, Sonner/Vaul, animations.dev) | 13 | 316K |
| [`impeccable/`](impeccable/) | Skill | UI code craft reviewer/builder (pbakaus) — same territory as `taste-skill` | 1 | 2.3M |
| [`awesome-ux-skills/`](awesome-ux-skills/) | Skill | Flat-format UX skills: heuristics, personas, journey maps, double-diamond, accessibility, Dieter Rams (tommyjepsen) — no upstream LICENSE | 23 | 332K |
| [`video-use/`](video-use/) | Skill | Edit any video by conversation — transcribe, cut, color grade, overlays, subtitles (browser-use org) | 2 | 800K |
| [`ecc-video-editing/`](ecc-video-editing/) | Skill | AI video-editing pipeline for real footage: FFmpeg → Remotion → ElevenLabs → fal.ai → Descript/CapCut (from mit-network/everything-claude-code) | 1 | — |
| [`claude-remotion-skill/`](claude-remotion-skill/) | Skill | Remotion (React→MP4) motion graphics: intros/outros/logos/reels/promos, text animation (haidrrrry) | 1 | 45K |
| [`video-motion-craft/`](video-motion-craft/) | Skill | Remotion motion graphics + FFmpeg/Whisper footage editing (trim, jump-cut, captions, overlays) (vibegameengine) | 1 | 192K |
| [`vertical-video-editing-skills/`](vertical-video-editing-skills/) | Skill | Script + talking-head/voiceover → creator-grade 9:16 vertical short via HyperFrames (nopefallacy) | 1 | 164K |
| [`video-editor-plugin/`](video-editor-plugin/) | Skill | General video editing: trim/compress/merge/resize/captions/title cards/GIFs/watermarks (ElSalvatore-sys) | 1 | 267K |
| [`remotion-ffmpeg-video-skill/`](remotion-ffmpeg-video-skill/) | Skill | Remotion + FFmpeg video skill (albertpikkop) | 1 | 61K |
| [`claude-code-video-toolkit/`](claude-code-video-toolkit/) | Not skills | Curated README pointing to video-production tools/skills (wilwaldon) — reference only, links out | — | 12K |
| [`img2game2d/`](img2game2d/) | Skill | Concept art → game-ready 2D assets: sprite sheets, skeletal rigs, atlases, lighting maps, engine exports (Godot/Unity/Spine/Phaser/PixiJS) (MrFaraidun) | 1 | 136K |
| [`spine-animation-ai/`](spine-animation-ai/) | Skill | AI-driven Spine 2D skeletal animation (GenielabsOpenSource) | 1 | 180K |
| [`live2d-from-art/`](live2d-from-art/) | Skill | Build/repair interactive Live2D from art or layered PNG/PSD — cutout, inpaint, mesh+param rig, MOC3 (fifteen42) | 1 | 37K |
| [`live2d-agent-kit/`](live2d-agent-kit/) | Skill | Live2D from reference art/PSD via psd2live, super-res, real Cubism validation, VTube Studio packaging (Ariakage) | 1 | 2.1M |
| [`PuppetLoom/`](PuppetLoom/) | Tool+Skill | `live2d-puppet` — animatable 2D chars from layered PSD via the PuppetLoom CLI; needs that CLI (CheshireMew) | 1 | 308K |
| [`svg-character-animator/`](svg-character-animator/) | Skill | SVG character/mascot state-machine animation — morph between poses/emotions, idle motion, iOS/SwiftUI export (molauu) | 1 | 737K |
| [`MotionLoom/`](MotionLoom/) | Tool+Skill | `motionloom` — project-aware animation production with runtime evidence + review-first PR handoff (lenhonbp) | 1 | 44K |
| [`ae-agent-skills/`](ae-agent-skills/) | Tool+Skill | After Effects editing via `ae-cli` — declarative JSON scenes + command-by-command edits; needs the ae-cli tool (yumehiko) | 2 | 42K |
| [`gpt-image2-layered-psd/`](gpt-image2-layered-psd/) | Skill | `psd-layer-extractor` — split an image into semantic element PNGs + assemble an editable layered PSD (JongLeePc) | 1 | 126K |
| [`character-animation-skill/`](character-animation-skill/) | Skill | Character animation skill (karem505) | 1 | 140K |
| [`agent-skills-addyosmani/`](agent-skills-addyosmani/) | Skill | 25 end-to-end engineering-practice skills: TDD, spec-driven, debugging, security, perf, CI/CD, git workflow, shipping (Addy Osmani/Google) | 25 | 573K |
| [`security-audit-skill/`](security-audit-skill/) | Skill | Multi-phase security audit with independently-verified findings (Cloudflare, official) | 1 | 368K |
| [`archify/`](archify/) | Tool+Skill | Full diagram-tool repo (~313MB: website, viewer, benchmarks) — only its 2 skills kept: `archify` (architecture/flow/sequence diagrams as HTML) + `archify-review` (repo-maintainer only) (tt-a1i) | 2 | 8.6M |
| [`Agent-Reach/`](Agent-Reach/) | Tool+Skill | CLI that reads/searches Twitter/Reddit/YouTube/GitHub/Bilibili/XHS, no API keys — only the skill wrapper kept, **needs the `agent-reach` CLI installed** (Panniantong) | 1 | 104K |
| [`VoiceStudio/`](VoiceStudio/) | Tool+Skill | Local ElevenLabs-alternative voice app (Electron+backend+frontend) — only `skills/` kept, **needs VoiceStudio installed and running** (debpalash) | 2 | 64K |
| [`open-design-skills/`](open-design-skills/) | Skill | `skills/` + `design-systems/` + `design-templates/` from nexu-io/open-design | 162 + 152 + 113 | 22M |
| [`animation-principles/`](animation-principles/) | Skill | Disney's 12 animation principles, indexed 12 ways — domain, role, UI element, tool/framework, timing, emotion… (dylantarre) | 144 | 1.6M |
| [`social-media-skills/`](social-media-skills/) | Skill | Social-media ops: content, analytics, campaigns, community, tools (canva, capcut) (social-media-skills) | 106 | 3.8M |
| [`html-anything-skills/`](html-anything-skills/) | Skill | HTML deliverable templates from nexu-io/html-anything | 81 | 1.7M |
| [`designer-skills/`](designer-skills/) | Skill | UX process: research, systems, ops, interaction, strategy, critique (Owl-Listener) — see `INDEX.md` | 107 | 1.1M |
| [`motion-skills/`](motion-skills/) | Skill | Motion graphics/video/animation, 15 packs (iart-ai): TikTok, explainers, data charts, web/GSAP, WebGL/3D, Manim, ecommerce, ads, kinetic type | 51 | 1.9M |
| [`claude-ads/`](claude-ads/) | Skill | Paid ads across 12 platforms: audit, budget, creative, attribution (AgriciDaniel) — `ads/` is the root conductor | 34 | 617K |
| [`ui-ux-pro-max/`](ui-ux-pro-max/) | Skill | UI/UX design-intelligence DB, branding, styling, slides (nextlevelbuilder) | 7 | 11M |
| [`pixel2motion/`](pixel2motion/) | Skill | Image/pixel-art → motion/video (nolangz) | 1 | 228K |
| [`video-production-skills/`](video-production-skills/) | Skill | HyperFrames/Remotion video: motion direction, text openers, dark-SaaS style, reference-replica QC (Pluviobyte) | 4 | 196K |
| [`content-skills/`](content-skills/) | Skill | Viral short-form content: hooks, captions/CTAs, platform formats (vyralcontent) | 7 | 760K |
| [`taste-skill/`](taste-skill/) | Skill | Anti-slop frontend/design skills (Leonxlnx) | 14 | 360K |
| [`motion-design-skill/`](motion-design-skill/) | Skill | Lottie/dotLottie-aware motion design (LottieFiles) | 1 | 92K |
| [`motion-dev-animations-skill/`](motion-dev-animations-skill/) | Skill | Motion.dev (Framer Motion successor) animations for React/Next.js/Svelte/Astro, 120fps GPU-accelerated (199-biotechnologies) | 1 | 137K |
| [`awesome-design-skills/`](awesome-design-skills/) | Skill | `SKILL.md` + `DESIGN.md` style systems (bergside) | 68 | 632K |
| [`html-ppt-skill/`](html-ppt-skill/) | Skill | HTML PPT Studio: 36 themes, decks, layouts, animations (lewislulu) — keeps `.git` | 1 | 21M |
| [`huashu-design/`](huashu-design/) | Skill | 花叔Design: HTML prototypes, slides, GSAP animation, MP4/GIF export, review | 1 | 32M |
| [`awesome-claude-design/`](awesome-claude-design/) | Not skills | Curated index of `DESIGN.md` files (VoltAgent) — `README.md` only, links out | — | 24K |
| [`claude-quickstarts/`](claude-quickstarts/) | Not skills | Anthropic example apps — reference only (see `NOTE.md`) | — | 8.5M |

## Skill vs Tool+Skill vs Not skills

- **Not brought in at all** (fully app, zero SKILL.md found): `webadderallorg/Recordly`
  (screen recorder). See `Not brought in` note below the table in `use-skills/SKILL.md`.
- **Tool+Skill** folders (`archify`, `Agent-Reach`, `VoiceStudio`, and `composio-skills/`
  inside `awesome-claude-skills`) only work fully if the underlying tool/CLI/MCP server
  is actually present — the skill alone won't reproduce the app's behavior, it's a
  connector. Say so before promising results from one of these.

## Overlap note

`taste-skill`, the style systems in `awesome-design-skills`, and several `open-design-skills/skills/*`
share upstream lineage (taste-skill, stitch, brandkit, etc.). `open-design-skills` is the widest
superset. When looking for a design direction, start there or in `awesome-design-skills`.
