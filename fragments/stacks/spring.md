## Spring Stack
- Keep controllers thin; put business logic in services or application use cases, not controllers, repositories, or framework callbacks.
- Use constructor injection by default and avoid field injection in application code.
- Validate request, method, and configuration contracts explicitly with Bean Validation and Spring validation support.
- Standardize REST error responses through centralized exception handling and RFC 9457 `ProblemDetail` or `ErrorResponse`.
- Prefer `@ConfigurationProperties` over scattered `@Value` for structured configuration, and validate at startup.
- Define transactional boundaries explicitly at service entry points and other consistency-sensitive operations.
- Remember that `@Transactional` is proxy-based; self-invocation and thread or reactive boundary changes require explicit design.
- Prefer Spring test slices for focused verification and use broader integration tests only where wiring or infrastructure behavior matters.
- For outbound HTTP, prefer `RestClient` for synchronous integrations and `WebClient` for reactive or streaming scenarios unless constrained by an older baseline.
