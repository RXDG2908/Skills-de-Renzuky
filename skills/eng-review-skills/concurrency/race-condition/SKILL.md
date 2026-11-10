---
name: race-condition
description: Find and fix race conditions — bugs where the outcome depends on timing/interleaving of concurrent operations. Use when debugging intermittent/"sometimes" bugs, reviewing concurrent code, check-then-act patterns, shared mutable state, or when the user says "race condition", "works sometimes", "intermittent bug", "TOCTOU", "double submit creates two rows", or "concurrent update lost". Covers check-then-act/TOCTOU, lost updates, shared-state hazards, and the fixes (atomicity, locks, constraints).
---

# Race Condition

Role: hunt timing bugs. A race exists whenever correctness depends on the order/interleaving
of concurrent operations and that order isn't guaranteed. Symptoms: "works 99% of the
time", "only under load", "two rows appeared".

## Classic shapes
- **Check-then-act / TOCTOU**: `if not exists → create`, `if balance >= x → deduct`,
  `if (!locked) lock()`. Two threads both pass the check, both act. → make it atomic.
- **Lost update**: read value → compute → write back; a concurrent writer's change is
  clobbered. → atomic in-DB update, row lock (`SELECT ... FOR UPDATE`), or optimistic
  version column (see [[transaction-integrity]]).
- **Read-modify-write on shared memory/counter** without synchronization.
- **Double submit / duplicate**: two requests create two rows. → unique constraint (see
  [[duplicate-prevention]]).
- **Init/singleton race**; **cache stampede** (many misses recompute at once).
- **Async UI race**: an older fetch resolves after a newer one and overwrites state (see
  [[frontend-code-review]]).

## Fixes (prefer earliest)
1. **Make it atomic** — single atomic operation instead of check-then-act (`UPDATE ... WHERE
   x >= 1`, atomic `INCR`, compare-and-swap).
2. **Database constraint** — let `UNIQUE` reject the duplicate atomically.
3. **Locking** — row lock / optimistic version / distributed lock when the invariant spans
   calls (see [[distributed-locking]], [[concurrency-control]]).

## Review red flags
- Any `check … then … act` on shared/persistent state without a lock, constraint, or atomic
  op.
- `balance = balance - x` read-compute-write in app code.
- Intermittent duplicate rows → missing unique constraint.
- Cancelable async not cancelled; later response overwrites newer state.

## Output
Per race: the interleaving that breaks it, how to reproduce (load/concurrency), and the
atomic/locked/constrained fix. Related: [[concurrency-control]], [[transaction-integrity]], [[idempotency]].
