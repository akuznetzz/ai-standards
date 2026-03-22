## Architecture & Layering
- Service layers contain business logic only.
- Service layers must not use ORM directly.
- Service layers must not call external protocols such as HTTP directly.
- Database access must stay behind repository-style abstractions.
- If a change may break backward compatibility, report the risk to the user and do not choose the compatibility strategy unilaterally.

