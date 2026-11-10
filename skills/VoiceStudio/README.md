# VoiceStudio — Tool/App with a bundled skill

From <https://github.com/debpalash/VoiceStudio> (MIT + LICENSE-NOTICE.md for bundled
components). **Type: Tool/App.** The upstream repo is a full local voice application —
Electron desktop app + Python backend + web frontend + native bindings — a self-hosted
ElevenLabs alternative (voice cloning, voice design, dubbing, dictation, transcription,
646-language audiobook creation). Only `skills/` was pulled, not the app itself
(`backend/`, `frontend/`, `electron/`, `native/`, `omnivoice/`, `infra/`, `deploy/`).

- **`voicestudio`** — connects to the user's own *running* VoiceStudio backend via its
  REST API or MCP server: generate speech, transcribe, automate dubbing/narration. Does
  nothing on its own — requires VoiceStudio actually installed and running locally.
- **`voicestudio-maintainer`** — repo-specific, only for contributing to VoiceStudio itself.
