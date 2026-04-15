---
name: release-versioning
description: Use when the user asks to preview, save, commit, or tag a release-version change in the ai-standards repository. This skill is specific to ai-standards and enforces the local release workflow around scripts/bump_version.py, clean-worktree checks, main-only tagging, and separate commit approval.
---

# Release Versioning

Use this skill only inside the `ai-standards` repository.

## Workflow

1. Preview the next release metadata with `rtk uv run python scripts/bump_version.py`.
2. If the user specifies a target version or release date, pass them with `--version` and `--release-date`.
3. When the user wants to save release metadata, run `rtk uv run python scripts/bump_version.py save ...`.
4. Run `save` only on a clean git worktree. Do not bypass this check.
5. After `save`, verify the expected files changed and run the relevant repository checks.
6. If the user wants a commit, follow the repository git workflow: propose the exact commit message and wait for approval before committing.
7. Create a release tag only with `rtk uv run python scripts/bump_version.py tag`.
8. Run `tag` only from `main` and only when the git worktree is clean.

## Constraints

- Do not combine version saving, git commit, and tagging into one automatic step.
- Do not tag from feature branches.
- Do not create a tag when there are uncommitted changes.
- Treat `pyproject.toml` and `ai.project.toml` as coordinated release metadata for this repository.

## Expected Outputs

- Preview: current version, current release date, proposed version, proposed release date.
- Save: updated release metadata files and regenerated `AGENTS.md`.
- Tag: the created annotated tag name from `pyproject.toml`.
