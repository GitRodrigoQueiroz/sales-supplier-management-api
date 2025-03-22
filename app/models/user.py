from sqlalchemy import Column, Integer, String

from app.models.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_name = Column(
        String(50),
        nullable=False,
        unique=True,
    )
    password = Column(
        String(200),
        nullable=False,
    )
