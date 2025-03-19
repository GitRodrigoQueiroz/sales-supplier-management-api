from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.models.base import Base


class Part(Base):
    __tablename__ = "dim_parts"

    part_id = Column(Integer, primary_key=True, autoincrement=True)
    part_name = Column(String(255), nullable=False)
    supplier_id = Column(
        Integer,
        ForeignKey("dim_suppliers.supplier_id", ondelete="CASCADE"),
        nullable=False,
    )

    suppliers = relationship("Supplier", back_populates="parts")

    warranties = relationship(
        "Warranty",
        back_populates="part",
    )
