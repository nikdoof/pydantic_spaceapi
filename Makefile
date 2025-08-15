.PHONY: tests
tests:
	uv run --dev --group github pytest

lint:
	uv run --dev ruff check --output-format=github --select=E9,F63,F7,F82 .
	uv run --dev ruff check --output-format=github .

build:
	uv build