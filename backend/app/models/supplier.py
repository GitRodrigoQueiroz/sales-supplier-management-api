import enum

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.models.base import Base


class Supplier(Base):
    __tablename__ = "dim_suppliers"

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(50), nullable=False)
    location_id = Column(
        Integer, ForeignKey("dim_locations.location_id"), nullable=False
    )

    location = relationship("Location")
