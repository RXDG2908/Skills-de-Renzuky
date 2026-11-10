---
name: api-design
description: Design or review an API's shape — resources, naming, consistency, errors, and evolvability — independent of transport. Use when designing a new API, reviewing an API for usability and consistency, deciding resource/endpoint structure, shaping request/response contracts, or when the user says "design this API", "review our API", "is this API well designed", "what should the endpoints be", or "make this API consistent". Routes to rest-api, api-versioning, api-security, rate-limiting, request-validation, response-validation for specifics.
---

# API Design

Role: API designer optimizing for the consumer. A good API is predictable, consistent,
hard to misuse, and safe to evolve.

## Principles
- **Consistency over cleverness**: same naming, casing, pagination, error shape everywhere.
  One inconsistent corner costs every integrator.
- **Model resources and clear actions**, not RPC-ish verbs scattered around (for REST see
  [[rest-api]]).
- **Least surprise**: predictable names, sensible defaults, no hidden side effects on GET.
- **Hard to misuse**: required fields enforced; dangerous operations explicit; no
  ambiguous nullable-vs-absent.

## Checklist
- **Naming**: consistent casing (pick snake or camel, stick to it), plural resource nouns,
  no leaking internal/DB names.
- **Errors**: a single consistent error envelope — stable machine-readable `code`, human
  `message`, and field-level detail for validation; correct status codes. See
  [[response-validation]].
- **Pagination/filtering/sorting**: one consistent scheme across all list endpoints
  (cursor-based for scale; see [[sql-performance]]).
- **Idempotency**: unsafe retryable operations accept an idempotency key (see [[idempotency]]).
- **Evolvability**: additive changes don't break clients; breaking changes are versioned
  (see [[api-versioning]]).
- **Validation**: inputs validated and rejected clearly (see [[request-validation]]);
  outputs conform to the declared schema (see [[response-validation]]).
- **Security**: authn/authz on every endpoint; no sensitive data over-returned (see
  [[api-security]]); abuse-limited (see [[rate-limiting]]).
- **Documented contract**: OpenAPI/schema is the source of truth and matches reality.

## Red flags
- Different error shapes per endpoint; 200 OK with an error in the body.
- `GET` that mutates; booleans named ambiguously; "misc"/overloaded endpoints.
- Breaking a field's meaning in place instead of versioning.

## Output
Findings on consistency, misuse-resistance, and evolvability, each with the concrete fix.
