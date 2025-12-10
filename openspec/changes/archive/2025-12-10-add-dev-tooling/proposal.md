# Change: Add Development Tooling and Project Structure

**Linear Issue:** [ENG-1](https://linear.app/emkaytec-io/issue/ENG-1/initialize-agent-core-repository-and-tooling)

## Why

The repository needs standardized development tooling to enforce code quality from Day 1. Currently, `ruff` is not installed as a dependency, preventing linting from running. The project also lacks the intended package structure and several required dependencies specified in ENG-1.

## What Changes

- Add core dependencies to `pyproject.toml`: `langchain`, `pydantic`
- Add development dependencies: `ruff`, `black`, `pytest`
- Create package directory structure: `src/emkaytec_agent_core/`
- Configure `ruff` for linting (basic configuration)

## Impact

- Affected files: `pyproject.toml`
- New directories: `src/emkaytec_agent_core/`
- Developer workflow: All contributors can now run `ruff check .` and `pytest`

## Acceptance Criteria (from ENG-1)

- [ ] `uv sync` installs all dependencies without error
- [ ] `ruff check .` runs and passes (even if on empty files)
- [ ] `.env` files are confirmed ignored by Git

## Current State Analysis

| Criterion | Status | Notes |
|-----------|--------|-------|
| `uv sync` works | PASS | Already working |
| `ruff check .` passes | FAIL | ruff not installed |
| `.env` ignored | PASS | Already in .gitignore |
