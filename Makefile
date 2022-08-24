build:
	docker-compose build

update:
	docker-compose run --rm web poetry update

install:
	docker-compose run --rm web poetry install

up:
	docker-compose up

up-build:
	docker-compose up --build

down:
	docker-compose down

test:
	make install
	docker-compose run --rm web poetry run pytest --cov=api tests

lint:
	make install
	docker-compose run --rm web poetry run flake8 tests app.py summarizer_api
	docker-compose run --rm web poetry run isort --check --diff tests app.py summarizer_api
	docker-compose run --rm web poetry run black --check tests app.py summarizer_api
	docker-compose run --rm web poetry run mypy tests app.py summarizer_api

format:
	make install
	docker-compose run --rm web poetry run isort tests app.py summarizer_api
	docker-compose run --rm web poetry run black tests app.py summarizer_api

export:
	docker-compose run --rm web poetry export -f requirements.txt --output requirements.txt