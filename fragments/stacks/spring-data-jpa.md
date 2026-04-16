## Spring Data JPA Stack
- Keep persistence concerns behind repositories or dedicated data-access components, and do not inject repositories directly into controllers.
- Use DTOs or projections for transport and read models; do not expose JPA entities as public API contracts by default.
- Prefer immutable DTOs such as `record` when they fit the project conventions and validation needs.
- Treat fetch plans deliberately; keep associations lazy by default and shape read models explicitly with projections, entity graphs, fetch joins, or dedicated queries.
- Do not rely on incidental lazy loading outside a well-defined transactional boundary.
- Use derived queries, JPQL, Criteria, or native SQL deliberately based on query shape, clarity, and correctness instead of standardizing on one style mechanically.
- Keep write transactions explicit for multi-step mutations, and make locking choices visible where consistency depends on them.
- Test persistence behavior against the real database behavior that matters to the project; use Testcontainers-backed integration tests when dialect or transaction semantics are important.
