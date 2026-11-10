# tts-voice-bank — banco de voces TTS rápidas (Tool + referencia)

Voces "fáciles" para proyectos: la voz de TikTok, Loquendo, las voces de los videos de
curiosidades de YouTube, la voz robot de memes, etc. Todo **texto → audio** en segundos,
sin clonar voces ni modelos pesados (fuera de QwenTTS / ElevenLabs-likes).

Investigado el 2026-11-10. Las herramientas no oficiales (TikTok, Edge) dependen de
endpoints que pueden cambiar sin aviso.

---

## 1. Lo más rápido: `voz.py` (incluido, probado)

Usa **edge-tts** (las voces neurales de Microsoft Edge — gratis, sin API key, 322 voces).
Probado aquí con edge-tts 7.3.1 (la 7.2.8 daba error 403: si falla, `pip install -U edge-tts`).

```bash
pip install -U edge-tts
```

```bash
python voz.py "Sabías que los pulpos tienen tres corazones" -p narrador -o dato.mp3
```

```bash
python voz.py --file guion.txt -p peruano -o guion.mp3
```

```bash
python voz.py --list
```

```bash
python voz.py --voices es-
```

| Preset | Voz base | Para qué |
|---|---|---|
| `narrador` / `narradora` | es-MX Jorge / Dalia | La voz típica de videos de curiosidades / "top 10" de YouTube |
| `tiktok` | es-MX Dalia, +15% velocidad, tono más alto | Aproximación a la voz femenina rápida de TikTok |
| `rapido` | es-MX Jorge +35% | Shorts, resúmenes |
| `grave` | es-ES Álvaro, lento y grave | Trailers, épico |
| `espanol`, `argentino`, `peruano`, `peruana`, `colombiana`, `chileno`, `brasil`, `english` | Acentos regionales | Variedad de personajes |
| `loquendo` | Álvaro + bitcrush 11 kHz | **Sabor** sintético retro (no es Loquendo real; ver §3) |
| `robot` | Jorge + vocoder FFT | Voz robot / IA de meme |
| `ardilla` | Dalia pitch +35% | Chipmunk |
| `demonio` | Álvaro pitch -25% + eco | Terror / villano |
| `radio` | Jorge, banda 400–3200 Hz | Walkie-talkie / llamada telefónica |
| `eco` | Jorge + eco | Cueva / sala grande |

Los presets con efecto necesitan `ffmpeg` en el PATH. Cualquier voz se ajusta con
`-v es-AR-ElenaNeural --rate +20% --pitch -10Hz`.

**Voces en español disponibles en edge-tts** (lista real, 2026-11-10): AR Elena/Tomas ·
BO Sofia/Marcelo · CL Catalina/Lorenzo · CO Salome/Gonzalo · CR Maria/Juan · CU Belkys/Manuel ·
DO Ramona/Emilio · EC Andrea/Luis · ES Elvira/Ximena/Alvaro · GQ Teresa/Javier ·
GT Marta/Andres · HN Karla/Carlos · MX Dalia/Jorge · NI Yolanda/Federico · PA Margarita/Roberto ·
PE Camila/Alex · PR Karina/Victor · PY Tania/Mario · SV Lorena/Rodrigo · US Paloma/Alonso ·
UY Valentina/Mateo · VE Paola/Sebastian. Portugués BR: Francisca, Antonio, Thalita (multilingüe).

---

## 2. Voz de TikTok (la original)

TikTok no tiene API pública de TTS; estas herramientas usan su endpoint interno
(**no oficial**, se rompe a menudo y puede ir contra sus términos).

| Herramienta | Tipo | Link |
|---|---|---|
| Weilbyte/tiktok-tts | Web en el navegador (la base de casi todas) | <https://github.com/Weilbyte/tiktok-tts> |
| oscie57/tiktok-voice | Script Python → .mp3 | <https://github.com/oscie57/tiktok-voice> |
| tiktok-tts (npm) | Librería Node.js | <https://www.npmjs.com/package/tiktok-tts> |
| Ordyns/TextToSpeech-TikTokAPI | GUI, carga .txt | <https://github.com/Ordyns/TextToSpeech-TikTokAPI> |

Códigos de voz útiles (wiki de oscie57):

- **Español / portugués:** `es_mx_002` (MX hombre), `es_002` (ES hombre), `br_001` / `br_003` / `br_004` (BR mujer), `br_005` (BR hombre)
- **Inglés clásicas:** `en_us_001` (la mujer de TikTok), `en_us_002`, `en_us_006`, `en_us_007`, `en_male_narration` (narrador), `en_male_funny` (wacky), `en_female_emotional`, `en_au_001`, `en_uk_001`
- **Personajes:** `en_us_ghostface`, `en_us_chewbacca`, `en_us_c3po`, `en_us_stitch`, `en_us_stormtrooper`, `en_us_rocket`, `en_male_ghosthost`, `en_male_pirate`, `en_female_madam_leota`
- **Cantadas:** `en_female_f08_salut_damour`, `en_male_m03_lobby`, `en_male_m03_sunshine_soon`, `en_female_f08_warmy_breeze`, `en_male_sing_funny_it_goes_up`, `en_male_m2_xhxs_m03_silly` (chipmunk)

