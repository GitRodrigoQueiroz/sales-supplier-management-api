from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.models.base import Base


class Location(Base):
    __tablename__ = "dim_locations"
    __table_args__ = (
        UniqueConstraint(
            "market",
            "country",
            "province",
            "city",
            name="uq_market_country_province",
        ),
    )

    location_id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

    warranty = relationship("Warranty", back_populates="location")
    supplier = relationship("Supplier", back_populates="location")
