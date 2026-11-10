# D:\Skills — Mapa por temas

Dos formas de buscar una skill:

1. **Este archivo (`TEMAS.md`)** — mapa por *propósito*: ¿qué quieres hacer? (code, web,
   diseño, vídeo, audio, animación, contenido…). Te lleva a la carpeta/skill correcta.
2. **[`CATALOG.md`](CATALOG.md)** — índice plano de las 2297 entradas. Haz Ctrl-F por
   palabra clave y abre el `SKILL.md`/`DESIGN.md` de la ruta indicada.

Y en cualquier proyecto, di **"usa skills"** para que se elija y aplique la mejor
automáticamente (dispatcher en [`use-skills`](use-skills/)).

**Leyenda de tipo** — **Skill**: payload de skill listo para usar. **Tool+Skill**:
necesita un CLI/app/MCP externo instalado o corriendo. **Tool**: la herramienta upstream
tal cual, sin `SKILL.md` — se usa directamente (CLI, add-on, app). **Ref**: solo
referencia, nada invocable.

---

## 💻 Code & Ingeniería
Revisión, testing, arquitectura, metodología de agentes de código.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`eng-review-skills/`](eng-review-skills/) | Skill | Revisión/auditoría: BD, testing, fiabilidad (idempotency/outbox), API, frontend, concurrencia — checklist + red flags + fix | 32 |
| [`agent-skills-addyosmani/`](agent-skills-addyosmani/) | Skill | Ingeniería de extremo a extremo (Addy Osmani): TDD, spec-driven, debugging, seguridad, perf, CI/CD, git workflow, shipping | 25 |
| [`caveman/`](caveman/) | Skill | Metodología coding-agent: explorar, refactor seguro, migrar, revisar con evidencia, modo "caveman" | 20 |
| [`ant-design/`](ant-design/) | Skill | `usage-skills/` para construir con Ant Design (v4→v5, theme tokens); `maintainer-skills/` para mantener el repo | 9 |
| [`security-audit-skill/`](security-audit-skill/) | Skill | Auditoría de seguridad multi-fase con hallazgos verificados (Cloudflare, oficial) | 1 |
| [`archify/`](archify/) | Tool+Skill | Diagramas de arquitectura/flujo/secuencia como HTML explorable (+ `archify-review`, solo mantenedor) | 2 |
| [`fabricjs/`](fabricjs/) | Tool+Skill | Solo skill de mantenedor para abrir PRs contra fabric.js (no es "construir con Fabric") | 1 |
| [`master-skills/skills/build`](master-skills/skills/build) | Skill | De idea a app/web funcionando: spec, stack mínimo, dirección de diseño, build verificado, QA en navegador, deploy | — |

También en **awesome-claude-skills** (ver Automatización): `security-review`, `testing` (Playwright), `skill-creator`, `mcp-builder`.

---

## 🌐 Web & Frontend
Landing pages, portfolios, sitios, prototipos HTML, componentes.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`taste-skill/`](taste-skill/) | Skill | Frontend/diseño anti-slop: landing, portfolios, rediseños, calidad Awwwards | 14 |
| [`impeccable/`](impeccable/) | Skill | Revisor/constructor de craft de UI a nivel de código | 1 |
| [`html-anything-skills/`](html-anything-skills/) | Skill | Plantillas de entregable HTML autocontenido: artículos, cards, prototipos, reportes, résumés | 81 |
| [`huashu-design/`](huashu-design/) | Skill | 花叔Design: prototipos HTML, slides, GSAP, export MP4/GIF, review | 1 |
| [`ant-design/`](ant-design/) | Skill | Construir UIs con Ant Design (ver Code) | 9 |
| [`open-design-skills/design-templates/`](open-design-skills/design-templates/) | Skill | Plantillas HTML completas: dashboards, pitch books, artefactos | 113 |

Para la **estética/estilo** del sitio, ve a 🎨 Diseño.

---

