---
name: response-validation
description: Review or design API responses so they conform to the declared schema, expose no sensitive or excessive data, and use a consistent error shape. Use when checking what an API returns, preventing data over-exposure, enforcing an output contract, standardizing error responses, or when the user says "validate the response", "we're leaking fields", "consistent error format", "contract testing the output", or "excessive data exposure". Covers output schema conformance, field whitelisting, error envelopes, and contract tests.
---

# Response Validation

Role: make sure what goes OUT is exactly what the contract promises — no more (data leaks),
no less (broken clients), consistently shaped.

## Checklist
- **Field whitelist / explicit serialization**: build responses from an explicit DTO/
  serializer, never `return user` (dumps `password_hash`, `is_admin`, internal flags).
  This is OWASP "excessive data exposure" — see [[api-security]].
- **Schema conformance**: the response matches the declared OpenAPI/schema (types, required
  fields, enums). Catch drift with **contract tests** / response-schema assertions in
  integration tests (see [[integration-testing]]).
- **Consistent error envelope**: one shape across the whole API — stable machine `code`,
  human `message`, field-level details for validation, correct status code. Not a different
  shape per endpoint, not `200` with an error inside (see [[rest-api]]).
- **No internal leakage in errors**: no stack traces, SQL, file paths, framework internals,
  or secrets in prod error bodies — map to safe messages + a correlation id.
- **Nulls vs omission** are consistent and documented; numbers/dates/money formatted
  consistently (exact types — see [[database-audit]]).
- **Pagination metadata** consistent across list endpoints.

## Red flags
- `res.json(dbRow)` / `return entity` with no serializer.
- Different error JSON shapes across endpoints; HTTP 200 wrapping an error.
- Stack trace / SQL error returned to the client.
- Response includes fields not in the documented schema (silent contract drift).

Related: [[request-validation]], [[api-design]], [[api-security]], [[integration-testing]].
