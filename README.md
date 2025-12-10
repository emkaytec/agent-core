# Agent Core

Core libraries and tooling for EmkayTec agents. This repository provides a standardized Python environment for building AI agents using LangChain and OpenAI.

## Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) (Package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd agent-core
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Configure environment variables:
   Create a `.env` file in the root directory and add your keys (e.g., `OPENAI_API_KEY`).

## Development

This project uses modern Python tooling to ensure code quality.

### Linting & Formatting

- **Linting:** Run `uv run ruff check .` to catch errors and enforce style.
- **Formatting:** Run `uv run black .` to format your code.

### Testing

Run tests using `pytest`:

```bash
uv run pytest
```

## Project Structure

- `src/emkaytec_agent_core/`: Source code for the package.
- `main.py`: Entry point for testing/running the agent logic.
- `pyproject.toml`: Project configuration and dependencies.
