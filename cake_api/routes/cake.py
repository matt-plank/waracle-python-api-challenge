from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..db import get_db

router = APIRouter()


@router.get("", response_model=schemas.CakeList)
async def get_many(db: Session = Depends(get_db)):
    cakes = db.query(models.Cake).all()

    return cakes


@router.post("", response_model=schemas.Cake, status_code=status.HTTP_201_CREATED)
async def create(cake: schemas.NewCake, db: Session = Depends(get_db)):
    db_cake: models.Cake = models.Cake(
        name=cake.name,
        comment=cake.comment,
        imageUrl=cake.imageUrl,
        yumFactor=cake.yumFactor,
    )

    db.add(db_cake)
    db.commit()

    return db_cake


@router.put("", response_model=schemas.Cake, status_code=status.HTTP_200_OK)
async def update(cake: schemas.PartialCake, db: Session = Depends(get_db)):
    db_cake: models.Cake | None = db.query(models.Cake).filter_by(id=cake.id).first()

    if db_cake is None:
        return {"message": f"Could not find cake with ID {cake.id}"}

    if cake.name is not None:
        db_cake.name = cake.name

    if cake.comment is not None:
        db_cake.comment = cake.comment

    if cake.imageUrl is not None:
        db_cake.imageUrl = cake.imageUrl

    if cake.yumFactor is not None:
        db_cake.yumFactor = cake.yumFactor

    db.commit()

    return db_cake