## 🎨 Diseño (sistemas, UI, branding)
Direcciones visuales, design systems con tokens, UI kits.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`open-design-skills/design-systems/`](open-design-skills/design-systems/) | Skill | 152 sistemas: cada uno DESIGN.md + tokens.css + design-tokens.json + tailwind-v4.css. Elige por marca/estética | 152 |
| [`open-design-skills/skills/`](open-design-skills/skills/) | Skill | Superset más amplio: direcciones de diseño, extracción, crítica, gen. de imagen/audio | 162 |
| [`awesome-design-skills/`](awesome-design-skills/) | Skill | Sistemas de estilo (SKILL.md + DESIGN.md). Elige por estética | 68 |
| [`ui-ux-pro-max/`](ui-ux-pro-max/) | Skill | Inteligencia de diseño consultable + branding + styling + slides | 7 |

> **Solapamiento**: `taste-skill`, `awesome-design-skills` y varias de `open-design-skills/skills` comparten linaje. `open-design-skills` es el superset más amplio — empieza ahí.

---

## 🧭 UX (research & proceso)
Heurísticas, personas, journey maps, estrategia, crítica. Conocimiento (no genera archivos).

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`designer-skills/`](designer-skills/) | Skill | Proceso UX: research, sistemas, ops, interacción, estrategia, crítica — ver `INDEX.md` | 107 |
| [`awesome-ux-skills/`](awesome-ux-skills/) | Skill | Heurísticas, personas, journey/storyboard, double-diamond, accesibilidad, Dieter Rams | 23 |

---

## 🎬 Vídeo (edición & producción)
Editar footage real, reels verticales, motion graphics programático con Remotion.

| Carpeta / skill | Tipo | Qué | Nº |
|---|---|---|---|
| [`video-use/`](video-use/) | Skill | Edita cualquier vídeo por conversación: transcribe, corta, color grade, overlays, subtítulos (+ manim-video) | 2 |
| [`ecc-affaan-skills/skills/video-editing`](ecc-affaan-skills/skills/video-editing) | Skill | Pipeline footage real: FFmpeg→Remotion→ElevenLabs→fal.ai→Descript/CapCut | — |
| [`ecc-video-editing/`](ecc-video-editing/) | Skill | Pipeline de edición AI para footage real (mit-network/everything-claude-code) | 1 |
| [`vertical-video-editing-skills/`](vertical-video-editing-skills/) | Skill | Script + talking-head/voiceover → short 9:16 vía HyperFrames | 1 |
| [`video-editor-plugin/`](video-editor-plugin/) | Skill | Edición general: trim/compress/merge/resize/captions/title cards/GIFs/watermarks | 1 |
| [`video-production-skills/`](video-production-skills/) | Skill | HyperFrames/Remotion: dirección de motion, openers, estilo SaaS oscuro, QC de réplica | 4 |
| [`claude-remotion-skill/`](claude-remotion-skill/) | Skill | Remotion (React→MP4): intros/outros/logos/reels/promos, animación de texto | 1 |
| [`ecc-affaan-skills/skills/remotion-video-creation`](ecc-affaan-skills/skills/remotion-video-creation) | Skill | 29 reglas Remotion: 3D, animaciones, audio, captions, charts, transiciones | — |
| [`video-motion-craft/`](video-motion-craft/) | Skill | Remotion + FFmpeg/Whisper (trim, jump-cut, captions, overlays) | 1 |
| [`remotion-ffmpeg-video-skill/`](remotion-ffmpeg-video-skill/) | Skill | Remotion + FFmpeg | 1 |
| [`master-skills/skills/edit`](master-skills/skills/edit) | Skill | Corta dead space, añade captions y visuales dinámicos, stop-motion | — |
| [`pixel2motion/`](pixel2motion/) | Skill | Imágenes/pixel-art → motion/vídeo | 1 |
| [`brag/`](brag/) | Skill | Código de un proyecto → vídeo de lanzamiento vía Hyperframes | 1 |
| [`jianshuo-claude-skills/`](jianshuo-claude-skills/) | Skill | Producción de vídeo (王建硕): subtítulos, dubbing, reframe, multicam, overlay, segmentación, texto→vídeo, localización | ~15 |

> Remotion, FFmpeg y Whisper son **herramientas upstream** (framework React de vídeo, transcodificador, ASR) que estas skills usan como dependencias; no están como carpetas aquí.

---

## 🔊 Audio & Voz
Clonado de voz, dubbing, transcripción, TTS, generación de audio.

