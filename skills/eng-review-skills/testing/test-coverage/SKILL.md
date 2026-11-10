---
name: test-coverage
description: Assess test coverage meaningfully — find untested critical paths and cut worthless tests — rather than chasing a coverage percentage. Use when reviewing how well-tested code is, deciding if coverage is adequate, triaging which tests to keep vs delete, judging whether a test is worth maintaining, or when the user says "check test coverage", "is this well tested", "are these tests worth keeping", "we're proving A with A", or "what's untested that matters". Covers coverage as a gap-finder not a target, branch vs line coverage, and the "test proves nothing" anti-patterns.
---

# Test Coverage

Role: judge whether tests actually protect the code. Coverage % is a **gap-finder, not a
goal** — 100% line coverage with assertion-free tests protects nothing; 60% covering every
critical path can be fine.

## Use coverage correctly
- Read **uncovered** lines/branches to find real gaps, especially in critical/irreversible
  paths. Don't chase the number.
- Prefer **branch** coverage over line coverage — an `if` with no else-case test shows as
  "covered" by line but a branch is untested.
- A hard coverage gate can backfire: people write junk tests to pass it. If you gate, gate
  on **critical modules**, not a global %.

## Is a test worth keeping? Delete/rewrite if it…
- **Proves A with A** — restates the implementation; passes because code and test share the
  same (possibly wrong) logic.
- **Asserts nothing** / only "didn't throw" / only "mock was called".
- **Locks implementation detail** — breaks on every refactor though behavior is unchanged.
- **Is a duplicate** — same behavior as another test, no new input/branch.
- **Is permanently skipped/quarantined** with no owner or ticket.
- **Can't fail** — no realistic input makes it red.

## Is a critical path under-covered? Flag if…
- A money/auth/data-deletion branch has no test.
- Error/exception paths are untested (only happy path).
- Boundary conditions untested (empty, max, negative, concurrent).

## Output
Two lists: (1) real gaps worth filling, ranked by risk; (2) tests to delete or rewrite,
with why. Related: [[testing-strategy]], [[unit-testing]].
