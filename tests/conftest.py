from fastapi.testclient import TestClient
from pytest import fixture


@fixture
def client(app):
    return TestClient(app)


@fixture
def app(set_db_env_vars):
    from cake_api.app import app
    from cake_api.db import SessionLocal
    from cake_api.models import Cake

    db = SessionLocal()

    cakes: list[Cake] = [
        Cake(
            id=1,
            name="Chocolate Cake",
            comment="The best cake",
            imageUrl="https://food-images.files.bbci.co.uk/food/recipes/easy_chocolate_cake_31070_16x9.jpg",
            yumFactor=5,
        ),
        Cake(
            id=2,
            name="Lemon Drizzle",
            comment="The worst cake",
            imageUrl="https://www.cookingwithmykids.co.uk/wp-content/uploads/2019/12/lemon-drizzle-cake39-scaled.jpg",
            yumFactor=1,
        ),
    ]

    db.add_all(cakes)
    db.commit()

    yield app

    db.query(Cake).delete()
    db.commit()
    db.close()


@fixture
def set_db_env_vars(monkeypatch):
    monkeypatch.setenv("DATABASE_URI", "sqlite:///test.db")
