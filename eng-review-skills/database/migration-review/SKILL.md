---
name: migration-review
description: Review a database migration for safety under production load and for reversibility before it ships. Use when reviewing a schema migration, adding/dropping/renaming a column or table, changing a type, adding a constraint or index on a large table, or when the user says "is this migration safe", "review this migration", "will this lock the table", "zero-downtime migration", or "how do we roll this back". Covers locking behavior, expand/contract, backfills, and rollback.
---

# Migration Review

Role: the engineer who gets paged if this migration locks a 50M-row table at peak. Assume
the migration runs against live traffic unless proven otherwise.

## Checklist
- **Locking**: does the DDL take a long/exclusive lock? (e.g. Postgres: adding a column
  *with a volatile default* on old versions rewrites the table; MySQL varies by engine.)
  Prefer operations that are metadata-only or online.
- **Add NOT NULL safely**: add nullable → backfill in batches → add `NOT NULL`/CHECK with
  `NOT VALID` then `VALIDATE` — never one blocking statement on a big table.
- **Index creation**: `CREATE INDEX CONCURRENTLY` (Postgres) / online DDL — not a plain
  blocking `CREATE INDEX` on a hot table.
- **Expand/contract for renames & type changes**: add new → dual-write/backfill → switch
  reads → drop old, across separate deploys. Never rename-in-place a column the running
  app still reads.
- **Reversibility**: a `down`/rollback exists and is tested; or the change is forward-only
  by deliberate design (documented). Dropping a column is destructive — confirm no reader.
- **Data loss**: destructive steps (drop, truncate, type-narrowing) are called out, backed
  up, and intentional.
- **Backfill**: batched, throttled, resumable; not one giant `UPDATE` holding locks.
- **Ordering with code deploy**: the migration is compatible with BOTH the old and new app
  version during the rollout window (no "big bang" that assumes instant cutover).

## Red flags
- `ALTER TABLE big_table ADD COLUMN ... NOT NULL DEFAULT ...` as a single statement.
- Plain `CREATE INDEX` on a large, write-heavy table.
- Renaming/dropping a column in the same deploy the app switches to the new name.
- No rollback and no note saying why forward-only is safe.

## Output
Verdict (safe / needs changes), the specific locking/compat risk, and the safe rewrite
(expand-contract steps or concurrent/batched form). Related: [[transaction-integrity]], [[database-audit]].
