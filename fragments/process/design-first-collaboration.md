## Design-First Collaboration
- Start by naming the change intent, boundaries, and non-goals before implementation.
- Make architecture constraints explicit before touching code.
- Prefer stable contracts and composition over ad hoc coupling.
- Separate discovery, decision, and implementation concerns.
- When ambiguity remains, capture the decision point and the tradeoff instead of silently guessing.
- Stop and request review when continued execution would require choosing a new design direction or materially widening the agreed scope.
- Keep architectural reasoning visible enough that another agent can continue the work safely.

## Planning Discipline
- Use an explicit plan when the task involves architecture decisions, multiple dependent steps, migration risk, or non-trivial verification.
- If new constraints, contradictions, or failed verification invalidate the current approach, re-plan before continuing.
- Keep the planning overhead proportional to the task; do not force heavy process onto small local changes.
