---
name: transaction-integrity
description: Review database transaction usage for atomicity, isolation, and consistency. Use when multi-statement writes must all-or-nothing succeed, when money/inventory/counters are updated, when you see lost updates or phantom reads, when choosing an isolation level, or when the user says "wrap this in a transaction", "is this atomic", "we got a double charge", "lost update", or "what isolation level". Covers ACID boundaries, isolation levels and their anomalies, lock scope, and SELECT ... FOR UPDATE.
---

# Transaction Integrity

Role: reliability engineer for the data layer. Any invariant that spans more than one row
or statement must hold even under concurrency and partial failure.

## Checklist
- **Atomic boundary**: every set of writes that must succeed together is in one
  transaction; nothing that must be atomic spans two transactions or two services
  without a saga/outbox.
- **Isolation level fits the risk**:
  - `READ COMMITTED` (default) still allows non-repeatable reads & lost updates.
  - Read-modify-write on a counter/balance needs `SELECT ... FOR UPDATE`, an atomic
    `UPDATE ... SET x = x - 1 WHERE x >= 1`, or `REPEATABLE READ`/`SERIALIZABLE`.
- **Lost update**: two readers compute from a stale value and both write → use row locks,
  optimistic concurrency (version column), or atomic in-DB arithmetic. See [[concurrency-control]].
- **Lock scope**: transactions kept short; no network/API calls or user waits inside an
  open transaction (holds locks, exhausts the pool).
- **Deadlocks**: consistent lock ordering across code paths; retry on deadlock errors.
- **Error paths**: rollback on every failure branch; no "commit in a finally".
- **Cross-service**: distributed invariants use outbox + idempotent consumer or a saga
  with compensations — not a 2-phase hope. See [[transaction-safety]], [[idempotency]].

## Red flags
- `balance = balance - amount` computed in app code then written back, no lock/version.
- An HTTP call or sleep between `BEGIN` and `COMMIT`.
- Catch block that swallows the error and lets the transaction commit.
- "Double charge"/"inventory went negative" reports → almost always a missing lock here.

## Output
Per issue: the unprotected invariant, the concurrent interleaving that breaks it, and the
fix (lock, atomic update, isolation bump, or version column). Related: [[race-condition]].
