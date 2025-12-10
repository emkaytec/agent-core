# Tasks: Add Development Tooling

## 1. Update Dependencies

- [x] 1.1 Add core dependencies to `pyproject.toml` (`langchain`, `pydantic`)
- [x] 1.2 Add development dependencies group with `ruff`, `black`, `pytest`
- [x] 1.3 Run `uv sync` to install all dependencies

## 2. Create Package Structure

- [x] 2.1 Create `src/emkaytec_agent_core/` directory
- [x] 2.2 Add `__init__.py` to make it a proper Python package
- [x] 2.3 Update `pyproject.toml` with package configuration (if needed)

## 3. Configure Tooling

- [x] 3.1 Add basic `ruff` configuration to `pyproject.toml`
- [x] 3.2 Add basic `black` configuration to `pyproject.toml` (optional, for consistency)

## 4. Verification

- [x] 4.1 Verify `uv sync` completes without errors
- [x] 4.2 Verify `ruff check .` runs and passes
- [x] 4.3 Verify `.env` is ignored by git (`git check-ignore .env`)
