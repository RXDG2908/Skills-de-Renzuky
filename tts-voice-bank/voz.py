"""voz.py - audio rapido de texto a voz con presets (edge-tts, gratis, sin API key).

Uso:
  python voz.py "Hola, esto es una prueba" -p narrador -o hola.mp3
  python voz.py "texto" -v es-AR-TomasNeural --rate +20% --pitch -5Hz
  python voz.py --file guion.txt -p peruano -o guion.mp3
  python voz.py --list            # presets
  python voz.py --voices es       # voces reales disponibles (filtra por prefijo)
  python voz.py "texto" -p robot  # preset con efecto ffmpeg (robot/ardilla/radio/eco/demonio)

Requiere: pip install edge-tts   (ffmpeg solo para presets con efecto)
"""
import argparse, asyncio, os, shutil, subprocess, sys, tempfile

import edge_tts

# nombre: (voz, rate, pitch, filtro_ffmpeg | None)
PRESETS = {
    "narrador":    ("es-MX-JorgeNeural",     "+0%",  "+0Hz",  None),   # voz tipo videos de YouTube/curiosidades
    "narradora":   ("es-MX-DaliaNeural",     "+0%",  "+0Hz",  None),
    "tiktok":      ("es-MX-DaliaNeural",     "+15%", "+15Hz", None),   # aproximacion a la voz femenina rapida de TikTok
    "espanol":     ("es-ES-AlvaroNeural",    "+0%",  "+0Hz",  None),
    "argentino":   ("es-AR-TomasNeural",     "+0%",  "+0Hz",  None),
    "peruano":     ("es-PE-AlexNeural",      "+0%",  "+0Hz",  None),
    "peruana":     ("es-PE-CamilaNeural",    "+0%",  "+0Hz",  None),
    "colombiana":  ("es-CO-SalomeNeural",    "+0%",  "+0Hz",  None),
    "chileno":     ("es-CL-LorenzoNeural",   "+0%",  "+0Hz",  None),
    "rapido":      ("es-MX-JorgeNeural",     "+35%", "+0Hz",  None),   # resumenes / shorts
    "grave":       ("es-ES-AlvaroNeural",    "-10%", "-20Hz", None),   # trailer / epico
    "loquendo":    ("es-ES-AlvaroNeural",    "+5%",  "-8Hz",  "aresample=11025,aresample=44100,acrusher=bits=10:mode=log:aa=1"),  # sabor sintetico retro (aprox., no es Loquendo real)
    "robot":       ("es-MX-JorgeNeural",     "+0%",  "+0Hz",  "afftfilt=real='hypot(re,im)*sin(0)':imag='hypot(re,im)*cos(0)':win_size=512:overlap=0.75"),
    "ardilla":     ("es-MX-DaliaNeural",     "+10%", "+50Hz", "asetrate=44100*1.35,aresample=44100,atempo=0.9"),
    "demonio":     ("es-ES-AlvaroNeural",    "-15%", "-30Hz", "asetrate=44100*0.75,aresample=44100,atempo=1.2,aecho=0.8:0.8:40:0.4"),
    "radio":       ("es-MX-JorgeNeural",     "+0%",  "+0Hz",  "highpass=f=400,lowpass=f=3200,acompressor"),
    "eco":         ("es-MX-JorgeNeural",     "+0%",  "+0Hz",  "aecho=0.8:0.85:300|600:0.4|0.25"),
    "english":     ("en-US-GuyNeural",       "+0%",  "+0Hz",  None),
    "brasil":      ("pt-BR-AntonioNeural",   "+0%",  "+0Hz",  None),
}


async def synth(text, voice, rate, pitch, out):
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text", nargs="?")
    ap.add_argument("--file", help="leer el texto de un .txt")
    ap.add_argument("-p", "--preset", default="narrador")
    ap.add_argument("-v", "--voice", help="voz edge-tts concreta (sobrescribe el preset)")
    ap.add_argument("--rate"); ap.add_argument("--pitch")
    ap.add_argument("-o", "--out", default="voz.mp3")
    ap.add_argument("--list", action="store_true"); ap.add_argument("--voices", metavar="PREFIJO")
    a = ap.parse_args()

    if a.list:
        for k, (v, r, p, f) in PRESETS.items():
            print(f"{k:12} {v:24} rate={r:5} pitch={p:6} {'[efecto]' if f else ''}")
        return
    if a.voices is not None:
        vs = asyncio.run(edge_tts.list_voices())
        for v in vs:
            if v["ShortName"].lower().startswith(a.voices.lower()):
                print(v["ShortName"], v["Gender"])
        return

    text = open(a.file, encoding="utf-8").read() if a.file else a.text
    if not text:
        ap.error("falta el texto (o --file)")
    if a.preset not in PRESETS:
        ap.error(f"preset desconocido: {a.preset} (usa --list)")
    voice, rate, pitch, fx = PRESETS[a.preset]
    voice, rate, pitch = a.voice or voice, a.rate or rate, a.pitch or pitch

    if not fx:
        asyncio.run(synth(text, voice, rate, pitch, a.out))
    else:
        if not shutil.which("ffmpeg"):
            sys.exit("este preset necesita ffmpeg en el PATH")
        tmp = os.path.join(tempfile.mkdtemp(), "raw.mp3")
        asyncio.run(synth(text, voice, rate, pitch, tmp))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-af", fx, a.out], check=True)
    print(f"OK -> {a.out}  ({voice}, {rate}, {pitch}{', fx' if fx else ''})")


if __name__ == "__main__":
    main()
