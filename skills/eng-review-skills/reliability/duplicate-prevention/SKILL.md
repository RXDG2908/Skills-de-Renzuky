---
name: duplicate-prevention
description: Prevent duplicate records, double submissions, and double processing across a system. Use when guarding against double form submits, duplicate orders/payments, repeated webhook or queue processing, or data deduplication, or when the user says "prevent duplicates", "double submission", "stop double orders", "dedupe this", or "we have duplicate rows". Covers DB unique constraints, client+server submit guards, dedup keys, and why app-only checks fail under concurrency.
---

# Duplicate Prevention

Role: ensure "one logical thing" exists once, even under double-clicks, retries, and
concurrency. The durable guarantee lives in the database, not in app code.

## Layers (defense in depth)
- **Database unique constraint** = the only real guarantee. A `UNIQUE` index on the natural
  business key (`order_id`, `email`, `(user_id, product_id)`, `event_id`) makes a duplicate
  insert fail atomically. App-level "check then insert" has a race window — two requests
  both check, both insert. See [[race-condition]].
- **Idempotency key** for retryable operations (see [[idempotency]]).
- **Server-side submit guard**: dedup token per form render; reject a second use.
- **Client-side** (disable button, debounce) = UX nicety only, never the guarantee.

## Review checklist
- Is there a `UNIQUE` constraint on the real business identity? If dedup relies only on
  `SELECT ... IF NOT EXISTS THEN INSERT`, it's racy — flag it.
- Does the insert handle the unique-violation gracefully (treat as "already exists" success,
  not a 500)?
- Webhooks/queue consumers dedup on provider event id.
- Soft-delete + re-create doesn't resurrect a "duplicate" wrongly.

## Red flags
- `if not exists(...): insert(...)` as the sole guard under concurrency.
- Dedup done only in the frontend.
- Duplicate-row bug "fixed" by a cleanup cron instead of a constraint.
- Catch-all that turns a unique-violation into a hard error for the user.

Related: [[idempotency]], [[race-condition]], [[transaction-integrity]], [[database-audit]].
