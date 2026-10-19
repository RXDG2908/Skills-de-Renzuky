---
name: rest-api
description: Design or review a RESTful HTTP API specifically — resource modeling, correct HTTP methods and status codes, idempotency/safety semantics, and HTTP conventions. Use when building or reviewing REST/HTTP endpoints, choosing methods and status codes, deciding resource URLs, or when the user says "design REST endpoints", "review this REST API", "right HTTP status code", "should this be PUT or PATCH", or "restful resource design". For transport-agnostic API shape see api-design.
---

# REST API

Role: apply HTTP correctly. REST leans on the protocol's semantics — use them so the API is
predictable to any HTTP client, cache, and proxy. (For overall shape/consistency see
[[api-design]].)

## Methods & semantics
- `GET` — safe (no side effects) and idempotent. Never mutate on GET. Cacheable.
- `POST` — create / non-idempotent action. Returns `201` + `Location` on create.
- `PUT` — full replace, **idempotent** (same request repeated = same state).
- `PATCH` — partial update.
- `DELETE` — idempotent (deleting twice is still "gone").
Make retryable unsafe operations idempotent via a key (see [[idempotency]]).

## Resources & URLs
- Nouns, plural collections: `/orders`, `/orders/{id}`, `/orders/{id}/items`.
- Hierarchy for ownership; query params for filter/sort/paginate — not new endpoints per
  filter.
- No verbs in paths (`/getOrders` ✗). Genuinely non-CRUD actions: a sub-resource or a
  documented action endpoint, consistently.

## Status codes (use the right one)
- 200 ok · 201 created · 202 accepted (async) · 204 no content.
- 400 validation · 401 unauthenticated · 403 unauthorized · 404 not found · 409 conflict
  (e.g. duplicate, version) · 422 semantic validation · 429 rate limited.
- 500 unexpected · 503 unavailable. Never 200 with an error body.

## Checklist
- Methods match semantics; GET is side-effect-free; PUT/DELETE idempotent.
- Status codes correct and consistent; errors use one envelope (see [[response-validation]]).
- Pagination/filtering consistent; `Location` on create.
- Caching headers (`ETag`, `Cache-Control`) where it helps; conditional requests supported.
- Auth on every endpoint (see [[api-security]]); abuse-limited (see [[rate-limiting]]).

## Red flags
- `POST /getUser`; mutating GETs; everything returns 200.
- Non-idempotent PUT; 500 for a validation error.

Related: [[api-design]], [[api-versioning]], [[request-validation]].
