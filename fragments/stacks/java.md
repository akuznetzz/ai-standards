## Java Stack
- Use modern Java idioms supported by the repository baseline; for greenfield services, prefer Java 21+ style instead of writing new code to legacy Java 8 constraints by habit.
- Prefer immutable value objects, including `record`, for stable domain, transport, and configuration data when framework constraints allow it.
- Keep null-handling explicit; use `Optional` for legitimate absence at API boundaries, and avoid nullable-by-default designs that hide invariants.
- Favor explicit, narrow public contracts when they express a stable capability.
- Keep concurrency and async execution explicit; do not hide executors, schedulers, or reactive concerns inside ordinary service methods.
