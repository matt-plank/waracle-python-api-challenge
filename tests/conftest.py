from fastapi.testclient import TestClient
from pytest import fixture


@fixture
def client():
    from cake_api.app import app

    return TestClient(app)
