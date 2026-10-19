# -*- coding: utf-8 -*-
import glob, os, re, io

BASE = "D:/Skills"

def read(p):
    return io.open(p, encoding="utf-8", errors="replace").read()

def frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    body = m.group(1)
    fm = {}
    # split top-level keys
    cur = None
    buf = []
    def flush():
        if cur is not None:
            v = "\n".join(buf).strip()
            v = v.strip('"\'')
            fm[cur] = v
    for line in body.split("\n"):
        km = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", line)
        if km and not line.startswith(" ") and not line.startswith("\t"):
            flush()
            cur = km.group(1).strip()
            rest = km.group(2).strip()
            if rest in ("|", ">", "|-", ">-", "|+", ">+"):
                buf = []
            else:
                buf = [rest]
        else:
            buf.append(line.strip())
    flush()
    return fm

def clean(s, n=240):
    if not s:
        return ""
    s = " ".join(s.split())
    s = s.strip('"\'|> ').strip()
    if len(s) > n:
        s = s[:n-1].rstrip() + "…"
    return s

def entry(name, desc, path, tags=""):
    rel = path.replace("\\", "/").replace(BASE + "/", "")
    line = f"- **{name}** — {desc}"
    if tags:
        line += f"  _[{tags}]_"
    line += f"  · `{rel}`"
    return line

out = []
out.append("# D:\\Skills — Catálogo plano\n")
out.append("Índice de una línea por skill / design-system / template. Búscalo con Ctrl-F por palabra clave, "
           "luego abre el `SKILL.md` / `DESIGN.md` de la ruta indicada.\n")
out.append("Generado por `scratchpad/build_catalog.py`. Regenerar al añadir repos.\n")

def section(title, hint):
    out.append(f"\n## {title}\n")
    if hint:
        out.append(f"_{hint}_\n")

total = 0

# 1. open-design-skills/skills
section("open-design-skills / skills (162)",
        "Superset más amplio: direcciones de diseño, plantillas de deck/card/artículo/vídeo, extracción, crítica, motion, gen. imagen/audio.")
rows = []
for f in sorted(glob.glob(f"{BASE}/open-design-skills/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description","")), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 2. open-design-skills/design-systems
section("open-design-skills / design-systems (152)",
        "Cada uno: DESIGN.md + tokens.css + design-tokens.json + tailwind-v4.css. Se aplican como sistema de diseño. Elige por nombre de marca/estética.")
