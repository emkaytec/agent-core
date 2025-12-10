# development-tooling Specification

## Purpose
TBD - created by archiving change add-dev-tooling. Update Purpose after archive.
## Requirements
### Requirement: Development Dependencies

The project SHALL include development dependencies for code quality tooling: `ruff` for linting, `black` for formatting, and `pytest` for testing.

#### Scenario: Install development dependencies

- **WHEN** a developer runs `uv sync`
- **THEN** ruff, black, and pytest are installed and available

#### Scenario: Run linter on codebase

- **WHEN** a developer runs `ruff check .`
- **THEN** the command executes successfully (exit code 0 with no errors on compliant code)

### Requirement: Core Dependencies

The project SHALL include core AI/ML dependencies: `langchain` for LLM orchestration and `pydantic` for data validation.

#### Scenario: Core dependencies available

- **WHEN** a developer runs `uv sync`
- **THEN** langchain and pydantic are installed and importable

### Requirement: Package Structure

The project SHALL use a `src/` layout with the package directory `src/emkaytec_agent_core/`.

#### Scenario: Package directory exists

- **WHEN** the repository is cloned
- **THEN** the directory `src/emkaytec_agent_core/` exists with an `__init__.py` file

### Requirement: Security Configuration

The project SHALL prevent accidental commit of sensitive files by including `.env`, `.venv`, and common secret patterns in `.gitignore`.

#### Scenario: Environment file ignored

- **WHEN** a developer runs `git check-ignore .env`
- **THEN** the command returns `.env` (confirming the file is ignored)

