<!-- Source: https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules-new/vue.mdc -->
<!-- Imported: 2026-03-22 -->
<!-- Adaptation: normalized for UMA2, deduplicated, and reduced to durable Vue stack guidance -->

## Vue Stack
- Prefer the Composition API for new Vue components unless the repository already standardizes on another pattern.
- When using Single-File Components with the Composition API, prefer `<script setup>` as the default authoring style.
- Keep components small and focused, with minimal template logic; move derived view state into `computed` and reusable logic into composables.
- Prefer `computed` for derived state and `watch` or `watchEffect` for side effects or external synchronization, not as the default data-flow mechanism.
- Use explicit TypeScript types for props, emits, composables, and store contracts.
- Keep component contracts explicit with detailed prop definitions, one-way data flow, and keyed `v-for` lists.
- Move reusable stateful logic into composables instead of duplicating it across components.
- Design composables with clear inputs and outputs: accept refs or getters when reactivity matters, and return a plain object of refs by default.
- Keep composable side effects SSR-safe by deferring DOM-only work to mount-time hooks and cleaning up listeners, timers, and subscriptions on unmount.
- Keep state management modular and explicit; prefer Pinia when the project uses a central store.
- Keep routing concerns in Vue Router boundaries and treat guards as application flow control, not business logic.
- Handle forms with explicit validation, loading states, and actionable error paths.
- Use lazy loading and code splitting deliberately for route-level and other large UI boundaries.
- Treat UI performance deliberately: keep props stable, avoid unnecessary component abstractions in hot paths, and virtualize very large lists when needed.
- Prefer Vite-based tooling when the project does not already use a different supported build system.
- Cover components, composables, and async UI behavior with focused tests.
