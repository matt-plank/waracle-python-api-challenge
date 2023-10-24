from pydantic import BaseModel


class Cake(BaseModel):
    id: int
    name: str
    comment: str
    imageUrl: str
    yumFactor: int


class NewCake(BaseModel):
    name: str
    comment: str
    imageUrl: str
    yumFactor: int


CakeList = list[Cake]
