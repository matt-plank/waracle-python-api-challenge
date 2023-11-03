from fastapi.testclient import TestClient


def test_get(client: TestClient):
    response = client.get("/spec")

    assert response.status_code == 200
    assert "info" in response.json()
