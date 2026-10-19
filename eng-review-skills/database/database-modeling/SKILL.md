---
name: database-modeling
description: Design or review a relational/NoSQL data model — entities, relationships, keys, normalization, and deliberate denormalization. Use when designing a schema from requirements, reviewing a proposed data model, deciding SQL vs. NoSQL or how to shape documents, choosing keys and relationships, or when the user says "design the schema", "model this domain", "normalize this", "should this be one table or many", or "relational or document". Covers normal forms, keys/surrogates, relationship cardinality, and when to denormalize.
---

# Database Modeling

Role: data architect. Model the domain's real invariants first; shape for access
patterns second; denormalize only with a measured reason.

## Process
1. List entities and their true identity (natural key? surrogate?).
2. Map relationships and cardinality (1:1, 1:N, M:N → junction table).
3. Normalize to 3NF. Each fact in exactly one place; no partial/transitive dependencies.
4. Only then, denormalize specific hot paths — and write down why.

## Checklist
- **Keys**: stable primary keys; surrogate (`id`) + natural unique constraint where a
  natural key exists; no meaningful data encoded in auto-increment IDs.
- **Relationships**: M:N via junction tables, never comma-lists in a column; FK direction
  matches ownership.
- **Normalization**: no repeating groups, no column that depends on a non-key column.
- **Types**: smallest correct type; exact numerics for money; enums constrained.
- **Nullability**: NULL means "unknown/absent", not "zero"/"false"/"empty" — don't overload it.
- **Temporal/soft-delete**: if history matters, model it (valid-from/to, audit table),
  don't bolt on `is_deleted` and hope.
- **NoSQL**: document shape driven by read patterns; embed vs. reference decided by
  access + update cost + document-size bounds; know you're trading joins for duplication.

## Deliberate denormalization — allowed when
- Read path is measurably hot and the join is the proven cost.
- The duplicated data has a clear owner and a consistency mechanism (trigger, app
  invariant, or eventual-consistency job that's documented).

## Red flags
- One wide table with 60 nullable columns modeling several entities.
- JSON blob holding fields you filter/join on.
- M:N stored as a delimited string.

Grounding: `reference-docs/system-design-primer`. Related: [[database-audit]], [[sql-performance]].
