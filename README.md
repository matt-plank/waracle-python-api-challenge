[![Test with PyTest](https://github.com/matt-plank/waracle-python-api-challenge/actions/workflows/test.yaml/badge.svg)](https://github.com/matt-plank/waracle-python-api-challenge/actions/workflows/test.yaml)

# Python API Challenge

My solution to the "Python API Challenge" take-home assessment from Waracle.

The Open API specification, as requested, can be found [here](cake_api/specification.json).

Alternatively, the specification can be found with a request to `GET https://cakes.matthewplank.com/spec`.

For example:

```bash
$ curl https://cakes.matthewplank.com/spec
```

`cakes.matthewplank.com` is hosted with Heroku. I have added a few cakes already for your convenience.

My solution is implemented using Python's FastAPI, validating data with Pydantic, and storing persistently with SQLAlchemy (tests run against a temporary SQLite database, my deployment uses Postgres, but the API is configured to be database agnostic - as long as it's SQL based). Users can deploy locally with docker-compose for an out-of-the-box environment where environment variables and databases are configured (with Postgres), Docker for slightly more control of the database, or Python for maximum environmental control.

## Run with docker-compose (most convenient)

I would recommend using docker-compose for fastest setup time and a hands-off development experience.

Clone the repo

```bash
$ git clone https://github.com/matt-plank/waracle-python-api-challenge.git
```

Build and run

```bash
$ docker-compose up
```

## Setup and test with Docker

Clone the repo

```bash
$ git clone https://github.com/matt-plank/waracle-python-api-challenge.git
```

Build docker image

```bash
# In repo root
$ docker build -t cake_api .
```

Run server

```bash
$ docker run \
    -p 8000:8000 \
    -e DATABASE_URI=<MY-DB-URI> \  # e.g. DATABASE_URI=sqlite://db.db
    -e PORT=8000 \  # the port the API will run on locally
    cake_api
```

Or run tests

```bash
$ docker run \
    -e DATABASE_URI=sqlite://db.db \
    -it \
    cake_api \
    python -m pytest
```

## Setup with Python

Clone the repo

```bash
$ git clone https://github.com/matt-plank/waracle-python-api-challenge.git
```

Install dependencies

```bash
# In repo root
$ pip install -r requirements.txt
```

Install package

```bash
# In repo root
$ pip install .
# Or, for development:
$ pip install -e .
```

Start server

```bash
$ uvicorn cake_api.app:app \
    --host 0.0.0.0 \
    --port <PORT> \
    --reload  # For development
```

Run tests

```bash
# In repo root
$ python -m pytest
```
