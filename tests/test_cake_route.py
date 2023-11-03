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


def test_post(client: TestClient):
    response = client.post(
        "/cake",
        json={
            "name": "Sponge",
            "comment": "Plain but unobjectionable",
            "imageUrl": "https://drivemehungry.com/wp-content/uploads/2022/04/sponge-cake-16.jpg",
            "yumFactor": 2,
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 3,
        "name": "Sponge",
        "comment": "Plain but unobjectionable",
        "imageUrl": "https://drivemehungry.com/wp-content/uploads/2022/04/sponge-cake-16.jpg",
        "yumFactor": 2,
    }


def test_post_missing_name(client: TestClient):
    response = client.post(
        "/cake",
        json={
            "comment": "Plain but unobjectionable",
            "imageUrl": "https://drivemehungry.com/wp-content/uploads/2022/04/sponge-cake-16.jpg",
            "yumFactor": 2,
        },
    )

    assert response.status_code == 422


def test_post_name_too_long(client: TestClient):
    response = client.post(
        "/cake",
        json={
            "name": "A" * 31,
            "comment": "Plain but unobjectionable",
            "imageUrl": "https://drivemehungry.com/wp-content/uploads/2022/04/sponge-cake-16.jpg",
            "yumFactor": 2,
        },
    )

    assert response.status_code == 422


def test_post_comment_too_long(client):
    response = client.post(
        "/cake",
        json={
            "name": "Simple cake name",
            "comment": "A" * 201,
            "imageUrl": "https://drivemehungry.com/wp-content/uploads/2022/04/sponge-cake-16.jpg",
            "yumFactor": 2,
        },
    )

    assert response.status_code == 422


def test_post_yum_factor_too_large(client):
    response = client.post(
        "/cake",
        json={
            "name": "Cheesecake",
            "comment": "Amazingly delicious",
            "imageUrl": "https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcSAGR_z32pqR6KX8pO021KtUDcZrzhSZW_EpLRZ5D0k1mTthOALP5hhom8Q345nHhCm",
            "yumFactor": 6,
        },
    )

    assert response.status_code == 422


def test_post_yum_factor_too_small(client):
    response = client.post(
        "/cake",
        json={
            "name": "Fruit cake",
            "comment": "Literally awful",
            "imageUrl": "https://images.immediate.co.uk/production/volatile/sites/30/2021/10/Boiled-Fruit-Cake-8b92bb5.jpg?quality=90&resize=556,505",
            "yumFactor": -1,
        },
    )

    assert response.status_code == 422


def test_put_update_commend(client):
    response = client.put(
        "/cake/1",
        json={
            "comment": "My simple comment",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Chocolate Cake",
        "comment": "My simple comment",
        "imageUrl": "https://food-images.files.bbci.co.uk/food/recipes/easy_chocolate_cake_31070_16x9.jpg",
        "yumFactor": 5,
    }


def test_put_yum_factor_too_large(client):
    response = client.put(
        "/cake/2",
        json={
            "yumFactor": 6,
        },
    )

    assert response.status_code == 422


def test_put_yum_factor_too_small(client):
    response = client.put(
        "/cake/2",
        json={
            "yumFactor": -1,
        },
    )

    assert response.status_code == 422


def test_put_name_too_long(client):
    response = client.put(
        "/cake/1",
        json={
            "name": "A" * 31,
        },
    )

    assert response.status_code == 422


def test_delete(client):
    response = client.delete("/cake/2")

    assert response.status_code == 200


def test_delete_bad_id(client):
    response = client.delete("/cake/100")

    assert response.status_code == 404


def test_post_put_delete_and_get(client):
    """Testing everything together in the same way I user might use the API."""

    client.post(
        "/cake",
        json={
            "name": "Sponge",
            "comment": "Plain but unobjectionable",
            "imageUrl": "https://drivemehungry.com/wp-content/uploads/2022/04/sponge-cake-16.jpg",
            "yumFactor": 2,
        },
    )

    client.put(
        "/cake/1",
        json={
            "name": "Double Chocolate Cake",
        },
    )

    client.delete("/cake/2")

    response = client.get("/cake")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "Double Chocolate Cake",
            "comment": "The best cake",
            "imageUrl": "https://food-images.files.bbci.co.uk/food/recipes/easy_chocolate_cake_31070_16x9.jpg",
            "yumFactor": 5,
        },
        {
            "id": 3,
            "name": "Sponge",
            "comment": "Plain but unobjectionable",
            "imageUrl": "https://drivemehungry.com/wp-content/uploads/2022/04/sponge-cake-16.jpg",
            "yumFactor": 2,
        },
    ]
