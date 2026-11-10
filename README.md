# Skills library

Reusable skills collected for future design/frontend/content generations. Each was
stripped to its skill payload (app source, websites, preview galleries, `.git` removed
unless noted).

## Layout — light to clone

```
skills/   every skill folder (SKILL.md, rules, scripts, configs) — text only
tools/    tools.json + install.ps1 / install.sh — LINKS to the tools the skills use,
          never the tools themselves. Fetched tools land in tools/_downloads/ (gitignored)
```

- **Nothing heavy goes in git**: `.gitignore` blocks images, video, audio, fonts, 3D files,
  PDFs, archives, binaries, ML weights, `node_modules/` and render output (`out/`, `dist/`…).
  Skill example images/sample media stay only on the PC that made them, so after a fresh
  clone some skills' preview images or bundled fonts are missing; the instructions still work.
- **Setting up on a new PC**: `git clone …`, then install only what you need:
  `.\tools\install.ps1` (list) → `.\tools\install.ps1 ffmpeg yt-dlp` or
  `-Category lipsync`. Each tool comes from its official repo. See [`tools/README.md`](tools/README.md).

Two ways to find a skill:

- **[`TEMAS.md`](TEMAS.md)** — topic map by *purpose* (code, web, design, video, audio,
  animation, 2D characters, image, content/social, ads, docs, automation, reference).
  Start here when you know *what you want to do*.
- **[`CATALOG.md`](CATALOG.md)** — flat one-line index of all 5613 entries (skills +
  design-systems + templates). Grep it by keyword, then open the `SKILL.md` / `DESIGN.md`
  at the path shown. Regenerate with `python .catalog/build_catalog.py`.

Say **"usa skills"** in any project to have the right one picked and applied automatically.

**Type** column: **Skill** = the folder is only agent-skill payload. **Tool+Skill** = the
upstream repo is primarily a standalone application/CLI/product; only a thin companion
skill was extracted, and using it for real may require that tool installed/running/MCP-connected.
**Tool (link only)** = a standalone tool with no `SKILL.md`; the repo keeps only its link in `tools/tools.json` — install it with `tools/install.ps1 <name>`.
**Not skills** = kept for reference only, nothing here is invocable as a skill.

