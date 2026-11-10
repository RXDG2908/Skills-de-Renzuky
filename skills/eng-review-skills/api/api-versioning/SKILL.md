---
name: api-versioning
description: Design or review how an API evolves without breaking existing clients — versioning strategy, breaking vs non-breaking changes, and deprecation. Use when making a breaking API change, choosing a versioning scheme, planning deprecation of an old version/field, or when the user says "version this API", "is this a breaking change", "how do we deprecate", "v1 vs v2", or "evolve the API safely". Covers what counts as breaking, versioning schemes, and deprecation process.
---

# API Versioning

Role: let the API change without a flag day for consumers. The default is **don't break
them**; version only when you must.

## Breaking vs non-breaking
**Non-breaking (additive, no version bump):**
- Add a new optional request field; add a new response field; add a new endpoint; add a new
  optional query param; add a new enum value *only if clients tolerate unknowns*.

**Breaking (needs a version / migration):**
- Remove/rename a field or endpoint; change a field's type or meaning; make an optional
  field required; change defaults, error codes, or pagination semantics; tighten
  validation on existing inputs.

Consumers must ignore unknown fields (Postel) so additive changes stay safe — note it in
the contract.

## Schemes (pick one, apply consistently)
- **URI path** `/v1/` — simplest, most visible, cache/proxy friendly. Common default.
- **Header / media-type** (`Accept: application/vnd.api.v2+json`) — cleaner URLs, less
  obvious.
- Avoid per-endpoint ad-hoc versioning; be consistent across the API.

## Deprecation process
- Announce + document; send `Deprecation`/`Sunset` headers; log/measure usage of the old
  version or field.
- Give a real window; don't remove until usage ~0 or the window passes.
- Run old and new in parallel during migration (expand/contract, like [[migration-review]]).

## Review checklist
- Is this change actually breaking? If yes, is it versioned or gated?
- Can old and new clients both work during rollout?
- Is there a deprecation path with measurement, not an instant removal?

## Red flags
- Changing a field's meaning in place "to avoid a v2".
- Removing a field with live consumers and no sunset.
- Inconsistent versioning across endpoints.

Related: [[api-design]], [[rest-api]], [[migration-review]].
