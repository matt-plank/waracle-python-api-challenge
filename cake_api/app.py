from fastapi import FastAPI

from .db import engine
from .models import Base
from .routes import cake

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(cake.router, prefix="/cake")
