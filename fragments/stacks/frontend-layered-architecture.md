## Frontend Layered Architecture

### Scope
- Use this fragment when the frontend is large enough to benefit from explicit boundaries between UI composition, stateful workflows, domain logic, and infrastructure concerns.
- Keep the structure pragmatic; do not introduce extra layers unless they have a stable responsibility and a clear review benefit.

### Boundaries
- Keep components focused on rendering and interaction wiring; move reusable business workflows, state transitions, and integration logic into dedicated modules or slices.
- Keep data-fetching, caching, and mutation orchestration out of ad hoc component trees when the application needs shared or cross-screen behavior.
- Expose public APIs for architectural units that are meant to be reused, and avoid deep imports into another unit's internal files.
- Keep framework bootstrap, routing setup, and environment wiring separate from feature or domain logic.

### Consistency
- Keep dependency direction explicit so broader UI composition layers depend on lower-level feature or shared foundations, not the reverse.
- Treat shared frontend infrastructure as a stable foundation, not as a dumping ground for unrelated feature code.