| Folder | Type | What | Count | Size |
|---|---|---|---|---|
| [`eng-review-skills/`](skills/eng-review-skills/) | Skill (authored) | 32 engineering review/audit skills written for this library: database, testing, reliability (idempotency/outbox), API, frontend, concurrency — checklist + red-flags + fix, grounded in `reference-docs/` | 32 | 140K |
| [`reference-docs/`](skills/reference-docs/) | Not skills | Authoritative source docs for the above (OWASP CheatSheets/ASVS/WSTG/API-Security, Google eng-practices, system-design-primer, clean-code-js, redis-doc) — reference only | — | 41M |
| [`ant-design/`](skills/ant-design/) | Skill | Sparse-checked out from ant-design/ant-design (MIT, ~280MB repo): `usage-skills/` (component lookup, v4→v5 migration, theme tokens) + `maintainer-skills/` (repo-specific, mostly Chinese) | 9 | 96K |
| [`awesome-claude-skills/`](skills/awesome-claude-skills/) | Skill (+ Tool for composio-skills/) | 28 standalone skills + `document-skills/` (docx/pdf/pptx/xlsx) + `composio-skills/` (832 `<app>-automation` stubs, **need Rube MCP**) (ComposioHQ) | 864 | 14M |
| [`caveman/`](skills/caveman/) | Skill | Coding-agent methodology: explore, refactor, migrate, review with evidence, terse "caveman mode" (JuliusBrussee) — the skills/ dir is MIT; the Caveman engine app itself is BSL-1.1 and wasn't brought in | 20 | 408K |
| [`brag/`](skills/brag/) | Skill | Turns a project's own code into a shareable launch video via Hyperframes (latent-spaces) | 1 | 17M |
| [`emilkowalski-skills/`](skills/emilkowalski-skills/) | Skill | Animation/UI craft from Emil Kowalski (Vercel, Sonner/Vaul, animations.dev) | 13 | 316K |
| [`impeccable/`](skills/impeccable/) | Skill | UI code craft reviewer/builder (pbakaus) — same territory as `taste-skill` | 1 | 2.3M |
| [`awesome-ux-skills/`](skills/awesome-ux-skills/) | Skill | Flat-format UX skills: heuristics, personas, journey maps, double-diamond, accessibility, Dieter Rams (tommyjepsen) — no upstream LICENSE | 23 | 332K |
| [`video-use/`](skills/video-use/) | Skill | Edit any video by conversation — transcribe, cut, color grade, overlays, subtitles (browser-use org) | 2 | 800K |
| [`ecc-video-editing/`](skills/ecc-video-editing/) | Skill | AI video-editing pipeline for real footage: FFmpeg → Remotion → ElevenLabs → fal.ai → Descript/CapCut (from mit-network/everything-claude-code) | 1 | — |
| [`claude-remotion-skill/`](skills/claude-remotion-skill/) | Skill | Remotion (React→MP4) motion graphics: intros/outros/logos/reels/promos, text animation (haidrrrry) | 1 | 45K |
| [`video-motion-craft/`](skills/video-motion-craft/) | Skill | Remotion motion graphics + FFmpeg/Whisper footage editing (trim, jump-cut, captions, overlays) (vibegameengine) | 1 | 192K |
| [`vertical-video-editing-skills/`](skills/vertical-video-editing-skills/) | Skill | Script + talking-head/voiceover → creator-grade 9:16 vertical short via HyperFrames (nopefallacy) | 1 | 164K |
| [`video-editor-plugin/`](skills/video-editor-plugin/) | Skill | General video editing: trim/compress/merge/resize/captions/title cards/GIFs/watermarks (ElSalvatore-sys) | 1 | 267K |
| [`remotion-ffmpeg-video-skill/`](skills/remotion-ffmpeg-video-skill/) | Skill | Remotion + FFmpeg video skill (albertpikkop) | 1 | 61K |
| [`ecc-affaan-skills/`](skills/ecc-affaan-skills/) | Skill | 3 media skills pulled from affaan-m/ECC (the ~100MB "Everything Claude Code" monorepo, rest left out): `video-editing` (FFmpeg→Remotion→ElevenLabs→fal.ai→Descript/CapCut), `remotion-video-creation` (29 Remotion rules), `fal-ai-media` (image/video/audio via fal.ai MCP) | 3 | 198K |
| [`jianshuo-claude-skills/`](skills/jianshuo-claude-skills/) | Skill | 41 personal skills (Wang Jianshuo): video production (subtitles, dubbing, reframe, multicam, overlay, text→video, video-book), publishing (Hugo/WeChat/小红书/X/App Store/TestFlight), VoiceDrop (needs its MCP), article mining, style distillation — several Chinese and MCP/CLI-dependent | 41 | 17M |
| [`master-skills/`](skills/master-skills/) | Skill | 3 "master skills" (Jakeschincariol, MIT): `edit` (cut dead space, captions, stop-motion), `virality` (LinkedIn+YouTube agents fused), `build` (best design+code skills merged into apps/sites) | 3 | 487K |
| [`claude-code-video-toolkit/`](skills/claude-code-video-toolkit/) | Not skills | Curated README pointing to video-production tools/skills (wilwaldon) — reference only, links out | — | 12K |
| [`img2game2d/`](skills/img2game2d/) | Skill | Concept art → game-ready 2D assets: sprite sheets, skeletal rigs, atlases, lighting maps, engine exports (Godot/Unity/Spine/Phaser/PixiJS) (MrFaraidun) | 1 | 136K |
| [`spine-animation-ai/`](skills/spine-animation-ai/) | Skill | AI-driven Spine 2D skeletal animation (GenielabsOpenSource) | 1 | 180K |
| [`live2d-from-art/`](skills/live2d-from-art/) | Skill | Build/repair interactive Live2D from art or layered PNG/PSD — cutout, inpaint, mesh+param rig, MOC3 (fifteen42) | 1 | 37K |
| [`live2d-agent-kit/`](skills/live2d-agent-kit/) | Skill | Live2D from reference art/PSD via psd2live, super-res, real Cubism validation, VTube Studio packaging (Ariakage) | 1 | 2.1M |
| [`PuppetLoom/`](skills/PuppetLoom/) | Tool+Skill | `live2d-puppet` — animatable 2D chars from layered PSD via the PuppetLoom CLI; needs that CLI (CheshireMew) | 1 | 308K |
| [`svg-character-animator/`](skills/svg-character-animator/) | Skill | SVG character/mascot state-machine animation — morph between poses/emotions, idle motion, iOS/SwiftUI export (molauu) | 1 | 737K |
| [`MotionLoom/`](skills/MotionLoom/) | Tool+Skill | `motionloom` — project-aware animation production with runtime evidence + review-first PR handoff (lenhonbp) | 1 | 44K |
| [`ae-agent-skills/`](skills/ae-agent-skills/) | Tool+Skill | After Effects editing via `ae-cli` — declarative JSON scenes + command-by-command edits; needs the ae-cli tool (yumehiko) | 2 | 42K |
| [`gpt-image2-layered-psd/`](skills/gpt-image2-layered-psd/) | Skill | `psd-layer-extractor` — split an image into semantic element PNGs + assemble an editable layered PSD (JongLeePc) | 1 | 126K |
| [`character-animation-skill/`](skills/character-animation-skill/) | Skill | Character animation skill (karem505) | 1 | 140K |
| [`agent-skills-addyosmani/`](skills/agent-skills-addyosmani/) | Skill | 25 end-to-end engineering-practice skills: TDD, spec-driven, debugging, security, perf, CI/CD, git workflow, shipping (Addy Osmani/Google) | 25 | 573K |
| [`security-audit-skill/`](skills/security-audit-skill/) | Skill | Multi-phase security audit with independently-verified findings (Cloudflare, official) | 1 | 368K |
| [`face-analysis-skill/`](skills/face-analysis-skill/) | Skill (authored) | Face detection & analysis pipeline guide: which library per stage (detection/landmarks/parsing/preprocess/inference) — InsightFace, MediaPipe, OpenCV, YOLO, DeepFace, dlib, face-alignment, SAM2, ONNX Runtime, OpenVINO, TensorRT — with install, license & privacy cautions. Libraries not vendored | 1 | 28K |
| [`lyric-swap-lipsync/`](skills/lyric-swap-lipsync/) | Skill (authored) | Change what a character says or sings in a clip with the same voice/rhythm + lip-sync: vocal split (UVR/Demucs) → word-level speech edit (ViiTorVoice-NAR/AuK) or singing lyric edit (SoulX-Singer/YingMusic/ACE-Step) or voice conversion (Seed-VC/RVC) → LatentSync/MuseTalk. Tools in `tools/tools.json` | 1 | 6K |
| [`tts-voice-bank/`](skills/tts-voice-bank/) | Skill (authored) | Quick TTS presets + Spanish voice guide (edge-tts, kokoro, piper, espeak-ng); sample mp3s stay local | 1 | — |
| [`Export-Paper-Model-from-Blender/`](tools/README.md#export-paper-model-from-blender) | Tool (link only) | Blender add-on: unfolds a mesh into a printable papercraft net with glue tabs, edge numbers, valley/mountain folds, sheet nesting → SVG/PDF; needs Blender ≥5.0, drivable via Blender MCP (addam, GPL-3.0+ per `blender_manifest.toml`, no LICENSE file) | — | 165K |
| [`boxes/`](tools/README.md#boxes) | Tool (link only) | Boxes.py: 100+ parametric laser-cut box/structure generators — finger joints, tab-slot, living hinges, kerf compensation; Python CLI/web → SVG (florianfesti, GPL-3.0) — shallow clone | — | 58M |
| [`openscad-skills/`](skills/openscad-skills/) | Skill | OpenSCAD agent skills: BOSL2 geometry, workflow planning, project structure, board-game organizers (written for Gemini CLI, work the same) (joaorura, MIT) | 4 | 55K |
| [`cadquery-skills/`](skills/cadquery-skills/) | Skill | CadQuery Claude Code plugin: planner, code generation, assembly constraints, export, design versioning (gAmUssA, MIT) — needs CadQuery installed | 5 | 124K |
| [`packbox/`](tools/README.md#packbox) | Tool (link only) | PackBox Studio: local packaging app — parametric dielines, artwork editor, 3D fold preview; Electron/Vite, needs Node (sbarrak, MIT) | — | 4.4M |
| [`packaging-dieline-generator/`](tools/README.md#packaging-dieline-generator) | Tool (link only) | Offline box dieline generator: dimensions + board thickness → 1:1 mm SVG or PDF; single HTML in `release/` (NealZhouPanda, MIT) | — | 43M |
| [`loom/`](skills/loom/) | Skill | `loom-textures`: seamless game textures & PBR materials as JS code (bricks, stone, wood, metal, rust, lava, sci-fi…) → albedo/normal/height/roughness/metallic/AO/ORM/emissive + lit previews, seam check, live viewer; local, needs Node ≥22.18 + `npm install` (uilianks, MIT) | 1 | 7.2M |
| [`shader-skills/`](skills/shader-skills/) | Skill | `shader-art-coding`: procedural GLSL/Shadertoy shaders — noise/fBm, SDF raymarching, terrain, water, clouds, generative art; bundler + checker + examples (gokayfem, MIT) | 1 | 8.1M |
| [`scenario-skills/`](skills/scenario-skills/) | Tool+Skill | Scenario AI skills: seamless/tileable textures, tile-preserving upscale, PBR retexture (`scenario-textures`, `scenario-patina-retexture`), plus image/video/audio/3D gen and Blender/Maya/ZBrush/Unreal/Unity/Godot/Roblox experts — **generation needs the Scenario MCP (paid account)** (scenario-labs, MIT) — `tests/` removed | 167 | 28M |
| [`Materialize/`](tools/README.md#materialize) | Tool (link only) | Materialize: photo → PBR maps (height, normal, metallic, smoothness, edge, AO) with live preview, to replicate real materials; folder is the Unity source project — get the Windows build from the repo's Releases (Bounding Box Software, GPL-3.0) | — | 32M |
| [`archify/`](skills/archify/) | Tool+Skill | Full diagram-tool repo (~313MB: website, viewer, benchmarks) — only its 2 skills kept: `archify` (architecture/flow/sequence diagrams as HTML) + `archify-review` (repo-maintainer only) (tt-a1i) | 2 | 8.6M |
| [`Agent-Reach/`](skills/Agent-Reach/) | Tool+Skill | CLI that reads/searches Twitter/Reddit/YouTube/GitHub/Bilibili/XHS, no API keys — only the skill wrapper kept, **needs the `agent-reach` CLI installed** (Panniantong) | 1 | 104K |
| [`VoiceStudio/`](skills/VoiceStudio/) | Tool+Skill | Local ElevenLabs-alternative voice app (Electron+backend+frontend) — only `skills/` kept, **needs VoiceStudio installed and running** (debpalash) | 2 | 64K |
| [`open-design-skills/`](skills/open-design-skills/) | Skill | `skills/` + `design-systems/` + `design-templates/` from nexu-io/open-design | 162 + 152 + 113 | 22M |
| [`animation-principles/`](skills/animation-principles/) | Skill | Disney's 12 animation principles, indexed 12 ways — domain, role, UI element, tool/framework, timing, emotion… (dylantarre) | 144 | 1.6M |
| [`social-media-skills/`](skills/social-media-skills/) | Skill | Social-media ops: content, analytics, campaigns, community, tools (canva, capcut) (social-media-skills) | 106 | 3.8M |
| [`html-anything-skills/`](skills/html-anything-skills/) | Skill | HTML deliverable templates from nexu-io/html-anything | 81 | 1.7M |
| [`designer-skills/`](skills/designer-skills/) | Skill | UX process: research, systems, ops, interaction, strategy, critique (Owl-Listener) — see `INDEX.md` | 107 | 1.1M |
| [`motion-skills/`](skills/motion-skills/) | Skill | Motion graphics/video/animation, 15 packs (iart-ai): TikTok, explainers, data charts, web/GSAP, WebGL/3D, Manim, ecommerce, ads, kinetic type | 51 | 1.9M |
| [`claude-ads/`](skills/claude-ads/) | Skill | Paid ads across 12 platforms: audit, budget, creative, attribution (AgriciDaniel) — `ads/` is the root conductor | 34 | 617K |
| [`ui-ux-pro-max/`](skills/ui-ux-pro-max/) | Skill | UI/UX design-intelligence DB, branding, styling, slides (nextlevelbuilder) | 7 | 11M |
| [`pixel2motion/`](skills/pixel2motion/) | Skill | Image/pixel-art → motion/video (nolangz) | 1 | 228K |
| [`video-production-skills/`](skills/video-production-skills/) | Skill | HyperFrames/Remotion video: motion direction, text openers, dark-SaaS style, reference-replica QC (Pluviobyte) | 4 | 196K |
| [`content-skills/`](skills/content-skills/) | Skill | Viral short-form content: hooks, captions/CTAs, platform formats (vyralcontent) | 7 | 760K |
| [`taste-skill/`](skills/taste-skill/) | Skill | Anti-slop frontend/design skills (Leonxlnx) | 14 | 360K |
| [`motion-design-skill/`](skills/motion-design-skill/) | Skill | Lottie/dotLottie-aware motion design (LottieFiles) | 1 | 92K |
| [`motion-dev-animations-skill/`](skills/motion-dev-animations-skill/) | Skill | Motion.dev (Framer Motion successor) animations for React/Next.js/Svelte/Astro, 120fps GPU-accelerated (199-biotechnologies) | 1 | 137K |
| [`awesome-design-skills/`](skills/awesome-design-skills/) | Skill | `SKILL.md` + `DESIGN.md` style systems (bergside) | 68 | 632K |
| [`html-ppt-skill/`](skills/html-ppt-skill/) | Skill | HTML PPT Studio: 36 themes, decks, layouts, animations (lewislulu) — keeps `.git` | 1 | 21M |
| [`huashu-design/`](skills/huashu-design/) | Skill | 花叔Design: HTML prototypes, slides, GSAP animation, MP4/GIF export, review | 1 | 32M |
| [`superpowers/`](skills/superpowers/) | Skill | Plan → execute → verify workflow: brainstorming, writing-plans, TDD, systematic-debugging, subagent-driven dev (obra, MIT) — `hooks/` inert unless installed as plugin | 15 | 2.0M |
| [`karpathy-skills/`](skills/karpathy-skills/) | Skill | Karpathy-inspired coding guidelines: think first, simplicity, surgical changes, goal-driven (forrestchang/multica-ai; third-party, not by Karpathy) | 1 | 57K |
| [`mattpocock-skills/`](skills/mattpocock-skills/) | Skill | Matt Pocock's `.claude` skills: PRD, TDD, refactor, git safety (MIT) | 38 | 1.1M |
| [`everything-claude-code/`](skills/everything-claude-code/) | Skill | Full affaan-m/ECC monorepo: 1000+ skills incl. translated copies under `docs/`, agents, hooks (MIT) — supersets `ecc-affaan-skills/` | 1068 | 70M |
| [`anthropic-skills-official/`](skills/anthropic-skills-official/) | Skill | Official `anthropics/skills` (2026-10-28 snapshot): mcp-builder, webapp-testing, skill-creator, docx/pdf/pptx/xlsx, theme-factory… — newer than the copies in `awesome-claude-skills/` | 20 | 13M |
| [`supabase-agent-skills/`](skills/supabase-agent-skills/) | Skill | Official Supabase: `postgres-best-practices` (schema, indexes, RLS) + supabase (MIT) | 2 | 374K |
| [`onewave-claude-skills/`](skills/onewave-claude-skills/) | Skill | 233 mixed skills incl. `database-schema-designer` (DDL + rollback migrations) and `database-migrator` (OneWave-AI, MIT) | 233 | 8.5M |
| [`minecraft-agent-skills/`](skills/minecraft-agent-skills/) | Skill | Minecraft: NeoForge/Fabric modding, Architectury multiloader, plugins, datapacks (Jahrome907, MIT) | 61 | 3.0M |
| [`minecraft-dev-skill/`](skills/minecraft-dev-skill/) | Skill | Minecraft Java 1.21.1–26.2: Fabric, NeoForge, Paper, Bukkit/Spigot, server ops — copy whole folders, not just SKILL.md (Extez61, MIT) | 6 | 732K |
| [`minecraft-mod-dev/`](skills/minecraft-mod-dev/) | Skill | NeoForge/Fabric mod dev; fetches current loader docs; JEI/AE2/Create integration (chouzz) | 1 | 23K |
| [`minecraft-forge-skills/`](skills/minecraft-forge-skills/) | Skill | Forge, NeoForge, NeoGradle, GregTech Modern, Bedrock GameTest — no Fabric (mrquentin) | 5 | 105K |
| [`minecraft-mod-builder/`](skills/minecraft-mod-builder/) | Skill | Step-by-step first-mod guide, Fabric or NeoForge (Riloox) | 1 | 75K |
| [`sourcepawn-l4d2/`](skills/sourcepawn-l4d2/) | Skill | Left 4 Dead 2 SourceMod plugins: write/review/debug/compile, Left4DHooks refs (Mart-User, GPL-3.0) — pairs with the `l4d2` MCP for live server testing | 1 | 5.7M |
| [`awesome-gamedev-agent-skills/`](skills/awesome-gamedev-agent-skills/) | Skill | Game dev by engine: Godot (15), Unity (8), Roblox/Luau, more (gamedev-skills, Apache-2.0) | 78 | 4.2M |
| [`claude-video/`](skills/claude-video/) | Skill | `watch`: download a video (yt-dlp), extract frames + transcript so Claude can analyze it (bradautomates, MIT) — needs yt-dlp + ffmpeg | 1 | 557K |
| [`ykdojo-yt-dlp/`](skills/ykdojo-yt-dlp/) | Skill | yt-dlp: video, audio, subtitles from YouTube and 1000+ sites (ykdojo/safeclaw) | 1 | 4K |
| [`daymade-claude-code-skills/`](skills/daymade-claude-code-skills/) | Skill | 121 mixed skills incl. `youtube-downloader` (HLS, transcripts), `video-comparer` (daymade, MIT) | 121 | 34M |
| [`OpenMontage/`](skills/OpenMontage/) | Tool+Skill | Agentic video production system: 140 skills (Remotion, HyperFrames, ffmpeg, video-edit/download/translate/understand, avatars, music-to-video) — skills live in `.claude/skills` + `.agents/skills`; full pipelines need its Python app (calesthio, **AGPL-3.0**) | 140 | 91M |
| [`remotion-skills-official/`](skills/remotion-skills-official/) | Skill | Official Remotion skills (remotion-dev/skills): best-practices, create, render, captions, upgrade… — Remotion itself runs via `npx` per project | 12 | 3.0M |
| [`hyperframes-official/`](skills/hyperframes-official/) | Skill | Official HyperFrames skills (heygen-com, Apache-2.0): hyperframes, -cli, -registry, media-use, remotion-to-hyperframes, slideshow, figma + `.claude/skills` (captions-overlay, cut-the-curve, motion-doctrine…) — skill payload only; the 108M `registry/` blocks and app source left out; CLI via `npx hyperframes` | 13 | 22M |
| [`ffmpeg-skill/`](skills/ffmpeg-skill/) | Tool+Skill | Local editor for agents: 42 FFmpeg tools (cut, captions, reframe, loudness, platform exports) + an MCP server — MCP not installed (kajisho5, MIT) | 14 | 22M |
| [`cut-as-code/`](skills/cut-as-code/) | Skill | Video editing as code: video-understand → cut, captions, b-roll, content cards, motion graphics (343M recipe library), color grade, `video-to-shorts` (WhiteTowerAI, MIT) | 10 | 357M |
| [`talking-head-rough-cut/`](skills/talking-head-rough-cut/) | Skill | Rough cut for talking-head clips: join, remove silences/filler, keep last take, transcribe (ffmpeg + whisper.cpp; Win/macOS/Linux) (vincentventalon, MIT) | 2 | 852K |
| [`video-editing-ffmpeg-whisper/`](skills/video-editing-ffmpeg-whisper/) | Skill | Trim, jump cut, captions (Hormozi/standard/minimal), text overlay, speed — Bash + FFmpeg + Whisper (6missedcalls, MIT) | 1 | 86K |
| [`cut-video/`](skills/cut-video/) | Skill | Tighten long recordings: remove silences/ums/dead air, keep laughs and comedic pauses (louisedesadeleer, MIT) | 1 | 72K |
| [`rondoflow/`](skills/rondoflow/) | Tool+Skill | RondoFlow skill catalog: 2320 aggregated skills (`catalog/skills/*`, e.g. `download-videos-from-sites`, `download-videos-audio-with-ytdlp`) + agents/canvas templates; the visual multi-agent app itself left out (rondoflow, MIT — see `THIRD_PARTY_NOTICES.md`) | 2320 | 26M |
| [`awesome-claude-code/`](skills/awesome-claude-code/) | Not skills | Curated list of Claude Code skills, hooks, commands, plugins (hesreallyhim) — links out | — | 3.5M |
| [`awesome-claude-design/`](skills/awesome-claude-design/) | Not skills | Curated index of `DESIGN.md` files (VoltAgent) — `README.md` only, links out | — | 24K |
| [`behisecc-awesome-claude-skills/`](skills/behisecc-awesome-claude-skills/) | Not skills | Curated awesome-list of Claude Skills by category (BehiSecc) — `README.md` only, links out to external repos; nothing invocable here | — | 264K |
| [`claude-quickstarts/`](skills/claude-quickstarts/) | Not skills | Anthropic example apps — reference only (see `NOTE.md`) | — | 8.5M |

## Skill vs Tool+Skill vs Not skills

- **Not brought in at all** (fully app, zero SKILL.md found): `webadderallorg/Recordly`
  (screen recorder). See `Not brought in` note below the table in `use-skills/SKILL.md`.
- **Batch 2026-10-19 — omitted on purpose**: `remotion-dev/remotion`, `FFmpeg/FFmpeg` and
  `openai/whisper` are upstream tools/libraries (React video framework, media transcoder,
  ASR model), not skills — the video skills above call them as dependencies, so they
  weren't imported as folders. Already present, so skipped as duplicates:
  `haidrrrry/claude-remotion-skill` (→ `claude-remotion-skill/`),
  `nopefallacy/vertical-video-editing-skills` (→ `vertical-video-editing-skills/`),
  `ComposioHQ/awesome-claude-skills` (→ `awesome-claude-skills/`).
- **Tool+Skill** folders (`archify`, `Agent-Reach`, `VoiceStudio`, and `composio-skills/`
  inside `awesome-claude-skills`) only work fully if the underlying tool/CLI/MCP server
  is actually present — the skill alone won't reproduce the app's behavior, it's a
  connector. Say so before promising results from one of these.

## Overlap note

`taste-skill`, the style systems in `awesome-design-skills`, and several `open-design-skills/skills/*`
share upstream lineage (taste-skill, stitch, brandkit, etc.). `open-design-skills` is the widest
superset. When looking for a design direction, start there or in `awesome-design-skills`.
