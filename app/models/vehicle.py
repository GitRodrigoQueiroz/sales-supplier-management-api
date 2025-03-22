import enum

from sqlalchemy import Column, Date, Enum, Integer, String
from sqlalchemy.orm import relationship

from backend.app.models.base import Base


class PropulsionType(enum.Enum):
    electric = "electric"
    hybrid = "hybrid"
    gas = "gas"


class Vehicle(Base):
    __tablename__ = "dim_vehicle"

    vehicle_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    model = Column(
        String(255),
        nullable=False,
    )
    prod_date = Column(
        Date,
        nullable=False,
    )
    year = Column(
        Integer,
        nullable=False,
    )
    propulsion = Column(
        Enum(PropulsionType),
        nullable=False,
    )

    warranty = relationship(
        "Warranty",
        back_populates="vehicle",
    )
