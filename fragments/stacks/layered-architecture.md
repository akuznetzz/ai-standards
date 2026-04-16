## Layered Architecture

### Scope
- Treat layered architecture as an opt-in structural style for codebases that benefit from explicit dependency boundaries and reviewable orchestration.
- Keep the layering model small enough that engineers can explain the purpose of each layer without inventing ceremonial indirection.

### Boundaries
- Define clear layer responsibilities and keep them stable across modules that participate in the same architecture.
- Allow dependencies to point from higher-level orchestration toward lower-level implementation details, not the reverse.
- Keep cross-layer contracts explicit and reviewable; do not hide important workflow jumps behind implicit callbacks or ambient global state.
- Place side effects at the edges of the system and keep transformations and decision logic in layers that can be tested without infrastructure.
- When a concern does not fit the current layer boundaries cleanly, adjust the structure deliberately instead of smearing the same workflow across multiple layers.
