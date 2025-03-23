from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Warranty(Base):
    __tablename__ = "fact_warranties"

    claim_key = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    vehicle_id = Column(
        Integer,
        ForeignKey(
            "dim_vehicle.vehicle_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        unique=True,
    )
    repair_date = Column(
        Date,
        nullable=False,
    )
    client_comment = Column(String)
    tech_comment = Column(
        String,
        nullable=False,
    )
    classifed_failured = Column(
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
    purchance_id = Column(
        Integer,
        ForeignKey(
            "dim_purchances.purchance_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )

    vehicle = relationship("Vehicle", back_populates="warranty")
    location = relationship("Location", back_populates="warranty")
    purchance = relationship("Purchase", back_populates="warranty")
