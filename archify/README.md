# archify — Tool/App with a bundled skill

From <https://github.com/tt-a1i/archify> (MIT; `archify` skill itself based on
Cocoon-AI/architecture-diagram-generator MIT v1.0). **Type: Tool/App.** The upstream
repo is a full product (~313MB: a website, a standalone diagram viewer webapp, a
benchmark suite, `generated/` example outputs, a packaged `archify.zip`) — only its two
skill folders were pulled.

- **`archify/`** — the main skill. Creates polished, validated architecture, workflow,
  sequence, data-flow, and lifecycle/state diagrams as explorable standalone HTML with
  inline SVG, dark/light themes, optional trace motion, and PNG/JPEG/WebP/SVG/WebM
  export. Accepts plain-language requirements or pasted Mermaid input; can inspect
  repository evidence so the diagram reflects real code. Ships its own `scripts/`,
  `renderers/`, `schemas/`, `recipes/`, `references/`, `assets/`, `bin/`.
- **`archify-review/`** — maintainer-only skill for triaging archify's own issues/PRs by
  value/cost/impact. Not useful outside contributing to the archify repo.

Dropped: `website/`, `viewer/`, `benchmarks/`, `experiments/`, `generated/`,
`integrations/`, `archify.zip`, `docs/`.
