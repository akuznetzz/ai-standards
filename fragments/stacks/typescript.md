<!-- Source: https://github.com/PatrickJS/awesome-cursorrules/tree/main -->
<!-- Additional references: official TypeScript docs and typescript-eslint guidance -->
<!-- Imported: 2026-04-15 -->
<!-- Adaptation: normalized for UMA2, reduced to durable TypeScript guidance, and stripped of framework-specific and overly prescriptive style rules -->

## TypeScript Stack
- Prefer strict TypeScript configuration and keep compiler guarantees strong instead of weakening types to silence errors.
- Avoid `any`; use `unknown`, narrowing, and explicit domain types where the value shape is not yet proven.
- Add explicit types at public and shared module boundaries, including exported functions, shared utilities, and external adapters.
- Keep local types close to where they are used; extract shared types only when they cross module boundaries or are reused.
- Prefer discriminated unions, utility types, and type guards over broad assertions and duplicated shape logic.
- Use `satisfies` when you need to verify object shape without losing useful inference.
- Prefer `const`, `readonly`, and immutable updates when they improve correctness and make state changes easier to reason about.
- Use descriptive names; boolean values should read as predicates such as `is`, `has`, or `can`.
- Avoid non-null assertions and unchecked type assertions unless the invariant is established nearby and obvious from the code.
- Treat optional properties and indexed access precisely; model absence explicitly instead of relying on loose object semantics.
- Use type-only imports and exports deliberately when the project tooling supports modern TypeScript module semantics.
- Use explicit `override` in inheritance-based code so base-class changes fail loudly.
- Validate and parse untrusted input explicitly at the application boundary before it flows into domain logic.
- Keep framework-specific conventions in the relevant stack fragments rather than in the shared TypeScript rules.
