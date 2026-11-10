---
name: resource-leverage-mapping
description: "Finds the highest-leverage use of available resources — where the same input produces the most output. Triggers: 'resource leverage', 'highest-leverage use', 'where should we put our energy', 'maximize impact', 'leverage mapping'."
---

# Resource Leverage Mapping

Not all uses of a resource are equal. Some produce disproportionate output — because they remove a constraint, create more resources, or unlock other opportunities. Leverage mapping makes that asymmetry visible before resources are committed.

---

## Your Process

**Step 1: Inventory Available Resources**
List all meaningful resources available: time, money, people, attention, relationships, existing assets, reputation. Be specific — "the engineering team" is less useful than "three senior engineers with 20% slack capacity."

**Framing check:** Confirm the specific resource situation before continuing. State what you've identified — the context, the resources in scope, and the allocation question being asked — in one sentence, then use `AskUserQuestion`:
- **Question:** "I'm reading this as: [your one-sentence framing of the resource situation and the core allocation question]. Is that right?"
- **Header:** "Framing"
- **Options:**
  - **Yes — proceed** — framing is correct
  - **Adjust** — one element is off; user will correct it before you continue
  - **Reframe** — different situation than read; incorporate the correction before proceeding

**Step 2: List All Candidate Uses**
For each resource, what are all the plausible ways it could be deployed? Do not filter yet — generate a full list of options.

**Step 3: Estimate Output per Unit of Input**
For each candidate use: what is the likely output for a given unit of input? This doesn't need to be precise — a rough order-of-magnitude estimate is sufficient. The goal is to find the outliers.

**Step 4: Identify Multiplier Effects**
Which uses of a resource create more resources, unlock additional capacity, or enable other uses? These are the highest-leverage options. Examples: building a relationship that opens a distribution channel; shipping a feature that funds the next two.

**Step 5: Find Underused High-Leverage Resources**
Which available resources are currently underused relative to their potential leverage? Relationships, existing data, attention from a key person, and existing assets are commonly overlooked.

**Step 6: Recommend the Highest-Leverage Allocation**
**Before narrowing:** Show the complete set of candidate uses with their estimated output and multiplier effects to the user first. Use `AskUserQuestion`:
- **Question:** "I've identified [N] candidate uses across the resources. Before I select the highest-leverage allocation, are there any you'd flag as especially important, or any I've missed?"
- **Header:** "Prioritise"
- **Options:**
  - **Proceed with your selection** — the set looks right
  - **Flag one** — user will name a specific use to include or prioritise
  - **Add a missing one** — user will describe a candidate use not yet listed

Given the analysis, what is the best deployment of the available resources?

---

## Human Check-in

Before proceeding, use the `AskUserQuestion` tool. State your interpretation of the situation in 1–2 sentences — what is being analyzed and what the core question is — then ask:

- **Question:** "My read: [your 1–2 sentence interpretation]. How do you want to proceed?"
- **Header:** "Scope"
- **Options:**
  - **Full analysis** — Complete all steps, reasoning shown throughout
  - **Key findings only** — Bottom-line output, skip step-by-step detail
  - **Highest leverage use only** — Single best allocation of the scarcest resource
  - **Reframe** — The read is off; correct it and the analysis will follow the corrected framing

Proceed based on their selection. If the user reframes, incorporate the correction before running any analysis.

## Output Format

### Resource Inventory
| Resource | Available Quantity / Capacity |
|----------|------------------------------|
| ... | ... |

### Candidate Uses with Output Estimates
| Resource | Use | Estimated Output per Unit Input | Multiplier Effect? |
|----------|-----|--------------------------------|--------------------|
| ... | ... | Low / Medium / High | Yes / No — [describe] |

### Underused High-Leverage Resources
- [Resource] — current use vs. potential leverage.

### Recommended Allocation
State the highest-leverage deployment with rationale. Make the trade-offs explicit — what is being deprioritised and why.

---

## Notes

Run this before a planning cycle or before committing significant resources to a course of action. The most common finding is that a relationship or an existing asset is being underused relative to its potential leverage.

---

## What's Next

After delivering this output, use `AskUserQuestion` to offer the next move:

- **Question:** "Leverage mapped. What's next?"
- **Header:** "Next"
- **Options:**
  - `/resource-allocation-analysis` — Reallocate resources to the leverage points
  - `/strategy-force-economy` — Deploy effort economically via the leverage found
  - `/systems-leverage-analysis` — Combine resource leverage with systems leverage
  - **Done** — Wrap up and synthesise what we have so far
