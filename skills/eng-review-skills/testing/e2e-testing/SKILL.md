---
name: e2e-testing
description: Write or review end-to-end tests that drive the whole system the way a user does (browser/API through to the database). Use when adding E2E coverage for critical user journeys, reviewing flaky browser tests, deciding what belongs in E2E vs lower levels, or when the user says "write e2e tests", "Playwright/Cypress tests", "these e2e tests are flaky", "test the full checkout flow", or "what should be an e2e test". Covers journey selection, stable selectors, waiting correctly (no sleeps), and flakiness control.
---

# E2E Testing

Role: protect the handful of journeys whose breakage is a business incident. E2E is the
most expensive, slowest, flakiest level — spend it only where it pays.

## Pick the right tests
- Critical, revenue/safety journeys: sign-up, login, checkout/payment, the core "job to be
  done". One happy path + the most important failure (e.g. declined card).
- Do NOT re-test every field validation or branch here — push those down to unit/integration
  (see [[testing-strategy]]).

## Write them to not be flaky
- **Selectors**: role/label/test-id (`data-testid`), never brittle CSS/XPath tied to layout.
- **Waiting**: wait for a condition/element/network response — **never** `sleep(n)`. Fixed
  sleeps are the #1 cause of flaky E2E.
- **Isolation**: each test creates its own account/data; no dependence on a shared seeded
  user that other tests mutate.
- **Idempotent setup/teardown**: re-runnable; clean up created data.
- **One assertion focus** per test; a journey test asserts the outcome, not every pixel.
- **Deterministic environment**: freeze time/clock where it affects assertions; stub only
  truly external third parties (payment sandbox is fine).

## Red flags
- `await page.waitForTimeout(3000)` sprinkled around → flaky.
- Tests that must run in a specific order.
- Dozens of E2E tests covering logic that unit tests should own (slow suite, inverted
  pyramid).
- Screenshots/visual diffs with no tolerance → fail on font rendering.

Grounding: `awesome-claude-skills/webapp-testing` and `agent-skills-addyosmani/
browser-testing-with-devtools` are practical Playwright toolkits. Related: [[testing-strategy]].
