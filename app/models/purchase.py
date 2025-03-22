import enum

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base


class PurchaseType(enum.Enum):
    bulk = "bulk"
    warranty = "warranty"


class Purchase(Base):
    __tablename__ = "dim_purchances"

    purchance_id = Column(Integer, primary_key=True, autoincrement=True)
    purchance_type = Column(Enum(PurchaseType), nullable=False)
    purchance_date = Column(Date, nullable=False)
    part_id = Column(
        Integer,
        ForeignKey("dim_parts.part_id", ondelete="CASCADE"),
        nullable=False,
    )

    warranty = relationship("Warranty", back_populates="purchance")

    part = relationship("Part")
