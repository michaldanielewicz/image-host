build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

lint:
	poetry run black .
	poetry run flake8 .
	poetry run isort .
	poetry run mypy .
