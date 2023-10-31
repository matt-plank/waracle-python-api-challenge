[![Test with PyTest](https://github.com/matt-plank/waracle-python-api-challenge/actions/workflows/test.yaml/badge.svg)](https://github.com/matt-plank/waracle-python-api-challenge/actions/workflows/test.yaml)

# Python API Challenge

My solution to the "Python API Challenge" take-home assessment from Waracle.

## Run with docker-compose (most convenient)

Clone the repo

```bash
$ git clone https://github.com/matt-plank/waracle-python-api-challenge.git
```

Build and run

```bash
$ docker-compose up
```

## Setup with Docker

Clone the repo

```bash
$ git clone https://github.com/matt-plank/waracle-python-api-challenge.git
```

Build docker image

```bash
# In repo root
$ docker build -t cake_api .
```

Run docker image

```bash
$ docker run \
    -p 8000:8000 \
    -e DATABASE_URI=<MY-DB-URI> \
    cake_api
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
