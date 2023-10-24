from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas
from ..db import get_db

router = APIRouter()


@router.get("", response_model=list[schemas.Cake])
async def get_many(db: Session = Depends(get_db)):
    cakes = db.query(models.Cake).all()

    return cakes


@router.post("", response_model=schemas.CakeList)
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
