## Feature-Sliced Design Stack
- Treat Feature-Sliced Design as an opt-in architecture style for medium or large frontends; do not force the full layer model onto very small applications.
- Keep the layer hierarchy explicit and stable: higher layers may depend on lower layers, but not the reverse.
- Respect slice isolation: modules inside one slice must not reach into another slice's internals on the same layer.
- Expose a deliberate public API for each slice or shared segment, and import through that public API instead of deep internal paths.
- Name slices and shared segments by domain purpose and role, not by generic technical buckets such as `components`, `hooks`, or `utils`.
- Keep `shared` for truly application-agnostic foundations and cross-cutting utilities; do not turn it into a dumping ground for undecomposed feature code.
- Place business entities in `entities`, user-facing capabilities in `features`, composed UI blocks in `widgets`, route-level screens in `pages`, and app wiring in `app`.
- Introduce a slice only when it has clear ownership, cohesive responsibility, and a stable reason to change; avoid ceremonial over-splitting.
- Keep framework entrypoints thin and push reusable domain, model, and integration logic into the slice structure rather than into page or component files.
