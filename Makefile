##---------- Preliminaries ----------------------------------------------------
.POSIX:     # Get reliable POSIX behaviour
.SUFFIXES:  # Clear built-in inference rules

##---------- Variables --------------------------------------------------------
PREFIX = /usr/local  # Default installation directory

##---------- Build targets ----------------------------------------------------

run: ## Run application on port 5000
	poetry run uvicorn wg_be_exam.app:app --reload --workers 1 --log-config logger.conf --log-level debug --port 5000

dev: run

test:
	poetry run pytest
