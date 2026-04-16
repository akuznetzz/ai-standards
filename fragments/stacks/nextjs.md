## Next.js Stack
- Prefer the App Router for new Next.js work unless the repository is intentionally standardized on the Pages Router.
- Treat Server Components as the default rendering boundary; add `'use client'` only for interactive UI, browser APIs, or client-only Hooks.
- Keep privileged data access, secrets, and server-only logic on the server side; do not leak them through client bundles or public environment variables.
- Prefer server-side data fetching for initial page data via async Server Components, route handlers, or other server boundaries instead of duplicating the same fetch on the client.
- Make caching and revalidation explicit for data that matters: choose static caching, per-request freshness, or timed revalidation deliberately instead of relying on accidental defaults.
- Use Server Actions for form-style mutations and UI-driven writes when they fit the App Router flow; use route handlers when you need a public HTTP contract, webhook target, or third-party consumer.
- Provide route-level `loading`, `error`, and `not-found` boundaries where asynchronous or failure behavior is user-visible.
- Use streaming, Suspense boundaries, and deferred UI work deliberately for slow or non-urgent parts of the interface.
- Keep route handlers, server actions, and server components thin enough that business logic remains testable outside framework entrypoints.
