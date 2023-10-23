[![Test with PyTest](https://github.com/matt-plank/waracle-python-api-challenge/actions/workflows/test.yaml/badge.svg)](https://github.com/matt-plank/waracle-python-api-challenge/actions/workflows/test.yaml)

# Python API Challenge

My solution to the "Python API Challenge" take-home assessment from Waracle.

## Setup (for use)

Clone the repo

```bash
$ git clone https://github.com/matt-plank/waracle-python-api-challenge.git
```

Install package

```bash
# In repo root
$ pip install .
```

Start server

```bash
$ uvicorn cake_api.app:app --host 0.0.0.0 --port <PORT>
```

## Setup (for development and testing)

Clone the repo

```bash
$ git clone https://github.com/matt-plank/waracle-python-api-challenge.git
```

Install dev dependencies

```bash
# In repo root
$ pip install -r requirements.txt
```

Install package (in editable mode)

```bash
# In repo root
$ pip install -e .
```

Start server (auto reload)

```bash
$ uvicorn cake_api.app:app \
    --host 0.0.0.0 \
    --port <PORT> \
    --reload
```

Run tests

```bash
# In repo root
$ python -m pytest
```
