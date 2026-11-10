---
name: integration-testing
description: Write or review integration tests that exercise a unit together with its real collaborators (database, queue, cache, adjacent service). Use when testing data-access code, module boundaries, API handlers against a real DB, or message consumers, or when the user says "write integration tests", "test against a real database", "test this API endpoint end to end in the service", or "mock vs real DB". Covers real-dependency setup, test isolation/cleanup, contract boundaries, and when not to mock.
---

# Integration Testing

Role: verify the seams. Integration tests catch what unit tests can't — wrong SQL, wrong
serialization, broken migrations, mismatched contracts — by using the **real** dependency.

## Principles
- Use a real database/queue/cache (containerized, e.g. Testcontainers, or an ephemeral
  instance), not a mock. A mocked DB that returns what you told it proves nothing about
  your SQL.
- Each test sets up and tears down its own data; no cross-test leakage, no reliance on
  seed state or run order.
- Test the boundary contract: given input X, the row written / message emitted / response
  returned is exactly Y.
- Wrap in a transaction rolled back per test, or truncate between tests — pick one and be
  consistent.

## What to cover here (not in unit)
- Queries/ORM mappings actually return the right rows (incl. joins, null handling).
- Migrations apply cleanly and the code works against the migrated schema.
- API handler → service → DB round trip, including validation and error responses.
- Message produced is consumed and processed correctly (and idempotently — see [[idempotency]]).
- Transaction behavior under the real engine (see [[transaction-integrity]]).

## Red flags
- "Integration" test that mocks the database — it's a unit test in disguise, with no value.
- Shared test DB state causing order-dependent flakiness.
- No cleanup → tests pass alone, fail together.
- External third-party API hit live in CI (flaky, rate-limited) — use a contract test or a
  recorded/faked boundary instead.

Related: [[testing-strategy]], [[unit-testing]], [[e2e-testing]].
