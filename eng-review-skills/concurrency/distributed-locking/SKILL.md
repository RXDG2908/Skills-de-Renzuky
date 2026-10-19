---
name: distributed-locking
description: Design or review distributed locks and leader coordination across multiple processes/nodes — and know when NOT to use one. Use when coordinating work across instances, ensuring only one worker runs a job, building a scheduler/cron that must not double-run, implementing a lock in Redis/ZooKeeper/etcd, or when the user says "distributed lock", "only one instance should", "leader election", "Redlock", "prevent double cron", or "mutex across servers". Covers lock requirements (TTL/fencing), Redis/consensus options, and safer alternatives.
---

# Distributed Locking

Role: coordinate across nodes correctly — and first ask whether a lock is even the right
tool. Distributed locks are subtle and often a smell; a uniqueness constraint or idempotent
design is frequently better and safer.

## Prefer these before a lock
- **DB unique constraint / atomic update** — "only once" via the database (see
  [[duplicate-prevention]], [[race-condition]]). No lock needed.
- **Idempotent operation** — if double-execution is harmless, you may not need a lock at all
  (see [[idempotency]]).
- **Single-consumer queue / partitioning** — route all work for a key to one consumer.

## If you do need one — requirements
- **TTL / auto-expiry**: a holder that crashes must not hold the lock forever.
- **Ownership**: only the acquirer can release it (unique token) — never delete another
  holder's lock.
- **Fencing token**: a monotonic token returned on acquire and checked by the protected
  resource — so a paused/expired holder that resumes can't still write. (Redis `SET NX PX`
  alone does **not** give safety under GC pauses/clock issues; Redlock is debated — for
  correctness-critical locks use a consensus system.)
- **The right backend**: Redis (`SET key val NX PX`, `reference-docs/redis-doc`) for
  best-effort/performance; **ZooKeeper/etcd/Consul** for correctness-critical mutual
  exclusion and leader election.

## Review red flags
- `SETNX` with no expiry → permanent lock on crash.
- Releasing without checking ownership → one worker frees another's lock.
- Treating a Redis lock as a hard correctness guarantee for money/data integrity.
- Using a distributed lock where a DB unique constraint would do (simpler + safer).
- Long work holding a lock past its TTL with no fencing → two workers run concurrently.

Related: [[concurrency-control]], [[race-condition]], [[idempotency]], [[chaos-testing]].
