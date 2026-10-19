---
name: load-testing
description: Plan and review load tests that verify a system meets its performance targets at expected traffic. Use when validating throughput/latency SLOs, sizing capacity before a launch, reviewing a load-test plan, or when the user says "load test this", "can it handle X rps", "will it survive the launch", "what's our p99 under load", or "capacity planning". Covers realistic workload modeling, SLO targets, ramp profiles, and reading the results. For breaking-point testing see stress-testing.
---

# Load Testing

Role: prove the system meets its targets under **expected** load. Load testing answers
"does it hold at the traffic we plan for, within our latency budget?" (Breaking it on
purpose is [[stress-testing]].)

## Before running
- Define SLOs: target throughput (rps), latency (p50/p95/**p99**), error-rate ceiling.
  Averages lie — target tail latency.
- Model a **realistic** workload: the real mix of endpoints, think-time, payload sizes,
  cache hit/miss ratio, authenticated vs anonymous. A flat hammer on one endpoint
  misleads.
- Use production-like data volume and infra; a load test against an empty DB is fiction.

## Running
- Warm up, then ramp to target and hold (steady-state), not an instant spike.
- Isolate the variable; change one thing between runs.
- Capture server-side too: CPU, memory, DB connections, GC, queue depth — not just client
  numbers.

## Reading results
- Report p95/p99 and error rate at target load, plus where latency starts to climb.
- Find the bottleneck: DB connections saturated? CPU-bound? lock contention (see
  [[concurrency-control]])? N+1 under load (see [[sql-performance]])?
- Verify rate limiting / backpressure behaves (see [[rate-limiting]]).

## Red flags
- Only average latency reported.
- Tested one endpoint in isolation and called it "the system".
- Ran against a tiny dataset / dev-sized infra.
- No server-side metrics, so the bottleneck is unknown.

Grounding: `reference-docs/system-design-primer` (performance vs scalability, back-of-the-
envelope). Related: [[stress-testing]], [[chaos-testing]].
