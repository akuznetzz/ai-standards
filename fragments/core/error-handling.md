## Error Handling
- Functions must either return a valid result or raise an exception with actionable context.
- Never swallow exceptions.
- Never return `None`, empty collections, or magic values to hide an error.
- Use exception chaining when translating low-level failures.
- Use `Optional[T]` only for legitimate absence of a value, not for error signaling.

