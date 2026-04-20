<!-- Source: https://github.com/HackSoftware/Django-Styleguide -->
<!-- Imported: 2026-04-16 -->
<!-- Adaptation: normalized for UMA2, preserving the HackSoft-derived opt-in service-and-selector architecture for Django projects -->

## Django Service Layer

### Scope
- This fragment is an opt-in architectural style, not a Django baseline.
- Use it when the project explicitly adopts a service-and-selector application layer across Django and DRF entry points.

### Architecture
- Keep views, API endpoints, admin actions, Celery tasks, and background jobs thin; delegate workflows to services.
- Place write operations (create, update, delete) in service functions or classes under `<app>/services.py`.
- Place reusable read operations and query building in selector functions under `<app>/selectors.py`.
- Do not put business logic in views, serializers, forms, model `save()` methods, signals, or custom managers.
- Use explicit service and selector boundaries so orchestration, validation placement, and side effects stay reviewable.
- Use the ORM through services and selectors; extract complex or reusable queries into selectors rather than inlining them in services.

### Boundaries
- Treat serializers and forms as boundary validation and mapping tools, not as the home of business rules.
- Prefer explicit orchestration over implicit signal-driven flows for project-internal behavior.

### Service Conventions
- Use keyword-only arguments for service and selector signatures and provide type annotations.
- Follow the `<entity>_<action>` naming convention for services and selectors, such as `user_create` or `order_list`.
- Call `full_clean()` on model instances before `save()` in services to trigger model-level validation.
- Move complex validation and cross-relation logic to the service layer.
- Use `django-filter` or equivalent filtering abstractions inside selectors.

### Celery & Background Tasks
- Treat Celery tasks as thin entry points: fetch data, call the appropriate service, handle retries at the task level.
- When post-commit side effects matter, dispatch them via `transaction.on_commit` to guarantee data consistency.
- Keep error handling and retry logic in the task; keep business logic in the service.

### Testing
- Organize tests by layer: `tests/services/`, `tests/selectors/`, `tests/models/`.
- Service tests should hit the database and mock only external calls and async tasks.
