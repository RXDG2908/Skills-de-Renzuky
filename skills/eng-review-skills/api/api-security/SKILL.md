---
name: api-security
description: Review an API for security vulnerabilities against the OWASP API Security Top 10 — authz, authn, data exposure, and abuse. Use when securing or reviewing an API, assessing endpoints for auth and access-control holes, checking for excessive data exposure, or when the user says "secure this API", "review API security", "is this endpoint safe", "BOLA/IDOR check", "auth on this API", or "OWASP API top 10". Covers object/function-level authorization, authentication, data exposure, mass assignment, and SSRF. Grounded in OWASP API Security & Cheat Sheets.
---

# API Security

Role: offensive-minded reviewer, defensive fix. Grounded in OWASP API Security Top 10
(`reference-docs/API-Security`) and the OWASP Cheat Sheets (`reference-docs/CheatSheetSeries`).
Every finding: the vulnerable endpoint, the exploit, severity, the fix.

## OWASP API Top 10 — the checklist
- **API1 BOLA (object-level authz / IDOR)**: `GET /orders/{id}` must verify the caller owns
  that object, not just that they're logged in. The #1 API vuln. Check **every** object
  access, including nested and in bulk endpoints.
- **API2 Broken authentication**: tokens validated (signature, expiry, audience); no weak
  JWT (`alg:none`, guessable secret); credential-stuffing/brute-force throttled (see
  [[rate-limiting]]).
- **API3 Broken object property authz / excessive data exposure**: don't return full
  objects and rely on the client to hide fields; don't accept arbitrary fields —
  **mass-assignment**: whitelist writable properties (see [[request-validation]]).
- **API4 Resource consumption**: pagination caps, payload-size limits, rate limits, query
  cost limits (esp. GraphQL depth).
- **API5 Function-level authz**: admin/privileged endpoints check role, not just auth.
- **API6 Sensitive business flows**: abuse-protected (bots buying all stock, etc.).
- **API7 SSRF**: never fetch a user-supplied URL without allowlist + egress controls.
- **API8 Misconfiguration**: CORS not `*` with credentials; security headers; verbose
  errors/stack traces off in prod.
- **API9 Inventory**: no forgotten/undocumented/old-version endpoints exposed.
- **API10 Unsafe third-party consumption**: validate data from upstream APIs too.

## Always
- Authorization checked server-side on every request (never trust client claims/hidden
  fields). Parameterized queries (no SQLi — see [[database-audit]]). Secrets not in code/
  logs. TLS enforced.

## Red flags
- Endpoint authenticates but never checks ownership (BOLA).
- `User.update(req.body)` — mass assignment.
- Server fetches `req.body.url`.
- Role check only in the UI.

Related: [[api-design]], [[rate-limiting]], [[request-validation]].
