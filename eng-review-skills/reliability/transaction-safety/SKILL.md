---
name: transaction-safety
description: Ensure operations that span services, queues, or external calls stay consistent despite partial failure — the distributed-transaction problem. Use when a workflow touches a DB plus a queue/third-party API, when "the DB committed but the message never sent" (or vice versa), when designing sagas or an outbox, or when the user says "distributed transaction", "dual write", "outbox pattern", "saga", "keep these two systems consistent", or "what if the second step fails". Covers the dual-write problem, transactional outbox, sagas with compensation, and at-least-once + idempotent consumers.
---

# Transaction Safety (across boundaries)

Role: keep multiple systems consistent when you can't wrap them in one ACID transaction.
Within one database, use [[transaction-integrity]]. The moment a workflow also touches a
queue, cache, or external API, a plain transaction no longer covers you.

## The dual-write problem
`commit DB; then publish message` — if the process crashes between them, the DB changed but
the message never went (or the reverse). Two systems, no shared transaction. Do **not**
"just put them close together and hope".

## Patterns
- **Transactional outbox**: write the business row AND an `outbox` row in the **same** DB
  transaction; a separate relay publishes outbox rows to the queue and marks them sent.
  The DB commit is the single source of truth; publishing becomes retryable/idempotent.
- **Saga**: a multi-step workflow as a sequence of local transactions, each with a
  **compensating** action to undo prior steps on failure (e.g. reserve → charge → ship;
  if charge fails, release the reservation). Choreography (events) or orchestration.
- **At-least-once + idempotent consumer**: assume messages redeliver; make the consumer
  idempotent (see [[idempotency]]) so reprocessing is safe.
- **Inbox/processed-log** on the consumer side to drop duplicates.

## Review checklist
- No dual write where a crash between steps corrupts consistency — outbox or saga instead.
- Consumers are idempotent and handle redelivery and out-of-order.
- Compensations exist and are themselves idempotent/retryable.
- Failure of step N leaves the system in a defined, recoverable state, not half-done.

## Red flags
- `await db.commit(); await queue.publish()` with nothing handling a crash in between.
- A saga with no compensation for a step.
- Assuming the message bus is exactly-once.

Grounding: `reference-docs/system-design-primer`. Related: [[idempotency]], [[transaction-integrity]], [[chaos-testing]].
