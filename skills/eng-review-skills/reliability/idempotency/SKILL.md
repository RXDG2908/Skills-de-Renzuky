---
name: idempotency
description: Design or review operations so that repeating them produces the same result as doing them once — critical for retries, webhooks, payments, and message consumers. Use when a request might be retried, when building webhook/event handlers or payment endpoints, when "at-least-once" delivery can cause double processing, or when the user says "make this idempotent", "we got charged twice", "handle retries safely", "idempotency key", or "exactly-once". Covers idempotency keys, natural idempotency, and dedup windows.
---

# Idempotency

Role: make "run it again" safe. Networks retry, queues deliver at-least-once, users
double-click. Any operation with a side effect that can be retried must be idempotent or
you get double charges, double emails, double rows.

## Techniques (prefer the earliest that fits)
1. **Naturally idempotent operation**: `SET status = 'paid'` (not `balance = balance + x`);
   `PUT` of a full resource (not blind `INSERT`). Design the write so repeating it is a
   no-op.
2. **Idempotency key**: client sends a unique key per logical operation; server records
   `(key → result)` in a unique-constrained table *in the same transaction* as the effect;
   a repeat returns the stored result instead of re-doing it. (Stripe's model.)
3. **Dedup on a natural unique constraint**: e.g. `UNIQUE(order_id, charge_attempt)` so a
   duplicate insert fails cleanly. See [[duplicate-prevention]].
4. **Processed-event log** for consumers: record `event_id` processed; skip if seen.

## Review checklist
- Every retryable side-effecting endpoint/consumer is idempotent by one of the above.
- The idempotency record and the side effect commit **atomically** (same transaction) —
  else a crash between them re-does or loses the work. See [[transaction-safety]].
- Keys have a defined scope and retention (how long is a repeat recognized?).
- Idempotency covers partial failure, not just exact replays.

## Red flags
- Payment/charge endpoint with no idempotency key.
- Webhook handler that `INSERT`s with no dedup — provider retries → duplicates.
- Queue consumer assuming exactly-once delivery (it's at-least-once).
- `balance = balance + amount` on a retryable path.

Grounding: `reference-docs/system-design-primer`. Related: [[duplicate-prevention]],
[[transaction-safety]], [[transaction-integrity]].
