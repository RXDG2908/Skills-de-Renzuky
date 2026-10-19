---
name: testing-strategy
description: Design or review a project's overall test strategy — what to test at which level, the test pyramid, and where coverage is missing or wasted. Use when setting up testing for a project, reviewing whether a test suite is sound, deciding what kind of test a change needs, or when the user says "what should we test", "design a test strategy", "is our test suite good", "too many/too few tests", or "where are the gaps". Routes specifics to unit-testing, integration-testing, e2e-testing, load-testing, chaos-testing, and test-coverage.
---

# Testing Strategy

Role: test architect. Tests exist to catch real regressions cheaply and give confidence
to change code — not to hit a coverage number. Match test type to risk.

## The shape (test pyramid, adapted)
- **Many fast unit tests** — pure logic, branches, edge cases. See [[unit-testing]].
- **Fewer integration tests** — real collaborators (DB, queue, adjacent module). See [[integration-testing]].
- **Few e2e tests** — critical user journeys only. See [[e2e-testing]].
- **Targeted non-functional** — load/stress for scaling-critical paths ([[load-testing]],
  [[stress-testing]]); chaos for resilience-critical systems ([[chaos-testing]]).

Inverted pyramid (mostly slow e2e) = slow, flaky, expensive. Flag it.

## Review checklist
- Every critical/irreversible path (payments, auth, data deletion) has tests at the right
  level.
- Tests assert behavior/outcomes, not implementation details (see [[test-coverage]] for
  the "proving A with A" trap).
- Bug fixes ship with a regression test that fails before the fix.
- No whole category missing (e.g. zero integration tests for a service that's all I/O).
- Flaky tests are quarantined/fixed, not ignored — they erode trust in the whole suite.
- CI runs the suite; failing tests block merge.

## Decision guide
- Pure function / branching logic → unit.
- "Does my code talk to the DB/API correctly" → integration.
- "Can a user complete checkout" → e2e (one happy path + key failure).
- "Does it hold at 10k rps" → load. "What breaks past the limit" → stress. "Does it
  survive a node dying" → chaos.

Grounding: `reference-docs/eng-practices` (what to look for in a code review).

## Output
A gap map: risk area → current coverage → what's missing → which level to add.
