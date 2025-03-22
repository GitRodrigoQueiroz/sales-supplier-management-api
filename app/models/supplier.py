from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Supplier(Base):
    __tablename__ = "dim_suppliers"

    supplier_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    supplier_name = Column(
        String(50),
        nullable=False,
    )
    location_id = Column(
        Integer,
        ForeignKey(
            "dim_locations.location_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    location = relationship("Location", back_populates="supplier")
    part = relationship("Part", back_populates="supplier")
