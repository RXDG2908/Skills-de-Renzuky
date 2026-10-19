---
name: stress-testing
description: Plan and review stress tests that push a system past its limits to find the breaking point and how it fails. Use when finding capacity limits, verifying graceful degradation, testing behavior beyond expected load, or when the user says "stress test", "find the breaking point", "what happens when it's overloaded", "does it degrade gracefully", or "spike test". Covers overload/spike/soak profiles, failure-mode observation, and recovery. For in-target validation see load-testing.
---

# Stress Testing

Role: break it on purpose, safely, to learn *how* it fails and whether it recovers. Load
testing proves it holds at target ([[load-testing]]); stress testing finds the cliff.

## Profiles
- **Overload**: ramp past target until something gives — record the breaking point (rps,
  concurrency) and the first thing that breaks.
- **Spike**: sudden jump to many × normal (flash sale, cron thundering herd) — does
  autoscaling/queueing absorb it or does it fall over?
- **Soak**: sustained load for hours — reveals leaks (memory, connections, file handles)
  and slow degradation.

## What to observe at/after the limit
- **Failure mode**: does it shed load gracefully (429s, backpressure, circuit-break) or
  cascade/crash? Graceful degradation is the goal, not infinite capacity.
- **Blast radius**: one overloaded component taking down unrelated ones (shared pool,
  retries amplifying load — the retry storm).
- **Recovery**: when load drops, does it recover on its own, or need a restart?
- **Data integrity under overload**: no lost/duplicated writes when things time out (see
  [[idempotency]], [[duplicate-prevention]]).

## Red flags
- No circuit breakers / timeouts → one slow dependency hangs everything.
- Unbounded retries → clients amplify an outage into a storm.
- Unbounded queues/buffers → OOM instead of backpressure.
- Never tested recovery, only the break.

Grounding: `reference-docs/system-design-primer`. Related: [[load-testing]], [[chaos-testing]], [[rate-limiting]].
