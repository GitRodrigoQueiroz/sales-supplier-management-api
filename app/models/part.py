from sqlalchemy import Column, Double, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Part(Base):
    __tablename__ = "dim_parts"

    part_id = Column(Integer, primary_key=True, autoincrement=True)
    part_name = Column(String(255), nullable=False)
    supplier_id = Column(
        Integer,
        ForeignKey(
            "dim_suppliers.supplier_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
    )
    unit_price = Column(
        Double,
        nullable=False,
    )

    supplier = relationship("Supplier", back_populates="part")
