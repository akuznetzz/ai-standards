# UMA2 — Core Rules

## Language & Communication
- Chat with the user in Russian.
- Keep code comments, docstrings, user-facing string literals, and git commit messages in English.

## Engineering Workflow
- Verify information before stating it.
- Preserve existing behavior unless the user explicitly requests a change.
- Make minimal, focused edits and avoid unrelated cleanup.
- Do not propose whitespace-only changes.
- Do not invent changes beyond the user's request.
- Prefer single coherent patches per file.

## General Engineering Principles
- Prefer small, coherent changes.
- Keep functions small and single-purpose.
- Use meaningful names and avoid unclear abbreviations.
- Replace magic values with named constants or configuration.
- Use comments only to explain intent or non-obvious decisions.
- Refactor early when debt becomes visible.

## DRY
- Do not duplicate code.
- If duplication is detected or strongly suspected, tell the user and propose a refactoring path.