Lista completa: <https://github.com/oscie57/tiktok-voice/wiki/Voice-Codes>.
Ojo: los personajes de Disney/Star Wars son marcas registradas, úsalos solo para memes personales.

> Alternativa sin depender de TikTok: el preset `tiktok` de `voz.py`, o en el propio
> CapCut / TikTok (Texto → Texto a voz) si editas ahí.

---

## 3. Loquendo (Jorge, Carlos, Diego, Juan, Carmen…)

Loquendo era un motor comercial italiano, comprado por Nuance; ya no se vende y no hay
API. Opciones:

| Opción | Notas |
|---|---|
| **La Voz de Zueira / Zueira's Voice** (Android) | App de texto a voz con la voz de Loquendo y otras. Buscar "Zueira's Voice" en Play Store; también la reseñan [Malavida](https://www.malavida.com/es/soft/la-voz-de-zueira/android/) y [APKMirror](https://apkmirror.com/apk/bruno-piovan/zueiras-voice-text-to-speech). "A Voz da Zueira" es otra app, solo en portugués: comprueba el desarrollador antes de instalar. |
| Sitios demo "Loquendo online" (TTSDemo, loquendo.online…) | Reproducen las voces clásicas; sin verificar, pueden tener anuncios o desaparecer. Pruébalos antes de confiar en ellos. |
| Voces "Jorge/Diego" en [Fish Audio](https://fish.audio) | Son modelos de IA de la comunidad que imitan el estilo, no Loquendo. Plan gratis limitado. |
| Instalar voces SAPI5 de Loquendo en Windows | Circulan sueltas por internet, pero sin licencia y desde fuentes no confiables: **no recomendado**. |
| `voz.py -p loquendo` | Imitación aproximada con edge-tts + bitcrush. Legal y local. |

---

## 4. Webs gratis "pegar texto → MP3"

| Web | Destaca | Límite del plan gratis (aprox.) |
|---|---|---|
| [TTSMaker](https://ttsmaker.com) | Muchas voces, también en español, descarga MP3/WAV | Límite semanal de caracteres, captcha y anuncios |
| [ttsMP3](https://ttsmp3.com/ai/text-to-speech/Spanish) | Voces Amazon Polly (Lupe, Miguel, Conchita…) | ~1000 caracteres |
| [TTSFree](https://www.ttsfree.com) | 140+ idiomas; dice permitir uso comercial | Por conversión |
| [Narakeet](https://www.narakeet.com/create/tts-maker.html) | 900 voces, pensado para YouTube | 20 archivos sin registrarse |
| [Fliki](https://fliki.ai/voices/spanish) | 116 voces en español | Plan gratis con marca de agua |
| [FakeYou](https://fakeyou.com) | Voces de famosos y personajes de la comunidad | La mayoría de voces son de pago |
| [SAM online (sam-js)](https://simulationcorner.net/index.php?page=sam) | Voz robot del Commodore 64 (1982), la de los memes retro | Gratis, en el navegador |

Precios y límites cambian; esto es lo que decían las reseñas en 2025–26.

---

## 5. Offline / sin internet (gratis, uso comercial)

| Motor | Calidad | Español | Instalar |
|---|---|---|---|
| **Piper** (rhasspy/OHF) | Buena, muy rápido en CPU, MIT | es_ES / es_MX ("sharvard", "davefx", "ald"…) | `pip install piper-tts` · voces en `huggingface.co/rhasspy/piper-voices` |
| **Kokoro-82M** | Muy natural, Apache-2.0, ligero | `ef_dora`, `em_alex`, `em_santa` | `pip install kokoro soundfile` |
| **eSpeak-NG** | Robótico (sirve como voz robot) | Sí | `winget install eSpeak-NG.eSpeak-NG` |
| **SAM** (s-macke/SAM) | Robot retro de los 80 | No (fonético) | <https://github.com/s-macke/SAM> |
| **Windows SAPI** (Sabina, Helena, Pablo) | Básica, ya instalada en Windows | Sí | `System.Speech` en PowerShell o [Balabolka](http://www.cross-plus-a.com/balabolka.htm) |

Microsoft Sam (la voz meme de Windows XP) **no** es el SAM del Commodore, aunque muchas
webs las mezclan.

---

## Licencias / uso en proyectos

- **edge-tts:** endpoint no oficial de Microsoft. Bien para prototipos y contenido propio, pero para un cliente comercial grande conviene Azure TTS oficial (mismas voces, tier gratis de 500k caracteres al mes).
- **TikTok TTS:** no oficial; mejor no usarlo en encargos para clientes.
- **Piper / Kokoro:** licencias abiertas (MIT / Apache), lo más seguro para uso comercial. Revisa la licencia de cada modelo de voz.
- **Voces de famosos/personajes:** riesgo legal y de derechos de imagen si se publican como reales o para monetizar.
