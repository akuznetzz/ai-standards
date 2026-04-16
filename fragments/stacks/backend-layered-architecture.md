## Backend Layered Architecture

### Scope
- Use this fragment when a backend service wants explicit separation between transport boundaries, application orchestration, persistence, and external integrations.
- Keep framework entry points thin and move business workflows into an application or service layer with stable contracts.

### Boundaries
- Treat controllers, routes, handlers, jobs, and CLI commands as transport or execution boundaries rather than as the home of business rules.
- Keep application or service layers focused on use-case orchestration, validation placement, and business decisions; do not spread those responsibilities across repositories, ORM models, or transport adapters.
- Keep database access behind persistence abstractions that match the chosen stack, whether that means repositories or an explicitly documented framework-native alternative.
- Encapsulate outbound protocols such as HTTP, queues, or object storage behind adapter-style boundaries so external integration details do not leak into business workflows.

### Consistency
- Define transactional boundaries explicitly around consistency-sensitive workflows instead of letting persistence calls commit opportunistically.
- Trigger side effects that depend on successful persistence after the transaction boundary, not mid-transaction.
