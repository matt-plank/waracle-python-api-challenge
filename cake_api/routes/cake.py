from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Cake(BaseModel):
    id: int
    name: str
    comment: str
    imageUrl: str
    yumFactor: int


CAKES: list[Cake] = [
    Cake(
        id=1,
        name="Chocolate Cake",
        comment="A simple chocolate cake",
        imageUrl="https://food-images.files.bbci.co.uk/food/recipes/easy_chocolate_cake_31070_16x9.jpg",
        yumFactor=5,
    )
]


@router.get("")
async def get_many():
    return CAKES
