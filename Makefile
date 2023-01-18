build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

bash:
	docker exec -it fastapi_app bash

test:
	pytest .

lint:
	poetry run black .
	poetry run flake8 .
	poetry run isort .
	poetry run mypy .