rows = []
for f in sorted(glob.glob(f"{BASE}/open-design-skills/design-systems/*/DESIGN.md")):
    t = read(f)
    name = os.path.basename(os.path.dirname(f))
    cat = ""
    desc = ""
    cm = re.search(r"^>\s*Category:\s*(.+)$", t, re.M)
    if cm: cat = cm.group(1).strip()
    # first '>' quote line that's not the Category line
    for qm in re.finditer(r"^>\s*(.+)$", t, re.M):
        line = qm.group(1).strip()
        if not line.lower().startswith("category:"):
            desc = line
            break
    d = clean(desc, 160)
    if cat:
        d = f"({cat}) {d}"
    rows.append(entry(name, d, os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 3. open-design-skills/design-templates
section("open-design-skills / design-templates (113)",
        "Plantillas de salida HTML completas con assets: decks, dashboards, pitch books, hyperframes, artefactos.")
rows = []
for f in sorted(glob.glob(f"{BASE}/open-design-skills/design-templates/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    tags = ", ".join(re.findall(r'[\w-]{3,}', fm.get("tags","")))[:70]
    rows.append(entry(name, clean(fm.get("description","") or fm.get("en_description",""), 200),
                      os.path.dirname(f), tags))
total += len(rows); out.append("\n".join(rows) + "\n")

# 4. html-anything-skills
section("html-anything-skills (81)",
        "Plantillas de entregable HTML autocontenido (SKILL.md + example.html). Artículos, cards, prototipos, reportes, résumés, vídeo-frames.")
rows = []
for f in sorted(glob.glob(f"{BASE}/html-anything-skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    cat = clean(fm.get("category",""), 20)
    rows.append(entry(name, clean(fm.get("description",""), 200), os.path.dirname(f), cat))
total += len(rows); out.append("\n".join(rows) + "\n")

# 5. ui-ux-pro-max
section("ui-ux-pro-max (7)",
        "Inteligencia de diseño consultable + branding + styling + slides.")
rows = []
for f in sorted(glob.glob(f"{BASE}/ui-ux-pro-max/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 260), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 6. designer-skills
section("designer-skills (107)",
        "Proceso UX: research, sistemas, ops, interacción, estrategia, crítica. Conocimiento (no genera archivos). Ver designer-skills/INDEX.md para buscador por situación.")
rows = []
for f in sorted(glob.glob(f"{BASE}/designer-skills/*/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    cat = f.replace("\\", "/").replace(BASE + "/designer-skills/", "").split("/")[0]
    rows.append(entry(name, clean(fm.get("description",""), 200), os.path.dirname(f), cat))
total += len(rows); out.append("\n".join(rows) + "\n")

# 7. taste-skill
section("taste-skill (14)",
        "Frontend/diseño anti-slop: landing, portfolios, rediseños, calidad Awwwards, gen. de imágenes.")
rows = []
for f in sorted(glob.glob(f"{BASE}/taste-skill/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 240), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 8. awesome-design-skills
section("awesome-design-skills (68)",
        "Sistemas de estilo (SKILL.md + DESIGN.md). Elige por estética.")
rows = []
for f in sorted(glob.glob(f"{BASE}/awesome-design-skills/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 180), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 9. motion-skills (15 packs)
section("motion-skills (51)",
        "Motion graphics/vídeo: tipografía cinética, gráficos animados, explainers, TikTok/Reels, 3D/WebGL, Manim, ilustración generativa, motion web. Cada pack trae su propio scripts/ (deliver-and-verify: frame, contact-sheet, probe mp4).")
rows = []
for f in sorted(glob.glob(f"{BASE}/motion-skills/*/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    pack = f.replace("\\", "/").replace(BASE + "/motion-skills/", "").split("/")[0]
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f), pack))
total += len(rows); out.append("\n".join(rows) + "\n")

# 10. content-skills
section("content-skills (7)",
        "Contenido viral corto: hooks, captions/CTAs, formatos por plataforma (TikTok, Reels, Shorts).")
rows = []
for f in sorted(glob.glob(f"{BASE}/content-skills/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 11. social-media-skills
section("social-media-skills (106)",
        "Operación de redes sociales: contenido, analítica, campañas, comunidad, herramientas (canva, capcut), investigación de audiencia.")
rows = []
for f in sorted(glob.glob(f"{BASE}/social-media-skills/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 200), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 12. claude-ads
section("claude-ads (34)",
        "Publicidad paga multi-plataforma (Google/Meta/YouTube/LinkedIn/TikTok/Microsoft/Apple/Amazon/Reddit/Pinterest/Snapchat/X): auditoría, presupuesto, creatividad, atribución. `ads/` es el conductor raíz; el resto son sub-skills por plataforma/workflow.")
rows = []
fm = frontmatter(read(f"{BASE}/claude-ads/ads/SKILL.md"))
rows.append(entry(fm.get("name","ads") + " (root)", clean(fm.get("description",""), 260), f"{BASE}/claude-ads/ads"))
for f in sorted(glob.glob(f"{BASE}/claude-ads/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 13. pixel2motion
section("pixel2motion (1)",
        "Convierte imágenes/pixel-art en motion/vídeo.")
rows = []
fm = frontmatter(read(f"{BASE}/pixel2motion/SKILL.md"))
rows.append(entry(fm.get("name","pixel2motion"), clean(fm.get("description",""), 300), f"{BASE}/pixel2motion"))
total += len(rows); out.append("\n".join(rows) + "\n")

# 14. video-production-skills
section("video-production-skills (4)",
        "Producción de vídeo con HyperFrames/Remotion: dirección de motion, openers de texto, estilo SaaS oscuro, QC de réplica de vídeo de referencia.")
rows = []
for f in sorted(glob.glob(f"{BASE}/video-production-skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 240), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 15. motion-design-skill
section("motion-design-skill (1)",
        "Skill de LottieFiles: animación consciente de Lottie/dotLottie.")
rows = []
for f in sorted(glob.glob(f"{BASE}/motion-design-skill/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 300), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 16. animation-principles
section("animation-principles (144)",
        "Disney's 12 principles of animation, indexed 12 different ways (by domain, thinking-style, role, skill-level, animation-type, emotional-outcome, UI element, industry, tool/framework, time-scale, principle-focus, problem-type). Ver animation-principles/docs/index.md.")
rows = []
for f in sorted(glob.glob(f"{BASE}/animation-principles/skills/*/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    cat = f.replace("\\", "/").replace(BASE + "/animation-principles/skills/", "").split("/")[0]
    rows.append(entry(name, clean(fm.get("description",""), 160), os.path.dirname(f), cat))
total += len(rows); out.append("\n".join(rows) + "\n")

# 17. awesome-claude-skills top-level (28 standalone)
section("awesome-claude-skills / top-level (28)",
        "Skills generalistas independientes (ComposioHQ): artifacts, branding, canvas art, changelog, ads, escritura, growth, dominios, organización de archivos/facturas, mejora de imagen, comms internas, resumes, temas, Twitter, YouTube, testing Playwright, creación de skills/MCP servers.")
rows = []
for f in sorted(glob.glob(f"{BASE}/awesome-claude-skills/*/SKILL.md")):
    parts = f.replace("\\", "/").split("/")
    if "composio-skills" in parts or "document-skills" in parts:
        continue
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 18. awesome-claude-skills/document-skills
section("awesome-claude-skills / document-skills (4)",
        "Los skills estándar docx/pdf/pptx/xlsx.")
rows = []
for f in sorted(glob.glob(f"{BASE}/awesome-claude-skills/document-skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 19. awesome-claude-skills/composio-skills
section("awesome-claude-skills / composio-skills (832)",
        "REQUIERE el servidor MCP Rube conectado (RUBE_SEARCH_TOOLS / RUBE_MANAGE_CONNECTIONS) — son prompts que llaman herramientas MCP de Composio, no workflows autónomos. Un skill `<app>-automation` por integración SaaS (Slack, Notion, Gmail, Adobe, Ahrefs, …). Verifica que el MCP esté disponible antes de aplicar uno.")
rows = []
for f in sorted(glob.glob(f"{BASE}/awesome-claude-skills/composio-skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 140), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 20. caveman
section("caveman (20)",
        "Metodología de coding-agent (JuliusBrussee): exploración, refactor seguro, migraciones, revisión con evidencia, condiciones de parada explícitas, modo de comunicación ultra-comprimido 'caveman'. skills/ es MIT; el motor Caveman en sí es BSL-1.1.")
rows = []
for f in sorted(glob.glob(f"{BASE}/caveman/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 21. brag
section("brag (1)",
        "Convierte el propio código de un proyecto en un vídeo de lanzamiento pulido vía Hyperframes (latent-spaces), sin screenshots.")
rows = []
fm = frontmatter(read(f"{BASE}/brag/brag/SKILL.md"))
rows.append(entry(fm.get("name","brag"), clean(fm.get("description",""), 300), f"{BASE}/brag/brag"))
total += len(rows); out.append("\n".join(rows) + "\n")

# 22. emilkowalski-skills
section("emilkowalski-skills (13)",
        "Skills de animación/craft UI de Emil Kowalski (Vercel, Sonner/Vaul, animations.dev).")
rows = []
for f in sorted(glob.glob(f"{BASE}/emilkowalski-skills/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 260), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 23. impeccable
section("impeccable (1)",
        "Revisor/constructor de craft de UI a nivel de código (pbakaus), mismo territorio que taste-skill/craft.")
rows = []
fm = frontmatter(read(f"{BASE}/impeccable/impeccable/SKILL.md"))
rows.append(entry(fm.get("name","impeccable"), clean(fm.get("description",""), 300), f"{BASE}/impeccable/impeccable"))
total += len(rows); out.append("\n".join(rows) + "\n")

# 24. awesome-ux-skills (flat format: <name>.md is the skill, no SKILL.md subfolder)
section("awesome-ux-skills (23)",
        "Formato plano (tommyjepsen): cada <name>.md en la raíz ES el skill. Heurísticas UX, personas, journey/storyboard, double-diamond, accesibilidad, UX persuasiva, patrones de interfaz IA, principios de Dieter Rams. Sin LICENSE upstream.")
rows = []
for f in sorted(glob.glob(f"{BASE}/awesome-ux-skills/*.md")):
    bn = os.path.basename(f)
    if bn in ("README.md", "UPSTREAM-README.md"):
        continue
    fm = frontmatter(read(f))
    name = bn[:-3]
    rows.append(entry(name, clean(fm.get("description",""), 220), f"{BASE}/awesome-ux-skills"))
total += len(rows); out.append("\n".join(rows) + "\n")

# 25. ant-design
section("ant-design (9)",
        "Del monorepo ant-design/ant-design (MIT, ~280MB, solo se extrajeron sus 2 carpetas de skills). usage-skills/ (3) para construir con Ant Design; maintainer-skills/ (6) es específico para mantener el propio repo ant-design.")
rows = []
for f in sorted(glob.glob(f"{BASE}/ant-design/*/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    tier = f.replace("\\", "/").replace(BASE + "/ant-design/", "").split("/")[0]
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f), tier))
total += len(rows); out.append("\n".join(rows) + "\n")

# 26. video-use [SKILL]
section("video-use (2) [SKILL]",
        "Edita cualquier vídeo por conversación (browser-use org): transcribe, corta, gradúa color, genera overlays, quema subtítulos. Incluye sub-skill manim-video.")
rows = []
for f in sorted(glob.glob(f"{BASE}/video-use/SKILL.md")) + sorted(glob.glob(f"{BASE}/video-use/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = fm.get("name", os.path.basename(os.path.dirname(f)))
    rows.append(entry(name, clean(fm.get("description",""), 260), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 27. agent-skills-addyosmani [SKILL]
section("agent-skills-addyosmani (25) [SKILL]",
        "Metodología de ingeniería de software de extremo a extremo (Addy Osmani/Google): API design, TDD, spec-driven, debugging, seguridad, performance, CI/CD, shipping, git workflow, doubt-driven review, etc. No es diseño/contenido.")
rows = []
for f in sorted(glob.glob(f"{BASE}/agent-skills-addyosmani/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 28. security-audit-skill [SKILL]
section("security-audit-skill (1) [SKILL]",
        "Auditoría de seguridad multi-fase con hallazgos verificados independientemente (Cloudflare, oficial).")
rows = []
for f in sorted(glob.glob(f"{BASE}/security-audit-skill/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 300), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 29. archify [TOOL/APP + skill]
section("archify (2) [TOOL/APP — con skill embebida]",
        "El repo completo (~313MB) es un producto (web, viewer, benchmarks); solo se trajeron sus 2 skills. archify = generador de diagramas de arquitectura/flujo/secuencia como HTML explorable. archify-review = solo para mantener el repo archify.")
rows = []
for f in sorted(glob.glob(f"{BASE}/archify/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = fm.get("name", os.path.basename(os.path.dirname(f)))
    rows.append(entry(name, clean(fm.get("description",""), 280), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 30. Agent-Reach [TOOL/APP + skill]
section("Agent-Reach (1) [TOOL/APP — con skill embebida]",
        "CLI que lee/busca Twitter, Reddit, YouTube, GitHub, Bilibili, Xiaohongshu sin claves de API. Solo se trajo el wrapper de skill; requiere el CLI agent-reach instalado para funcionar de verdad.")
rows = []
fm = frontmatter(read(f"{BASE}/Agent-Reach/skill/SKILL.md"))
rows.append(entry(fm.get("name","agent-reach"), clean(fm.get("description",""), 280), f"{BASE}/Agent-Reach/skill"))
total += len(rows); out.append("\n".join(rows) + "\n")

# 31. VoiceStudio [TOOL/APP + skill]
section("VoiceStudio (2) [TOOL/APP — con skill embebida]",
        "App local completa (Electron+backend+frontend) tipo ElevenLabs self-hosted: clonar voz, dubbing, transcripción. Solo se trajo skills/; requiere VoiceStudio instalado y corriendo para que la skill funcione.")
rows = []
for f in sorted(glob.glob(f"{BASE}/VoiceStudio/skills/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = os.path.basename(os.path.dirname(f))
    rows.append(entry(name, clean(fm.get("description",""), 260), os.path.dirname(f)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 32. fabricjs [TOOL/APP + skill, maintainer-only]
section("fabricjs (1) [TOOL/APP — skill de mantenedor únicamente]",
        "El repo de la librería JS de canvas (261MB) no se trajo; solo su skill de mantenedor para abrir PRs contra fabricjs/fabric.js. No es una skill de 'construir con Fabric.js'.")
rows = []
fm = frontmatter(read(f"{BASE}/fabricjs/fabricjs-open-pr/SKILL.md"))
rows.append(entry(fm.get("name","fabricjs-open-pr"), clean(fm.get("description",""), 280), f"{BASE}/fabricjs/fabricjs-open-pr"))
total += len(rows); out.append("\n".join(rows) + "\n")

# 33. 2D character / puppet / animation skills (batch 2026-09-24)
section("Character & 2D animation skills (11)",
        "Batch de animación de personajes/2D: imagen→sprites de juego, Spine, Live2D (varias), SVG, After Effects, PSD por capas. Algunos son Tool+Skill (requieren un CLI/app propio).")
rows = []
char_paths = [
    (f"{BASE}/img2game2d/SKILL.md", 260),
    (f"{BASE}/spine-animation-ai/SKILL.md", 220),
    (f"{BASE}/live2d-from-art/SKILL.md", 240),
    (f"{BASE}/live2d-agent-kit/SKILL.md", 240),
    (f"{BASE}/PuppetLoom/live2d-puppet/SKILL.md", 220),
    (f"{BASE}/svg-character-animator/SKILL.md", 260),
    (f"{BASE}/MotionLoom/motionloom/SKILL.md", 220),
    (f"{BASE}/ae-agent-skills/skills/aftereffects-cli/SKILL.md", 220),
    (f"{BASE}/ae-agent-skills/skills/aftereffects-declarative/SKILL.md", 220),
    (f"{BASE}/gpt-image2-layered-psd/SKILL.md", 240),
    (f"{BASE}/character-animation-skill/SKILL.md", 240),
]
for p, n in char_paths:
    fm = frontmatter(read(p))
    name = fm.get("name", os.path.basename(os.path.dirname(p)))
    rows.append(entry(name, clean(fm.get("description",""), n), os.path.dirname(p)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 34. Video editing / Remotion skills (batch 2026-09-29)
section("Video editing & Remotion skills (6)",
        "Edición de vídeo real (FFmpeg/Whisper) + motion graphics programático con Remotion (React→MP4), reels verticales 9:16, HyperFrames. Ver también claude-code-video-toolkit/ (solo README de referencia, no skill).")
rows = []
vid_paths = [
    (f"{BASE}/ecc-video-editing/video-editing/SKILL.md", 260),
    (f"{BASE}/claude-remotion-skill/remotion-motion-graphics/SKILL.md", 260),
    (f"{BASE}/video-motion-craft/SKILL.md", 260),
    (f"{BASE}/vertical-video-editing-skills/skills/video-editing/SKILL.md", 240),
    (f"{BASE}/video-editor-plugin/skills/video-editor/SKILL.md", 260),
    (f"{BASE}/remotion-ffmpeg-video-skill/skills/remotion-ffmpeg-video/SKILL.md", 240),
]
for p, n in vid_paths:
    fm = frontmatter(read(p))
    name = fm.get("name", os.path.basename(os.path.dirname(p)))
    rows.append(entry(name, clean(fm.get("description",""), n), os.path.dirname(p)))
total += len(rows); out.append("\n".join(rows) + "\n")

# 35. eng-review-skills (authored, not cloned)
section("eng-review-skills (32) [AUTORADAS]",
        "Skills de revisión/auditoría de ingeniería escritas para esta biblioteca (no clonadas): BD, testing, fiabilidad (idempotency/outbox), API, frontend, concurrencia. Fundamentadas en reference-docs/ (OWASP, Google, system-design-primer). Cada una: checklist + red flags + fix.")
rows = []
for f in sorted(glob.glob(f"{BASE}/eng-review-skills/*/*/SKILL.md")):
    fm = frontmatter(read(f))
    name = fm.get("name", os.path.basename(os.path.dirname(f)))
    grp = f.replace("\\", "/").replace(BASE + "/eng-review-skills/", "").split("/")[0]
    rows.append(entry(name, clean(fm.get("description",""), 220), os.path.dirname(f), grp))
total += len(rows); out.append("\n".join(rows) + "\n")

# 36 + 37 + 38 single-skill repos
section("Repos de una sola skill (3)", "")
rows = []
for p in [f"{BASE}/html-ppt-skill/SKILL.md", f"{BASE}/huashu-design/SKILL.md", f"{BASE}/motion-dev-animations-skill/SKILL.md"]:
    fm = frontmatter(read(p))
    rows.append(entry(fm.get("name", os.path.basename(os.path.dirname(p))),
                      clean(fm.get("description",""), 300), os.path.dirname(p)))
total += len(rows); out.append("\n".join(rows) + "\n")

out.insert(3, f"\n**Total: {total} entradas.**\n")

io.open(f"{BASE}/CATALOG.md", "w", encoding="utf-8").write("\n".join(out))
print("wrote", total, "entries")
print("size KB:", os.path.getsize(f"{BASE}/CATALOG.md") // 1024)
