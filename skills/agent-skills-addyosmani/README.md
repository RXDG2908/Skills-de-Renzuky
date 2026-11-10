# agent-skills — Skill

From <https://github.com/addyosmani/agent-skills> (MIT, Addy Osmani/Google Chrome).
**Type: Skill collection.** 25 production-engineering skills covering the whole
software-delivery lifecycle, not design/content — this is the strongest general
**coding-methodology** pack in the library.

- **api-and-interface-design** — stable API/module-boundary design
- **browser-testing-with-devtools** — real-browser testing via Chrome DevTools MCP
- **ci-cd-and-automation** — pipeline setup, quality gates, deploy strategy
- **code-review-and-quality** — multi-axis review before merge
- **code-simplification** — refactor for clarity without behavior change
- **constraint-driven-development** — writes CONSTRAINTS.md, watches diffs for a weakened quality bar
- **context-engineering** — session/rules-file setup for agent context
- **debugging-and-error-recovery** — systematic root-cause debugging
- **deprecation-and-migration** — sunset/migrate APIs, schemas, features
- **documentation-and-adrs** — architecture decision records
- **doubt-driven-development** — adversarial fresh-context review of every non-trivial decision
- **frontend-ui-engineering** — production-quality, accessible, responsive UI
- **git-workflow-and-versioning** — commits, branching, PRs, releases, semver
- **idea-refine** — divergent/convergent thinking to sharpen a vague idea
- **incremental-implementation** — thin, verifiable slices
- **interview-me** — one-question-at-a-time interview to extract true intent
- **observability-and-instrumentation** — logging/metrics/tracing/alerting
- **performance-optimization** — frontend/backend/query/DB perf
- **planning-and-task-breakdown** — spec → ordered implementable tasks
- **security-and-hardening** — OWASP Top Ten, dependency audit, privacy compliance
- **shipping-and-launch** — pre-launch checklist, staged rollout, rollback
- **source-driven-development** — grounds decisions in official docs
- **spec-driven-development** — writes specs/PRDs before coding
- **test-driven-development** — red-green-refactor
- **using-agent-skills** — meta-skill: how to discover/invoke the other 24

Kept `skills/` + `references/`. Dropped the Claude Code plugin scaffolding
(`.claude-plugin/`, `.codex-plugin/`, `agents/`, `commands/`, `hooks/`, `evals/`,
per-tool dot-dirs).
