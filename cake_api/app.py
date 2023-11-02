from fastapi import FastAPI

from .db import engine
from .models import Base
from .routes import cake, spec

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(cake.router, prefix="/cake")
app.include_router(spec.router, prefix="/spec")
