---
name: frontend-code-review
description: Review frontend/UI code (React, Vue, Svelte, vanilla) for correctness, security, performance, accessibility, and maintainability. Use when reviewing a component or frontend PR, assessing UI code quality, hunting frontend bugs, or when the user says "review this component", "review my frontend code", "is this React code good", "check this UI code", or "frontend PR review". Routes specifics to state-management, frontend-performance, error-handling, accessibility, and ux-review. For pure visual craft use taste-skill/impeccable; for UX-flow use designer-skills.
---

# Frontend Code Review

Role: senior frontend engineer reviewing code (not visual design — that's `impeccable`,
`taste-skill`; not UX flows — that's [[ux-review]], designer-skills). Each finding: the
file/line, what breaks, severity, fix.

## Checklist
**Correctness**
- Effects/lifecycles: correct dependency arrays; no stale closures; cleanup on unmount
  (listeners, timers, subscriptions) → leaks otherwise.
- Keys on lists are stable and unique (not array index when the list reorders).
- Async race: a fast-changing query where an older response can overwrite a newer one (see
  [[race-condition]]) — cancel/guard.
- Controlled vs uncontrolled inputs consistent.

**Security (frontend)**
- **XSS**: no `dangerouslySetInnerHTML`/`v-html`/`innerHTML` with unsanitized data. Framework
  auto-escaping intact; sanitize any HTML you must inject (OWASP XSS Prevention,
  `reference-docs/CheatSheetSeries`).
- No secrets/tokens/API keys in frontend code or bundles.
- `target="_blank"` has `rel="noopener"`; URLs from data validated (no `javascript:`).
- AuthZ is enforced on the server — the UI hiding a button is not security (see [[api-security]]).

**State** → [[state-management]]. **Performance** → [[frontend-performance]].
**Errors/empty/loading** → [[error-handling]]. **A11y** → [[accessibility]].

**Maintainability**
- Components focused; no 800-line god-components; logic extracted from markup.
- No prop-drilling where context/composition fits; no duplicated fetch logic.
- Types are honest (no `any` hiding real shapes).

## Red flags
- `dangerouslySetInnerHTML={{__html: userInput}}`.
- `useEffect` with missing deps or no cleanup.
- Index-as-key on a reorderable list.
- Secret in a `NEXT_PUBLIC_`/client-exposed var.

## Output
Findings most-severe first, grouped (correctness/security/perf/a11y/maintainability).
