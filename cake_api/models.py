from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Cake(Base):
    __tablename__ = "cake"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    comment: Mapped[str] = mapped_column(String(200))
    imageUrl: Mapped[str]
    yumFactor: Mapped[int]
