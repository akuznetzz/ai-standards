## TanStack Query Stack
- Use TanStack Query for server-state synchronization, caching, and background refetching; do not treat it as a generic replacement for all local UI state.
- Keep query keys stable, structured, and domain-meaningful so invalidation, refetching, and cache inspection stay predictable.
- Co-locate reusable query and mutation option factories with the feature or entity they serve instead of scattering ad hoc query definitions across components.
- Keep query functions focused on transport and parsing; keep business rules and cross-request orchestration outside raw query callbacks when they need independent testing.
- Handle loading, error, and empty states explicitly at the UI boundary instead of assuming every query resolves successfully.
- After mutations, revalidate affected server state deliberately with targeted invalidation, cache updates, or refetching instead of relying on stale data to self-correct.
- Use optimistic updates only when the interaction clearly benefits from them and rollback or reconciliation behavior is understood.
- Treat prefetching, dehydration, and hydration as boundary concerns for SSR or route transitions, not as hidden side effects spread across unrelated components.
- Prefer framework-specific adapters and provider boundaries for integration; keep query client lifecycle and defaults centralized instead of recreating clients ad hoc.
