---
name: sql-performance
description: Diagnose and fix slow SQL and ORM query performance. Use when a query or endpoint is slow, when reviewing data-access code for scalability, when an EXPLAIN plan shows full scans, when you suspect N+1 queries, or when the user says "this query is slow", "optimize this SQL", "why is the DB hammered", "fix the N+1", or "add the right index". Covers EXPLAIN/query-plan reading, indexing strategy, N+1 elimination, pagination, and avoiding over-fetching.
---

# SQL Performance

Role: performance engineer. Measure before and after; every recommendation is justified
by the query plan or row counts, not a hunch.

## Method
1. Get the actual slow query (from logs/APM), not a guess.
2. Run `EXPLAIN (ANALYZE, BUFFERS)` (Postgres) / `EXPLAIN` (MySQL). Read it: seq scan vs.
   index scan, rows estimated vs. actual, sort/hash spills to disk.
3. Fix the biggest cost node first. Re-measure.

## Checklist
- **Indexing**: predicate/join/order columns indexed; composite order follows leftmost
  prefix; covering index for hot read paths; no redundant/unused indexes bloating writes.
- **N+1**: ORM lazy-loads in a loop → batch with eager load / `IN (...)` / join. One of
  the most common real-world killers.
- **Over-fetching**: select only needed columns; avoid loading full rows/blobs to count.
- **Pagination**: keyset/seek pagination for deep pages, not `OFFSET n` on large tables.
- **Functions on indexed columns**: `WHERE lower(email)=...` defeats the index unless a
  functional index exists.
- **Implicit casts**: type mismatch in a predicate silently disables index use.
- **Large `IN` lists / `OR` chains**: consider `= ANY`, temp table, or rewrite.
- **Aggregations**: pre-aggregate / materialized view for expensive repeated rollups.
- **Connection/transaction scope**: long transactions holding locks; pool exhaustion.

## Red flags
- `rows removed by filter` huge in EXPLAIN → missing/wrong index.
- Same query shape fired hundreds of times per request → N+1.
- `OFFSET 100000` → will degrade linearly.

Grounding: `reference-docs/system-design-primer` (scaling the database, caching).

## Output
Per issue: the query, its plan cost, the fix (exact index DDL or rewrite), expected
improvement. Related: [[database-audit]], [[database-modeling]].
