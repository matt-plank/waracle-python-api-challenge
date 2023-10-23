from fastapi.testclient import TestClient


def test_get(client: TestClient):
    response = client.get("/cake")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Chocolate Cake",
            "comment": "A simple chocolate cake",
            "imageURL": "https://food-images.files.bbci.co.uk/food/recipes/easy_chocolate_cake_31070_16x9.jpg",
            "yumFactor": 5,
        }
    ]
