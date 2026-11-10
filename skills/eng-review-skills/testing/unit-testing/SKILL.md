---
name: unit-testing
description: Write or review fast, isolated unit tests for pure logic and single units of behavior. Use when adding unit tests, reviewing test quality, deciding edge cases to cover, fixing brittle or useless tests, or when the user says "write unit tests", "review these tests", "what edge cases", "these tests are brittle", or "add coverage for this function". Covers Arrange-Act-Assert, boundary/edge cases, test doubles done right, and avoiding tests that lock implementation detail.
---

# Unit Testing

Role: write tests that fail for the right reason and only the right reason. A unit test
pins **behavior** of one unit with its collaborators faked at the boundary.

## What a good unit test is
- **Fast & isolated**: no real DB/network/filesystem/clock — inject or fake those.
- **AAA**: Arrange, Act, Assert — one logical behavior per test.
- **Deterministic**: no sleeps, no random without a seed, no shared mutable state, no order
  dependence.
- **Named by behavior**: `returns_zero_when_cart_empty`, not `test1`.

## Edge cases to always consider
- Empty / null / zero / negative / max / min inputs.
- Boundary values (off-by-one around limits).
- Error/exception paths, not just the happy path.
- Idempotency / repeated calls where relevant.

## Review red flags
- **Asserting mocks were called** instead of asserting the real outcome (tests the wiring,
  not the behavior).
- **Testing private implementation** → breaks on every refactor though behavior is fine.
- **"Proving A with A"** — the test restates the code. See [[test-coverage]].
- **Over-mocking** — so much is faked the test can't fail meaningfully.
- **No assertion** / asserting only "didn't throw".
- **Logic in the test** (loops/conditionals computing the expected value the same way the
  code does).

## Doubles
Stub for inputs, mock/spy only when the *interaction* is the behavior under test (e.g.
"an email is sent"). Prefer real objects for cheap collaborators.

Related: [[testing-strategy]], [[integration-testing]]. For deciding whether a test earns
its keep: [[test-coverage]].
