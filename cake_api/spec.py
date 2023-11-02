SPECIFICATION_FILEPATH: str = "cake_api/specification.yaml"


def get_spec():
    with open(SPECIFICATION_FILEPATH, "r") as f:
        yield f.read()
