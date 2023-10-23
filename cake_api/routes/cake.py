from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


CAKES: list[dict] = [
    {
        "id": 1,
        "name": "Chocolate Cake",
        "comment": "A simple chocolate cake",
        "imageURL": "https://food-images.files.bbci.co.uk/food/recipes/easy_chocolate_cake_31070_16x9.jpg",
        "yumFactor": 5,
    }
]


@router.get("")
async def get_many():
    return JSONResponse(
        status_code=200,
        content=CAKES,
    )
