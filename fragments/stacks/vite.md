## Vite Stack
- Use this stack when the project is directly built and served by Vite; do not add Vite-specific rules to framework-managed stacks such as Next.js or Nuxt unless the repository truly owns Vite configuration directly.
- Access browser-exposed environment variables through `import.meta.env`, and expose only values intentionally prefixed for client use.
- Keep `vite.config.*` focused on build, dev-server, alias, and plugin wiring; do not move application logic or runtime decisions into build configuration without a clear build-time need.
- Keep path aliases consistent across Vite, TypeScript, tests, and other tooling so imports resolve the same way in every environment.
- Prefer maintained ecosystem plugins and add them deliberately; each plugin should solve a concrete build or integration need, not style preference alone.
- Prefer dynamic imports, route-level splitting, or framework lazy-loading primitives for large boundaries before reaching for manual chunk tuning.
- Treat manual chunking, advanced build output customization, and plugin statefulness as optimization work that should be justified by measurement or platform requirements.
- Keep client, SSR, and build-time code paths explicit when the project uses more than one runtime environment.
