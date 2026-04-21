<!--
Source provenance:
- Adopted on 2026-04-13 from an external workflow-orchestration rule set and a reviewed article about prompt tactics.
- Adaptation goal: keep durable reasoning-quality rules, reject model-specific incentive and emotional nudges.
-->

## Reasoning Hygiene
- For complex or ambiguous tasks, structure the work step by step instead of jumping straight to the answer.
- Make assumptions, edge cases, and verification points explicit when they affect correctness.
- Prefer self-review in the form of gaps, risks, and missing evidence over vague confidence claims.
- If using a role, make it task-specific and constraint-bearing rather than generic persona fluff.
- Do not rely only on upfront reasoning for non-trivial implementation tasks; re-evaluate locally while writing or modifying the current slice.
- Concentrate extra reasoning at points of local uncertainty or correctness risk instead of spreading it uniformly across the whole response.
- Before editing risky logic, perform a short local check of assumptions, invariants, boundary conditions, and likely failure modes for that exact fragment.
- Treat index math, assignments, returns, state transitions, error paths, schema and data mapping, and cross-boundary calls as default high-attention zones.
- After a risky local change, run or propose the most targeted verification that can confirm this fragment before continuing.
- Reject prompt tricks that rely on incentives, emotional pressure, or challenge language as shared engineering standards.
