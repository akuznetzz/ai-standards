<!-- Source: https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/java-springboot-jpa-cursorrules-prompt-file/.cursorrules -->
<!-- Imported: 2026-04-07 -->
<!-- Adaptation: normalized for UMA2, reduced to durable Java Spring guidance, and adjusted to modern DI and layering practices -->

## Java Spring Stack
- Keep controllers thin and limit them to HTTP boundary concerns.
- Keep business logic in services and keep persistence concerns behind repositories.
- Do not inject repositories directly into controllers.
- Use DTOs for transport-layer contracts between HTTP boundaries and application services.
- Do not expose JPA entities as public API contracts unless the repository already standardizes on that pattern.
- Prefer immutable DTOs such as `record` when they fit the project conventions and validation needs.
- Validate inputs explicitly at the boundary and model layers where the contract requires it.
- Prefer constructor injection over field injection.
- Use explicit transactional boundaries for multi-step write flows and other consistency-sensitive operations.
- Treat relationship loading deliberately; prefer lazy loading by default and address N+1-sensitive queries explicitly.
- Keep REST routes resource-oriented and avoid action verbs in endpoint paths.
- Raise explicit exceptions with actionable context for missing records and other business failures.
- Use JPQL, derived queries, or native SQL deliberately based on clarity, correctness, and the query shape instead of enforcing one query style everywhere.
- Use interface-plus-implementation service layering only when it adds a stable boundary or improves testability; do not force the pattern mechanically.
