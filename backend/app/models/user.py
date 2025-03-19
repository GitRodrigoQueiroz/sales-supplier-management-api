from sqlalchemy import Column, String

from backend.app.models.base import Base


class User(Base):
    __tablename__ = "user"

    user_name = Column(
        String(50),
        nullable=False,
        primary_key=True,
    )
    password = Column(
        String(50),
        nullable=False,
    )
