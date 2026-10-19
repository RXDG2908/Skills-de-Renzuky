---
name: concurrency-control
description: Choose and review concurrency-control strategy — optimistic vs pessimistic locking, isolation, and safe handling of shared state under parallelism. Use when multiple actors update the same data, choosing optimistic vs pessimistic locking, preventing lost updates/deadlocks, designing safe concurrent access, or when the user says "optimistic vs pessimistic locking", "concurrency control", "prevent lost updates", "version column", "deadlock", or "handle concurrent edits". Covers the optimistic/pessimistic trade-off, version/ETag flows, deadlock avoidance, and in-process concurrency hazards.
---

# Concurrency Control

Role: pick the mechanism that keeps shared data correct under parallelism at the lowest
cost. Sits above [[race-condition]] (the bugs) and [[distributed-locking]] (cross-node) —
this is choosing the strategy.

## Optimistic vs pessimistic
- **Optimistic** (version/ETag): read with a version; on write, `UPDATE ... WHERE
  version = N`; if 0 rows updated, someone else won → reject with a conflict (HTTP `409`)
  and let the caller retry/merge. Best when **conflicts are rare** — no locks held, scales
  well. The default for web edit flows (If-Match/ETag).
- **Pessimistic** (`SELECT ... FOR UPDATE` / row lock): lock before modifying so others
  wait. Best when **conflicts are frequent** or a retry is expensive/impossible. Costs: held
  locks, contention, deadlock risk, pool pressure — keep the critical section tiny.

## Essentials
- **Lost-update prevention** is the core job: never read-compute-write a shared value
  without version check, lock, or atomic in-DB operation (see [[transaction-integrity]]).
- **Isolation level** is part of this choice — know what anomalies your default level still
  permits.
- **Deadlock avoidance**: acquire locks in a consistent global order everywhere; keep
  transactions short; set lock/statement timeouts; retry on deadlock.
- **In-process** (threads/async): protect shared mutable state with the language's
  primitives; prefer immutable data and message-passing over shared memory; beware the
  async "await in the middle of a critical section" gap.
- **Conflict UX**: a 409/version-conflict needs a real user path (reload, merge, or
  last-write-wins *by decision*) — see [[ux-review]].

## Red flags
- Pessimistic locks held across network/user waits.
- Optimistic writes with no version/ETag check (so "optimistic" protects nothing).
- Inconsistent lock ordering → deadlocks under load.
- "Last write wins" by accident (silent lost update) rather than by decision.

Related: [[race-condition]], [[transaction-integrity]], [[distributed-locking]].
