<!-- Source: https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules-new/vue.mdc -->
<!-- Imported: 2026-03-22 -->
<!-- Adaptation: normalized for UMA2, deduplicated, and reduced to durable Vue stack guidance -->

## Vue Stack
- Prefer the Composition API for new Vue components unless the repository already standardizes on another pattern.
- Keep components small and focused, with minimal template logic.
- Use explicit TypeScript types for props, emits, composables, and store contracts.
- Move reusable stateful logic into composables instead of duplicating it across components.
- Keep state management modular and explicit; prefer Pinia when the project uses a central store.
- Keep routing concerns in Vue Router boundaries and treat guards as application flow control, not business logic.
- Handle forms with explicit validation, loading states, and actionable error paths.
- Use lazy loading and code splitting deliberately for larger routes and components.
- Prefer Vite-based tooling when the project does not already use a different supported build system.
- Cover components, composables, and async UI behavior with focused tests.
