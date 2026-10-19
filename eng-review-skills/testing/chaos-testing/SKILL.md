---
name: chaos-testing
description: Plan and review chaos/resilience experiments that inject failures into a system to verify it survives real-world faults. Use when validating resilience of a distributed system, designing failure-injection experiments, reviewing fault tolerance before a launch, or when the user says "chaos testing", "chaos engineering", "what if a node dies", "inject failures", "test resilience", or "will it survive a dependency outage". Covers hypothesis-driven experiments, blast-radius control, and the failures worth injecting.
---

# Chaos Testing

Role: resilience engineer. Chaos engineering is **hypothesis-driven**: "we believe the
system tolerates failure X with no user-visible impact" — then prove it in a controlled
blast radius, ideally eventually in production.

## Method
1. Define steady state (the metric that says "healthy": success rate, latency).
2. Hypothesize: injecting fault X keeps steady state within bounds.
3. Inject in the smallest blast radius (one instance, one AZ, small traffic %).
4. Measure vs. steady state. If it breaks, you found a real weakness — fix, re-run.
5. Have an abort/rollback switch always.

## Failures worth injecting
- Kill an instance / pod mid-request.
- A dependency is slow (latency injection) or down (error injection) — the common cause of
  cascading failure.
- Network partition / packet loss between services.
- Resource exhaustion (CPU/mem/disk full).
- Clock skew; DNS failure; expired cert.

## What it validates
- Timeouts, retries (with jittered backoff, bounded), and circuit breakers actually work.
- Graceful degradation / fallbacks, not cascade (see [[stress-testing]]).
- Idempotent retries don't double-process (see [[idempotency]]).
- Failover and self-healing recover steady state.

## Red flags / prerequisites
- Don't start chaos in prod without monitoring, alerting, and an abort switch.
- No defined steady-state metric → you can't tell if the experiment failed.
- Injecting broad faults with no blast-radius limit.
- Running chaos before the basics (timeouts, retries, health checks) even exist.

Related: [[stress-testing]], [[load-testing]], [[distributed-locking]].
