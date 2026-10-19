# eng-review-skills

**32 engineering review/audit skills — authored for this library** (not cloned). They
turn the topics you listed into actionable review skills: given code or a design, each
checks it against a concrete checklist, flags findings with severity, and gives the
smallest effective fix. Grounded in the authoritative sources under
[`../reference-docs/`](../reference-docs/) (OWASP, Google eng-practices, system-design-primer,
Redis docs). Cross-linked with `[[name]]` references.

## Groups

**database/ (5)** — database-audit · sql-performance · database-modeling · transaction-integrity · migration-review
**testing/ (8)** — testing-strategy · unit-testing · integration-testing · e2e-testing · load-testing · stress-testing · chaos-testing · test-coverage
**reliability/ (3)** — idempotency · duplicate-prevention · transaction-safety
**api/ (7)** — api-design · rest-api · api-security · api-versioning · rate-limiting · request-validation · response-validation
**frontend/ (6)** — frontend-code-review · ux-review · accessibility (code-level) · state-management · frontend-performance · error-handling (code-level)
**concurrency/ (3)** — race-condition · distributed-locking · concurrency-control

## Name notes (deliberate, to avoid collisions)

Two names you listed already existed in the library as **design/UX** skills; these are the
**code-level** complements, so their frontmatter `name:` is suffixed to coexist:
- `frontend/accessibility/` → frontmatter name **`accessibility-code`** (semantic HTML,
  ARIA, keyboard, focus). The design/WCAG-visual `accessibility` lives in `designer-skills`
  / `awesome-design-skills`.
- `frontend/error-handling/` → frontmatter name **`error-handling-code`** (catch/retry/
  boundaries/logging). User-facing `error-handling-ux` lives in `designer-skills`.

## Overlap with existing packs (use together, not instead)

- `agent-skills-addyosmani` covers TDD, security-and-hardening, performance,
  api-and-interface-design at a *methodology* level; these are *checklist/review* skills at
  a finer grain. Complementary.
- `security-audit-skill` (Cloudflare) is the heavy multi-phase audit; `api-security` /
  `database-audit` here are faster focused passes.
- `designer-skills` / `awesome-ux-skills` own UX *method* and *design* a11y; `ux-review` /
  `accessibility-code` here are quick code-side passes that defer to them for depth.

Authored 2026-10-05. License: same as the library (personal use). The reference-docs they
cite keep their own upstream licenses.
