import json

SPECIFICATION_FILEPATH: str = "cake_api/specification.json"


def get_spec():
    with open(SPECIFICATION_FILEPATH, "r") as f:
        contents = f.read()

    yield json.loads(contents)
