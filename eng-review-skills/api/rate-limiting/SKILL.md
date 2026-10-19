---
name: rate-limiting
description: Design or review rate limiting and throttling to protect an API from abuse and overload. Use when adding rate limits, protecting endpoints from brute-force or scraping, shaping traffic, choosing a limiting algorithm, or when the user says "add rate limiting", "throttle this endpoint", "prevent abuse/brute force", "token bucket vs sliding window", or "429 handling". Covers algorithms, per-key scoping, distributed counters, response headers, and what to limit.
---

# Rate Limiting

Role: protect availability and block abuse without punishing legitimate bursts. A limit is
only real if it's enforced server-side and works across all app instances.

## Algorithms
- **Token bucket** — allows bursts up to bucket size, refills at a steady rate. Good general
  default for APIs.
- **Sliding window (log/counter)** — smooth, accurate; more state.
- **Fixed window** — simplest but allows 2× burst at window edges.
- **Leaky bucket** — smooths output to a constant rate (shaping).

## Design checklist
- **Scope the key** right: per API key / per user / per IP / per endpoint — and combine
  (a per-IP limit plus a per-account limit). Auth endpoints need a tight per-account +
  per-IP limit against credential stuffing (see [[api-security]]).
- **Distributed counter**: enforce in a shared store (Redis) so all instances share the
  limit — an in-memory per-instance counter is bypassed by load balancing. (`reference-docs/
  redis-doc` for `INCR`/`EXPIRE` and token-bucket patterns.)
- **Response**: `429 Too Many Requests` + `Retry-After`; expose `RateLimit-Limit/-Remaining/
  -Reset` headers so good clients back off.
- **Tiers & fairness**: different limits per plan; a heavy user can't starve others.
- **Cost-based** for expensive/variable endpoints (weight by query cost), not just request
  count.
- **Fail-open vs fail-closed**: decide what happens if the limiter store is down (usually
  fail-open for availability, with alerting — but fail-closed for auth).

## Red flags
- Rate limit kept in process memory with multiple instances → not enforced.
- No limit on login/OTP/password-reset → brute-force open.
- 429 with no `Retry-After`; clients hammer harder.
- Only per-IP (NAT/proxy shares IPs) or only per-account (IP rotation) — need both.

Related: [[api-security]], [[stress-testing]], [[distributed-locking]].
