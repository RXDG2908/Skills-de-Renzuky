"""benchmark.py - mide cuanto tarda cada motor/voz TTS en generar audio.

Uso:
  python benchmark.py                    # todo, 3 corridas por caso
  python benchmark.py --runs 5
  python benchmark.py --only edge tiktok # filtra motores (edge, tiktok, sapi, fx)

Mide por caso (motor x voz x texto corto/medio/largo):
  - latencia: segundos de pared hasta tener el archivo (mediana y minimo)
  - audio:    duracion del audio generado (ffprobe)
  - RTF:      latencia / duracion de audio  (< 1 = genera mas rapido que tiempo real)
  - chars/s:  caracteres procesados por segundo

Escribe benchmark/resultados.md y benchmark/resultados.csv.
Requiere: edge-tts, ffmpeg/ffprobe; SAPI usa PowerShell (Windows); TikTok usa el proxy
no oficial de Weilbyte (puede caerse). Los textos se envian a esos servicios: no pongas
nada privado en ellos.
"""
import argparse, asyncio, base64, csv, json, os, platform, re, statistics, subprocess
import sys, tempfile, time, urllib.request
from datetime import datetime

import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from voz import PRESETS  # noqa: E402

TEXTS = {
    "corto": "Hola, esto es una prueba rapida de voz.",
    "medio": ("¿Sabías que los pulpos tienen tres corazones y sangre azul? Dos corazones bombean "
              "sangre a las branquias y el tercero al resto del cuerpo. Cuando nadan, el corazón "
              "principal se detiene, por eso prefieren arrastrarse. Sígueme para más datos curiosos."),
}
TEXTS["largo"] = " ".join([TEXTS["medio"]] * 4)

CASES = [
    ("edge",   "es-MX-JorgeNeural"),
    ("edge",   "es-PE-CamilaNeural"),
    ("edge",   "es-ES-AlvaroNeural"),
    ("tiktok", "es_mx_002"),
    ("tiktok", "en_us_001"),
    ("tiktok", "en_us_ghostface"),
    ("sapi",   "Microsoft Helena Desktop"),
    ("fx",     "loquendo"),
    ("fx",     "robot"),
    ("fx",     "ardilla"),
]

TIKTOK_URL = "https://ottsy.weilbyte.dev/api/generation"


# ---------- motores ----------
def run_edge(voice, text, out, rate="+0%", pitch="+0Hz"):
    asyncio.run(edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(out))


def _chunks(text, n=280):
    parts, cur = [], ""
    for s in re.split(r"(?<=[.!?])\s+", text):
        if len(cur) + len(s) + 1 > n and cur:
            parts.append(cur); cur = s
        else:
            cur = f"{cur} {s}".strip()
    if cur:
        parts.append(cur)
    return parts


def run_tiktok(voice, text, out):
    data = b""
    for chunk in _chunks(text):  # el endpoint acepta ~300 caracteres por peticion
        body = json.dumps({"text": chunk, "voice": voice}).encode()
        req = urllib.request.Request(TIKTOK_URL, body, {"Content-Type": "application/json",
                                                        "User-Agent": "tts-benchmark"})
        r = json.load(urllib.request.urlopen(req, timeout=60))
        if not r.get("success"):
            raise RuntimeError(r.get("error") or "tiktok fallo")
        data += base64.b64decode(r["data"])
    open(out, "wb").write(data)


def run_sapi(voice, text, out):
    wav = out[:-4] + ".wav"
    ps = ("Add-Type -AssemblyName System.Speech;"
          "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
          f"$s.SelectVoice('{voice}');$s.SetOutputToWaveFile('{wav}');"
          "$s.Speak([Console]::In.ReadToEnd());$s.Dispose()")
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], input=text.encode("utf-8"),
                   check=True, capture_output=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, out], check=True)
    os.remove(wav)


def run_fx(preset, text, out):
    voice, rate, pitch, fx = PRESETS[preset]
    raw = out[:-4] + "_raw.mp3"
    run_edge(voice, text, raw, rate, pitch)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", fx, out], check=True)
    os.remove(raw)


ENGINES = {"edge": run_edge, "tiktok": run_tiktok, "sapi": run_sapi, "fx": run_fx}


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


# ---------- main ----------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--only", nargs="*", choices=list(ENGINES))
    ap.add_argument("--outdir", default=os.path.join(HERE, "benchmark"))
    a = ap.parse_args()
    if platform.system() != "Windows" and (not a.only or "sapi" in a.only):
        print("SAPI solo existe en Windows: se omite")
    os.makedirs(a.outdir, exist_ok=True)
    tmp = tempfile.mkdtemp()

    rows = []
    for engine, voice in CASES:
        if a.only and engine not in a.only:
            continue
        if engine == "sapi" and platform.system() != "Windows":
            continue
        for tname, text in TEXTS.items():
            times, dur, err = [], 0.0, ""
            for i in range(a.runs):
                out = os.path.join(tmp, f"{engine}_{i}.mp3")
                t0 = time.perf_counter()
                try:
                    ENGINES[engine](voice, text, out)
                except Exception as e:  # registra el fallo y sigue con el resto
                    err = str(e)[:80]
                    break
                times.append(time.perf_counter() - t0)
                dur = duration(out)
            if times:
                med = statistics.median(times)
                row = dict(motor=engine, voz=voice, texto=tname, chars=len(text), corridas=len(times),
                           lat_mediana=round(med, 2), lat_min=round(min(times), 2),
                           audio_s=round(dur, 2), rtf=round(med / dur, 3) if dur else None,
                           chars_s=round(len(text) / med), error="")
            else:
                row = dict(motor=engine, voz=voice, texto=tname, chars=len(text), corridas=0,
                           lat_mediana=None, lat_min=None, audio_s=None, rtf=None, chars_s=None, error=err)
            rows.append(row)
            print(f"{engine:6} {voice:26} {tname:5}  "
                  + (f"{row['lat_mediana']:6.2f}s  audio {row['audio_s']:6.2f}s  RTF {row['rtf']}"
                     if row["corridas"] else f"FALLO {err}"))

    with open(os.path.join(a.outdir, "resultados.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

    fmt = lambda v, s="": "—" if v is None else f"{v}{s}"
    md = [f"# Benchmark TTS — {datetime.now():%Y-%m-%d %H:%M}", "",
          f"{a.runs} corridas por caso; latencia = mediana (mínimo). RTF < 1 = más rápido que tiempo real. "
          f"Textos: corto {len(TEXTS['corto'])}, medio {len(TEXTS['medio'])}, largo {len(TEXTS['largo'])} caracteres.", "",
          "| Motor | Voz | Texto | Latencia | Audio | RTF | chars/s |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["corridas"]:
            md.append(f"| {r['motor']} | {r['voz']} | {r['texto']} | {r['lat_mediana']}s ({r['lat_min']}s) "
                      f"| {r['audio_s']}s | {fmt(r['rtf'])} | {fmt(r['chars_s'])} |")
        else:
            md.append(f"| {r['motor']} | {r['voz']} | {r['texto']} | FALLO: {r['error']} | — | — | — |")
    open(os.path.join(a.outdir, "resultados.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(f"\n-> {os.path.join(a.outdir, 'resultados.md')}")


if __name__ == "__main__":
    main()
