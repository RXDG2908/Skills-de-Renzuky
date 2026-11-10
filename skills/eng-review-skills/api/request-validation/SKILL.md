---
name: request-validation
description: Review or design validation of incoming API/request data — types, ranges, formats, required fields, and rejecting untrusted input safely. Use when validating request bodies/params, hardening an endpoint against bad or malicious input, preventing mass assignment, or when the user says "validate this input", "sanitize the request", "schema validation", "reject bad input", or "mass assignment". Covers schema validation at the boundary, allow-listing, and the injection link. Grounded in OWASP input-validation guidance.
---

# Request Validation

Role: treat every byte from a client as hostile until validated. Validate at the system
boundary, once, with a schema — then trust it inward. Grounding: OWASP Input Validation &
Mass Assignment Cheat Sheets (`reference-docs/CheatSheetSeries`).

## Principles
- **Allow-list, not block-list**: define what's valid (type, range, length, format, enum)
  and reject everything else. Block-lists of "bad" patterns always leak.
- **Schema at the boundary**: validate the whole payload with a schema validator (zod,
  pydantic, JSON Schema, Bean Validation…) before any logic touches it. Reject early with a
  clear, field-level 400/422.
- **Validate, don't sanitize-and-hope**: prefer rejecting malformed input over silently
  "fixing" it.

## Checklist
- Types coerced/validated (no "123" treated as number by accident); numbers range-checked;
  strings length-capped; enums constrained; dates/emails/UUIDs format-checked.
- **Required vs optional** enforced; unknown/extra fields rejected or stripped.
- **Mass assignment**: bind only an explicit allow-list of writable fields — never
  `Model(**req.body)` / `entity.update(req.body)` (attacker sets `is_admin`, `balance`).
  See [[api-security]].
- **Size limits**: max body size, max array length, max string length, max file size —
  before processing (DoS guard; see [[rate-limiting]]).
- **Nested/recursive** payloads bounded (depth) — guards against billion-laughs / deep JSON.
- Injection defense is downstream but related: validated input + parameterized queries /
  output encoding (SQLi → [[database-audit]]; XSS → [[frontend-code-review]]).

## Red flags
- Business logic reading `req.body.x` with no prior schema validation.
- `update(req.body)` spreading arbitrary fields.
- Validation only in the frontend.
- No max length/size → unbounded input.

Related: [[response-validation]], [[api-security]], [[api-design]].
