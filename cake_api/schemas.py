from pydantic import BaseModel, Field


class Cake(BaseModel):
    id: int
    name: str = Field(max_length=30)
    comment: str = Field(max_length=200)
    imageUrl: str
    yumFactor: int = Field(ge=1, le=5)


class PartialCake(BaseModel):
    name: str | None = Field(None, max_length=30)
    comment: str | None = Field(None, max_length=200)
    imageUrl: str | None = Field(None)
    yumFactor: int | None = Field(None, ge=1, le=5)


class NewCake(BaseModel):
    name: str = Field(max_length=30)
    comment: str = Field(max_length=200)
    imageUrl: str
    yumFactor: int = Field(ge=1, le=5)


CakeList = list[Cake]
