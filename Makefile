.PHONY: help all sync freeze run test clean
.DEFAULT_GOAL := help

SRC_DIR := src
UV_RUN_CMD=uv run --directory $(SRC_DIR)

help: ## Show this help message
	@echo "Usage: make <target>"
	@echo
	@sed -n 's/^\([a-zA-Z_-]*\):.*##\(.*\)/\1:\2/p' $(MAKEFILE_LIST) | sort | awk -F: '{printf "  %-15s %s\n", $$1, $$2}'

all: clean sync run ## Run full pipeline: clean, sync, and run

sync: ## Set up environment and sync dependencies
	@uv sync --no-cache

freeze: sync ## Freeze environment to requirements.txt
	@uv pip freeze > requirements.txt

run: sync ## Run the app
	@${UV_RUN_CMD} app.py

test: sync ## Run tests
	@echo "No tests available currently."
	@exit 0

clean: ## Clean environment and remove .venv
	@uv clean
	@rm -rf .venv
