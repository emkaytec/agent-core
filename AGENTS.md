<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# Agent Guidelines

## Build & Run
- Package manager: `uv` (uses uv.lock)
- Python version: 3.14
- Install deps: `uv sync`
- Run: `uv run python main.py`

## Code Style
- Imports: stdlib first, then third-party (grouped), one import per line
- Types: Use type hints for function parameters and return types (e.g., `def get_response(prompt: str) -> str`)
- Naming: snake_case for functions/variables, PascalCase for classes
- Strings: Double quotes preferred, f-strings for interpolation
- Constants: Module-level variables for configuration (e.g., prompt templates)

## Project Structure
- Entry point: `main.py`
- Dependencies: openai, dotenv
- Environment: Uses `.env` file for secrets (OPENAI_API_KEY)

## Error Handling
- Let exceptions propagate unless specific handling is needed
- Use OpenAI client defaults for API error handling
