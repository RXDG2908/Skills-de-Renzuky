---
name: database-audit
description: Review a database schema, queries, and access patterns for correctness, integrity, performance, and security risks. Use when auditing a database, reviewing schema changes, assessing a data layer before shipping, diagnosing data-integrity problems, or when the user asks to "audit the database", "review this schema", "check our data model", or "is this DB design sound". Covers normalization vs. deliberate denormalization, constraints, indexing, N+1 and slow-query risks, injection-safe access, and migration safety. For deep single-topic passes, delegate to sql-performance, database-modeling, transaction-integrity, or migration-review.
---

# Database Audit

Role: senior data engineer doing a source-grounded review. A finding needs a concrete
failure (wrong result, data corruption, slow query under real load, security hole), the
evidence (schema/query/line), severity, and the smallest effective fix. No vague "could
be better".

## When to use

Broad first pass over a data layer. Then hand specific axes to the focused skills:
[[sql-performance]], [[database-modeling]], [[transaction-integrity]], [[migration-review]].

## Checklist

**Integrity**
- Every FK relationship enforced by an actual `FOREIGN KEY` constraint, not just app code.
- `NOT NULL`, `UNIQUE`, `CHECK` constraints match the real business invariants.
- No orphan rows possible; cascade behavior (`ON DELETE`) is intentional, not default.
- Money/quantities use exact types (`DECIMAL`/`NUMERIC`), never `FLOAT`.
- Timestamps store timezone (UTC) consistently.

**Correctness & modeling**
- Normalized to 3NF unless denormalization is deliberate and documented (see [[database-modeling]]).
- No EAV/"god table"/JSON-blob-as-schema where real columns belong.
- Enum-like columns constrained (CHECK or lookup table), not free text.

**Performance**
- Indexes on every FK and on columns in `WHERE`/`JOIN`/`ORDER BY` of hot queries.
- No unindexed full-table scans on large tables; no N+1 from the ORM (see [[sql-performance]]).
- Composite index column order matches query predicates (leftmost-prefix rule).

**Security**
- All access parameterized/prepared — zero string-concatenated SQL (OWASP: SQL Injection
  Prevention Cheat Sheet; see `reference-docs/CheatSheetSeries`).
- Least-privilege DB accounts; app does not connect as superuser/owner.
- No secrets, PII, or tokens stored unencrypted where they shouldn't be.

**Operability**
- Migrations are reversible and safe under concurrent writes (see [[migration-review]]).
- Transactions wrap multi-statement invariants (see [[transaction-integrity]]).

## Red flags (stop and flag)
- `SELECT *` in application code paths; queries built by string concatenation.
- A multi-row money operation with no transaction.
- A new `NOT NULL` column added to a large table with no default + backfill plan.
- "We enforce that in the application" for a cross-table invariant.

## Output
Findings list, most-severe first: file/query → what breaks → severity → fix. Separate
confirmed issues from lower-confidence ones.
