---
name: lyric-swap-lipsync
description: Change what a character says or sings in an existing clip, keeping the same voice, rhythm and mouth movement - the TikTok "the character now says/sings X" edit. Use when the user wants to replace words in a movie/series/anime scene, rewrite a song's lyrics in the original singer's voice without losing the beat, or re-dub a clip and re-sync the lips. Covers vocal separation, word-level speech editing, singing lyric editing, voice conversion and video lip-sync with open-source tools (LatentSync, MuseTalk, ViiTorVoice-NAR, SoulX-Singer, ACE-Step, Seed-VC, RVC/Applio, UVR/Demucs).
---

# Lyric swap + lip-sync

Goal: a clip where the character says or sings **new words** that sound like the same
voice, land on the same rhythm, and match the mouth. Everything runs locally. The tools
are listed in `tools/tools.json` and installed with `tools/install.ps1` (most need an
NVIDIA GPU).

## 0. Before you start

- **Consent and labeling.** Only do this with material you have the rights to, or as
  clearly labeled parody/fan edits. Never use it to make a real person appear to say
  something deceptive. TikTok requires the AI-generated label on realistic synthetic
  audio/video, so tell the user to turn it on.
- Get the clip: `yt-dlp` (skill `ykdojo-yt-dlp`), then cut the segment with ffmpeg.

## 1. Split the audio

```bash
ffmpeg -i clip.mp4 -vn -ac 2 -ar 44100 audio.wav
demucs --two-stems=vocals audio.wav          # -> vocals.wav + no_vocals.wav
```
UVR (Mel-Band Roformer / MDX models) usually gives cleaner vocals than Demucs on music.
For a movie scene, "no_vocals" is the music and ambience you mix back in later.

## 2. Transcribe with timestamps

`whisper vocals.wav --word_timestamps True --output_format json`. You need the exact
original text plus the start/end time of every word.

## 3. Write the new line (this matters most)

- **Same syllable count** per line, and stressed syllables on the same beats.
- Keep the vowels at the ends of long held notes when you can (open vowels like a/o
  sound most natural).
- Change as few words as possible. The less you regenerate, the more natural it sounds.

## 4. Regenerate the voice: pick a path

| Case | Tool | How |
|---|---|---|
| **Speech, swap a few words** | ViiTorVoice-NAR (best fit), AuK | Give it the audio, the original text and the edited text. Only the changed region is re-synthesized (`word` alignment, mask expand ~1.5). |
| **Speech, whole new line** | Fish Speech / any voice-clone TTS, then a timing fit | Clone from 10-30 s of clean vocals, generate the line, then time-stretch it to the original slot with `ffmpeg -af atempo` or `rubberband`. |
| **Singing, change some lyrics** | SoulX-Singer (singing voice editing) or YingMusic-Singer (melody-preserving lyric edit) | Feed the separated vocal + new lyrics. Fix the alignment in SoulX's MIDI editor for the best result. |
| **Singing, regenerate a section of the full mix** | ACE-Step 1.5 `edit` (only_lyrics) / `repaint` on a time range | Paste the full lyric sheet with only the changed lines swapped. Repaint one section at a time. |
| **Singing, most control** | Sing or TTS-sing a guide vocal with the new lyrics → Seed-VC (zero-shot, f0 on) or Applio/RVC (trained model) | The guide supplies the rhythm and melody; voice conversion supplies the original timbre. Match the key with the semitone shift. |

Tip: render 3-5 takes and keep the best one. Seed-VC needs no training; RVC needs ~10 min of
clean vocals but sounds closer.

## 5. Mix back

Put the new vocal over `no_vocals.wav` at the original timestamps, and match loudness and
reverb (`ffmpeg -filter_complex amix`, `loudnorm`). Splice only the edited span into the
original vocal, with 20-50 ms crossfades, so the untouched words stay 100% original.

## 6. Lip-sync the video

| Tool | When |
|---|---|
| **LatentSync 1.6** | Best quality for existing footage; offline; ~18 GB VRAM at 512px. |
| **MuseTalk 1.5** | Faster, lighter GPU; check the chin/jaw for warping. |
| **Wav2Lip** | Most robust on hard angles/animation, but the mouth comes out soft and the license is non-commercial. |

Only lip-sync the edited span. Cut it out, run lip-sync on that segment with the new full
mix, then concat it back. Animated/cartoon characters often sync worse; try Wav2Lip there.
A cloud alternative is `open-design-skills/skills/fal-lip-sync` (fal.ai).

## 7. Deliver

Export 9:16 for TikTok if needed (skill `vertical-video-editing-skills` or
`video-editor-plugin`), and remind the user about the AI-content label.
