# Makefile for managing the project
# include .env
# export

SRC_DIR := src
UV_RUN_CMD=uv run --directory $(SRC_DIR)

.PHONY: all sync run test clean

all: sync clean run

# Freeze environment to requirements.txt
freeze:
	@uv pip freeze > requirements.txt

# Set up environment and build project
sync:
	@uv sync --no-cache

# Run the app
run:
	@${UV_RUN_CMD} app.py

# Test the app
test:
	@echo "No tests available currently."
	@exit 0

# Clean environment and remove .venv
clean:
	@uv clean
	@rm -rf .venv
