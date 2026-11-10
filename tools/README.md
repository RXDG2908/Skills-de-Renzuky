# tools/ — herramientas que usan las skills (solo enlaces)

Este repo **no** guarda las herramientas en sí: solo la "cascarita" — dónde conseguirlas y
cómo instalarlas. Así el repo pesa poco al clonarlo, y cada persona baja en su propia PC
solo lo que va a usar, directo desde el repo oficial de cada herramienta.

- **[`tools.json`](tools.json)**: el manifiesto. Por cada herramienta: nombre, categoría,
  cómo se instala (`git` / `pip` / `winget` / `npx` / `manual`), URL oficial, licencia y
  qué skills la usan.
- **`install.ps1`** (Windows) / **`install.sh`** (Linux/macOS): leen el manifiesto e
  instalan lo que pidas. Lo que se clona va a `tools/_downloads/<nombre>/`, que está en
  `.gitignore` y nunca se sube.

```powershell
.\tools\install.ps1                       # ver la lista
.\tools\install.ps1 ffmpeg yt-dlp         # instalar por nombre
.\tools\install.ps1 -Category lipsync     # instalar una categoría
```

## Categorías

| Categoría | Qué hay |
|---|---|
| `base` | ffmpeg, yt-dlp, node, python, whisper, whisper.cpp, markitdown |
| `voz` | edge-tts, kokoro, piper, espeak-ng (los usa `tts-voice-bank`) |
| `video` | Remotion, HyperFrames, OpenMontage, servidor MCP de ffmpeg-skill |
| `lipsync` | LatentSync, MuseTalk, Wav2Lip: sincronizan la boca del video con un audio nuevo |
| `separacion` | UVR, Demucs: separan la voz de la música |
| `edicion-habla` | ViiTorVoice-NAR, AuK, Fish Speech: cambian palabras sueltas de una grabación sin cambiar la voz |
| `canto` | SoulX-Singer, YingMusic-Singer, ACE-Step, Seed-VC, Applio/RVC: cambian la letra de una canción o convierten una voz cantada |
| `3d-fab` | Blender, OpenSCAD, CadQuery, Boxes.py, Export Paper Model, PackBox, Packaging Dieline Generator |
| `texturas` | Materialize |
| `tool+skill` | Las apps que necesitan las skills marcadas **Tool+Skill** en el README principal (Agent-Reach, VoiceStudio, PuppetLoom, MotionLoom, archify, rondoflow, Scenario MCP, ae-cli) |

## Antiguas carpetas "Tool"

<a id="boxes"></a><a id="materialize"></a><a id="packbox"></a><a id="packaging-dieline-generator"></a><a id="export-paper-model-from-blender"></a>
`boxes`, `Materialize`, `packbox`, `packaging-dieline-generator` y
`Export-Paper-Model-from-Blender` antes iban copiadas enteras en el repo. Ahora son entradas
de `tools.json`. En esta PC las copias que ya había se movieron a `tools/_downloads/`, así
que nada se perdió.

## Agregar una herramienta

Añade un objeto a `tools.json` (`name`, `category`, `kind`, `url`, `license`, y también `id`
si es pip/winget/npx). Nunca subas el binario ni sus modelos: el `.gitignore` de la raíz
bloquea imágenes, video, audio, fuentes, modelos de IA (`*.safetensors`, `*.pt`…), archivos
comprimidos y ejecutables.
