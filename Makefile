##---------- Preliminaries ----------------------------------------------------
.POSIX:     # Get reliable POSIX behaviour
.SUFFIXES:  # Clear built-in inference rules

##---------- Variables --------------------------------------------------------
PREFIX = /usr/local  # Default installation directory

##---------- Build targets ----------------------------------------------------

build: ## Run docker compose
	docker-compose up -d --build --force-recreate

migrations: ## Migrate table with alembic
	cd wg_be_exam/db/ && alembic upgrade head

run: ## Run application on port 5000
	poetry run uvicorn wg_be_exam.app:app --reload --workers 1 --log-config logger.conf --log-level debug --host 0.0.0.0 --port 5000

dev: run

test:
	poetry run pytest

coverage:
	coverage run -m pytest

coverage-report: coverage
	coverage report -m

clean:
	rm -rf `find . -name __pycache__`
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
