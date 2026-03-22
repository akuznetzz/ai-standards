## Python Preferences
- Use type hints for parameters and return values.
- Prefer dataclasses or typed models over loose dictionaries for structured data.
- Prefer `match` over long `if` / `elif` chains when it improves readability.
- Prefer Typer for CLI entrypoints.
- Prefer plumbum when Python code must execute OS commands.
- When project tooling exists, prefer `uv run ruff check`, `uv run mypy`, and `uv run pytest` after code changes.

