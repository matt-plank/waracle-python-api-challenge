from fastapi.testclient import TestClient


def test_get(client: TestClient):
    response = client.get("/cake")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Chocolate Cake",
            "comment": "The best cake",
            "imageUrl": "https://food-images.files.bbci.co.uk/food/recipes/easy_chocolate_cake_31070_16x9.jpg",
            "yumFactor": 5,
        },
        {
            "id": 2,
            "name": "Lemon Drizzle",
            "comment": "The worst cake",
            "imageUrl": "https://www.cookingwithmykids.co.uk/wp-content/uploads/2019/12/lemon-drizzle-cake39-scaled.jpg",
            "yumFactor": 1,
        },
    ]
