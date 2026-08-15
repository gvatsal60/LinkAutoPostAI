# Default target
.DEFAULT_GOAL := help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'


# Makefile for managing the project
# include .env
# export

SRC_DIR := src
UV_RUN_CMD=uv run --directory $(SRC_DIR)

.PHONY: all sync run test clean help

all: clean sync run ## Build and run the app

# Set up environment and build project
sync: ## Sync dependencies
	@uv sync --no-cache

# Freeze environment to requirements.txt
freeze: sync ## Freeze dependencies to requirements.txt
	@uv pip freeze > requirements.txt

# Run the app
run: sync ## Run the app
	@${UV_RUN_CMD} app.py

# Test the app
test: sync ## Run tests
	@echo "No tests available currently."
	@exit 0

# Clean environment and remove .venv
clean: ## Clean environment
	@uv clean
	@rm -rf .venv
