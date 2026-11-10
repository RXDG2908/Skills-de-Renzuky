---
name: error-handling-code
description: Review or design error handling in code — catching, propagating, logging, and recovering from failures without swallowing them or leaking internals. Use when reviewing how code handles failures, hardening error paths, fixing swallowed exceptions or unhandled rejections, designing retry/fallback behavior, or when the user says "review error handling", "we're swallowing errors", "handle this failure", "retry logic", or "graceful degradation in code". Covers fail-fast vs recover, retries/backoff, error boundaries, and safe logging. Complements error-handling-ux (designer-skills) which covers user-facing messaging.
---

# Error Handling (code level)

Role: make failures visible, safe, and recoverable. The user-facing side (messages, empty/
error states, copy) is `designer-skills/error-handling-ux` and [[ux-review]]; this is the
**code** pass.

## Principles
- **Don't swallow**: an empty `catch {}` or `catch (e) { log(e) }` that then continues as if
  nothing happened hides bugs. Either handle meaningfully or propagate.
- **Fail fast on programmer errors** (bugs, invalid state) — crash/throw loudly in dev,
  surface to monitoring in prod. **Recover from operational errors** (network, timeout,
  rate limit) with retry/fallback.
- **Catch at the right level**: handle where you can actually do something; otherwise let it
  bubble to a boundary that logs + responds.
- **Preserve context**: wrap-and-rethrow with cause; never lose the stack by throwing a new
  bare string.

## Checklist
- No empty/log-and-continue catches on paths that must not silently fail.
- **Async**: every promise handled; no unhandled rejections; `Promise.all` failure handled;
  async errors in event handlers caught.
- **Retries**: only for idempotent/transient ops (see [[idempotency]]); bounded attempts;
  **exponential backoff + jitter**; a circuit breaker for a failing dependency — no
  unbounded retry storms (see [[stress-testing]]).
- **Timeouts** on every network/IO call — no infinite hang.
- **Error boundaries** (React) / global handlers so one component error doesn't white-screen
  the app; a fallback UI.
- **Logging**: log with context + correlation id; **never log secrets/PII/tokens**; don't
  leak stack traces/internals to the user (map to safe messages — see [[response-validation]]).
- **Cleanup on error**: resources released, transactions rolled back (see [[transaction-integrity]]).

## Red flags
- `catch (e) {}` / `catch (e) { console.log(e) }` then continue.
- `fetch` with no timeout and no `.catch`.
- Unbounded/no-backoff retry loop.
- Stack trace shown to the user; secret written to logs.
- No React error boundary → one throw blanks the page.

Related: [[frontend-code-review]], [[ux-review]], [[idempotency]].
