# Backend

# FastAPI

## To run in local (this way if you want run the backend directly from terminal):

- create a virtualenv.
- `pip install -r requirements.txt`
- create a .env and follow the example or export all the variables. example: `export API_ENVIRONMENT=local`
- create the DB: `docker-compose up -d postgres`
- start redis: `docker-compose up -d redis`
- run migrations: `alembic upgrade head`
- run api (one of these):
  - `python app/main.py`
  - `uvicorn app.main:app --host localhost --port 8000 --reload`

## To run containers in local:

- run: `docker-compose up -d postgres`
- run: `docker compose up --build backend`

## Swagger:

- Swagger docs: `http://localhost:8000/`

## alembic

- import the model.py file in env.py inside the alembic folder, only if you create a new table or model file.
- to create a new migration: `alembic revision --autogenerate -m "create name_table"`
- run migrations: `alembic upgrade head`
- to downgrade a migration: `alembic downgrade -1`
- to downgrade all migrations: `alembic downgrade base`
  https://alembic.sqlalchemy.org/en/latest/tutorial.html

## pre-commit

A framework for managing and maintaining multi-language pre-commit hooks.
https://pre-commit.com/index.html

- install pre-commit hooks: `pre-commit install` (will run them on every commit)
- it's recommended to run all pre-commit hooks before push to avoid errors in the CI/CD pipeline.
  - `pre-commit run --all-files`

## Pytest

- run `pytest --disable-pytest-warnings`

# Logging

- use logging and use it instead print. Example: `logging.debug("debugging")`
