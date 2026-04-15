<!-- Source: https://github.com/HackSoftware/Django-Styleguide -->
<!-- Imported: 2026-04-10 -->
<!-- Adaptation: normalized for UMA2, extracted DRF-specific guidance as a composable fragment and softened to durable DRF baseline rules -->

## Django REST Framework
- Choose `APIView`, generic views, or viewsets based on the amount of framework behavior you actually need; prefer the least abstract option that keeps the endpoint clear.
- Keep request and response contracts explicit, especially when the input shape and output shape differ.
- Use `Serializer` or `ModelSerializer` deliberately; do not use `ModelSerializer` when it hides important validation, permissions, or contract details.
- Reuse serializers only when the contract is genuinely shared, not just similar by accident.
- Validate incoming data at the API boundary, then delegate orchestration to the project's chosen application layer.
