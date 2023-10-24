import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI: str = os.environ.get("DATABASE_URI", "sqlite:///db.db")

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