| Carpeta / skill | Tipo | Qué | Nº |
|---|---|---|---|
| [`tts-voice-bank/`](tts-voice-bank/) | Tool | Banco de voces TTS rápidas: `voz.py` (edge-tts, 19 presets: narrador YouTube, tiktok, loquendo, robot, ardilla, acentos) + guía TikTok TTS / Loquendo / Zueira / webs gratis / Piper-Kokoro offline | 1 |
| [`VoiceStudio/`](VoiceStudio/) | Tool+Skill | App local tipo ElevenLabs: clonar voz, dubbing, transcripción — necesita VoiceStudio corriendo | 2 |
| [`ecc-affaan-skills/skills/fal-ai-media`](ecc-affaan-skills/skills/fal-ai-media) | Skill | Gen. de imagen/vídeo/**audio** (TTS CSM-1B, video→audio ThinkSound) vía fal.ai MCP | — |
| `jianshuo-claude-skills/` dubbing/transcribing/voicedrop | Tool+Skill | [`wjs-dubbing-video`](jianshuo-claude-skills/wjs-dubbing-video), [`wjs-transcribing-audio`](jianshuo-claude-skills/wjs-transcribing-audio), [`wjs-translating-subtitles`](jianshuo-claude-skills/wjs-translating-subtitles), [`wjs-voicedrop`](jianshuo-claude-skills/wjs-voicedrop) (necesita MCP voicedrop.cn) | — |

---

## 🎞️ Animación & Motion graphics
Principios, tipografía cinética, Lottie, Motion.dev, GSAP, animación web/UI.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`animation-principles/`](animation-principles/) | Skill | Los 12 principios de Disney, indexados 12 formas (dominio, rol, elemento UI, tool, timing, emoción…) | 144 |
| [`motion-skills/`](motion-skills/) | Skill | 15 packs: TikTok, explainers, data charts, web/GSAP, WebGL/3D, Manim, ecommerce, ads, tipografía cinética | 51 |
| [`emilkowalski-skills/`](emilkowalski-skills/) | Skill | Craft de animación/UI (Vercel, Sonner/Vaul, animations.dev) | 13 |
| [`motion-design-skill/`](motion-design-skill/) | Skill | Animación consciente de Lottie/dotLottie (LottieFiles) | 1 |
| [`motion-dev-animations-skill/`](motion-dev-animations-skill/) | Skill | Motion.dev (sucesor de Framer Motion): React/Next/Svelte/Astro, 120fps GPU | 1 |

---

## 🧍 Personajes 2D (rigging & animación)
De arte/PSD a personaje animable; sprites de juego; After Effects.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`live2d-from-art/`](live2d-from-art/) | Skill | Live2D interactivo desde arte o PNG/PSD por capas — cutout, inpaint, mesh+param, MOC3 | 1 |
| [`live2d-agent-kit/`](live2d-agent-kit/) | Skill | Live2D vía psd2live, super-res, validación Cubism real, empaquetado VTube Studio | 1 |
| [`PuppetLoom/`](PuppetLoom/) | Tool+Skill | Personajes 2D animables desde PSD por capas vía CLI PuppetLoom | 1 |
| [`spine-animation-ai/`](spine-animation-ai/) | Skill | Animación esquelética Spine 2D dirigida por IA | 1 |
| [`svg-character-animator/`](svg-character-animator/) | Skill | Máquina de estados de personaje/mascota SVG — morph poses/emociones, idle, export iOS/SwiftUI | 1 |
| [`character-animation-skill/`](character-animation-skill/) | Skill | Animación de personaje | 1 |
| [`img2game2d/`](img2game2d/) | Skill | Concept art → assets 2D de juego: sprite sheets, rigs, atlases, export Godot/Unity/Spine/Phaser/PixiJS | 1 |
| [`MotionLoom/`](MotionLoom/) | Tool+Skill | Producción de animación project-aware con evidencia de runtime y handoff review-first | 1 |
| [`ae-agent-skills/`](ae-agent-skills/) | Tool+Skill | Edición After Effects vía `ae-cli`: escenas JSON declarativas + edición comando a comando | 2 |

---

## 🖼️ Imagen & Arte / Assets
Generación y manipulación de imagen, PSD por capas.

| Carpeta / skill | Tipo | Qué | Nº |
|---|---|---|---|
| [`gpt-image2-layered-psd/`](gpt-image2-layered-psd/) | Skill | Divide una imagen en PNGs de elementos semánticos + ensambla un PSD editable por capas | 1 |
| [`img2game2d/`](img2game2d/) | Skill | Concept art → assets de juego (ver Personajes 2D) | 1 |
| [`ecc-affaan-skills/skills/fal-ai-media`](ecc-affaan-skills/skills/fal-ai-media) | Skill | Text-to-image (Nano Banana), image→video (Seedance/Kling/Veo 3) vía fal.ai | — |

También en **awesome-claude-skills**: mejora de imagen, canvas art, generación de temas.

---

## 👤 Visión facial (detección & análisis)
Detección de caras, landmarks, parsing/segmentación, atributos, reconocimiento e inferencia.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`face-analysis-skill/`](face-analysis-skill/) | Skill (autorada) | Guía de pipeline (detección → landmarks → parsing/segmentación → preprocesado → inferencia) y qué librería usar cuándo: InsightFace, MediaPipe, RetinaFace, OpenCV, YOLO, DeepFace, dlib, face-alignment, SAM2, ONNX Runtime, OpenVINO, TensorRT… Incluye notas de licencia y privacidad. Las librerías no se clonan: dice cuál instalar y cómo combinarlas | 1 |

---

## ✂️ Papercraft, troquelado & fabricación
Figuras armables, plantillas de corte, encajes simétricos, dielines de empaques, CAD paramétrico.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`Export-Paper-Model-from-Blender/`](Export-Paper-Model-from-Blender/) | Tool | Add-on de Blender: despliega un modelo 3D en piezas planas con pestañas de pegado, numeración de bordes y pliegues valle/montaña → SVG/PDF. Requiere Blender ≥5.0; manejable vía Blender MCP | — |
| [`boxes/`](boxes/) | Tool | Boxes.py: 100+ generadores de cajas para corte láser con finger joints, ranura-lengüeta, living hinges y compensación de kerf → SVG (CLI Python) | — |
| [`openscad-skills/`](openscad-skills/) | Skill | OpenSCAD + BOSL2: planificar modelos paramétricos, organizers de juegos de mesa; `projection()` → SVG/DXF para cortar | 4 |
| [`cadquery-skills/`](cadquery-skills/) | Skill | CadQuery: planificar, generar código, ensamblajes con restricciones, exportar (STL/STEP/SVG/DXF), versionar diseños | 5 |
| [`packbox/`](packbox/) | Tool | PackBox Studio: dielines de empaques + editor de arte + preview 3D del plegado (Electron, requiere Node) | — |
| [`packaging-dieline-generator/`](packaging-dieline-generator/) | Tool | Dielines de cajas a partir de medidas y grosor de cartón → SVG 1:1 mm / PDF; un solo HTML en `release/` | — |

Para papercraft de figuras: modelo en Blender (o `open-design-skills/skills/fal-3d`) →
`Export-Paper-Model` → PDF con las skills de pdf. Para encajes exactos: `boxes/` u OpenSCAD.

---

## 🧱 Texturas HD, PBR & materiales
Texturas seamless/tileables, mapas PBR (albedo, normal, height, roughness, metallic, AO), réplica de materiales desde foto, upscale.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`loom/`](loom/) | Skill | **Primera opción, local y gratis.** Texturas seamless por construcción escritas como código JS (ladrillo, piedra, madera, metal, óxido, lava, sci-fi…) → todos los mapas PBR + preview iluminada, aviso de costuras, visor en vivo. Requiere Node ≥22.18 y `npm install` | 1 |
| [`Materialize/`](Materialize/) | Tool | **Réplica desde foto**: foto de una superficie → height, normal, metallic, smoothness, AO. Proyecto Unity; usar el build de Windows de Releases | — |
| [`scenario-skills/`](scenario-skills/) | Tool+Skill | `scenario-textures` (tileables desde texto o referencia, packs temáticos, upscale 2×–8× sin romper el tile), `scenario-patina-retexture` (PBR sobre una malla), `dcc/blender/scenario-blender-texturing-shading` y `-uv-baking`, `game-engines/unreal/scenario-unreal-materials`. Necesita el MCP de Scenario (de pago) | 167 |
| [`shader-skills/`](shader-skills/) | Skill | Texturas procedurales en GLSL (ruido, terreno, agua, nubes): resolución ilimitada, para web/juegos | 1 |

Flujo típico: genera o replica la base (`loom`, Materialize, `fal-generate`/`fal-image-edit`) →
upscale (`fal-upscale`, `scenario-textures`) → aplicar/hornear en Blender vía Blender MCP.

---

## ✍️ Contenido & Social
Short-form viral, hooks/captions, publicación, crecimiento, X/Twitter, YouTube.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`social-media-skills/`](social-media-skills/) | Skill | Operación de redes: contenido, analítica, campañas, comunidad, herramientas (canva, capcut), audiencia | 106 |
| [`content-skills/`](content-skills/) | Skill | Contenido viral corto: hooks, captions/CTAs, formatos por plataforma (TikTok, Reels, Shorts) | 7 |
| [`master-skills/skills/virality`](master-skills/skills/virality) | Skill | Encuentra lo que funciona (LinkedIn+YouTube) y lo reescribe en tu voz → guion short-form | — |
| [`jianshuo-claude-skills/`](jianshuo-claude-skills/) | Skill/Tool+Skill | Publicación (Hugo, WeChat, 小红书, X, App Store, TestFlight), minería/reescritura de artículos, crecimiento en X | ~20 |

---

## 📣 Ads & Marketing
Publicidad paga multi-plataforma.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`claude-ads/`](claude-ads/) | Skill | 12 plataformas (Google/Meta/YouTube/LinkedIn/TikTok/Microsoft/Apple/Amazon/Reddit/Pinterest/Snapchat/X): auditoría, presupuesto, creatividad, atribución. `ads/` es el conductor raíz | 34 |

---

## 📄 Docs & Slides
Documentos, presentaciones, decks.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`awesome-claude-skills/document-skills/`](awesome-claude-skills/document-skills/) | Skill | Los estándar docx / pdf / pptx / xlsx | 4 |
| [`html-ppt-skill/`](html-ppt-skill/) | Skill | HTML PPT Studio: 36 temas, decks, layouts, animaciones | 1 |
| [`open-design-skills/design-templates/`](open-design-skills/design-templates/) | Skill | Decks y pitch books HTML (ver Web) | 113 |

---

## 🔌 Automatización (MCP / conectores externos)
Requieren un servidor MCP o CLI externo conectado.

| Carpeta | Tipo | Qué | Nº |
|---|---|---|---|
| [`awesome-claude-skills/composio-skills/`](awesome-claude-skills/composio-skills/) | Tool+Skill | 832 stubs `<app>-automation` (Slack, Notion, Gmail, Adobe, Ahrefs…) — **necesitan el MCP Rube conectado** | 832 |
| [`awesome-claude-skills/`](awesome-claude-skills/) (top-level) | Skill | 28 generalistas: artifacts, branding, changelog, escritura, growth, dominios, facturas, resumes, Twitter, YouTube, testing Playwright, crear skills/MCP | 28 |
| [`Agent-Reach/`](Agent-Reach/) | Tool+Skill | Lee/busca Twitter/Reddit/YouTube/GitHub/Bilibili/XHS sin API keys — **necesita el CLI agent-reach** | 1 |

---

## 📚 Referencia (no son skills)
No invocable; material de consulta o índices que enlazan fuera.

| Carpeta | Qué |
|---|---|
| [`reference-docs/`](reference-docs/) | Fuentes autoritativas (OWASP, Google eng-practices, system-design-primer, clean-code-js, redis-doc) — base de `eng-review-skills` |
| [`awesome-claude-design/`](awesome-claude-design/) | Índice curado de archivos `DESIGN.md` (VoltAgent) — enlaza fuera |
| [`behisecc-awesome-claude-skills/`](behisecc-awesome-claude-skills/) | Awesome-list de Claude Skills por categoría (BehiSecc) — enlaza fuera |
| [`claude-code-video-toolkit/`](claude-code-video-toolkit/) | README que apunta a herramientas de producción de vídeo |
| [`claude-quickstarts/`](claude-quickstarts/) | Apps de ejemplo de Anthropic |

---

_Para el índice completo, buscable línea por línea, ve a [`CATALOG.md`](CATALOG.md). Al
añadir repos nuevos: regenera el catálogo (`python .catalog/build_catalog.py`) y actualiza
este mapa y la tabla del [`README.md`](README.md)._
