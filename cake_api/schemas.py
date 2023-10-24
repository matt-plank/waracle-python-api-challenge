from pydantic import BaseModel, Field


class Cake(BaseModel):
    id: int
    name: str = Field(max_length=30)
    comment: str = Field(max_length=200)
    imageUrl: str
    yumFactor: int


class NewCake(BaseModel):
    name: str = Field(max_length=30)
    comment: str = Field(max_length=200)
    imageUrl: str
    yumFactor: int


CakeList = list[Cake]
