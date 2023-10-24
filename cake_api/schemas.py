from pydantic import BaseModel, Field


class Cake(BaseModel):
    id: int
    name: str = Field(max_length=30)
    comment: str = Field(max_length=200)
    imageUrl: str
    yumFactor: int


class PartialCake(BaseModel):
    id: int
    name: str | None = Field(None, max_length=30)
    comment: str | None = Field(None, max_length=200)
    imageUrl: str | None = Field(None)
    yumFactor: int | None = Field(None)


class NewCake(BaseModel):
    name: str = Field(max_length=30)
    comment: str = Field(max_length=200)
    imageUrl: str
    yumFactor: int


CakeList = list[Cake]
