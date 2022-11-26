install:
	poetry install

test:
	poetry run pytest -v --cov-report term-missing --cov-report html --cov-branch \
		--cov src/

lint:
	@echo "Running isort"
	poetry run isort .
	@echo "Running black"
	poetry run black .
	@echo "Running flake8"
	poetry run flake8 .

format:
	poetry run isort .
	poetry run black .