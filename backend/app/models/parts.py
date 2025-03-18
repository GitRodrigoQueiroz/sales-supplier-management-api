import enum

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.models.base import Base


class Part(Base):
    __tablename__ = "dim_parts"

    part_id = Column(Integer, primary_key=True, autoincrement=True)
    part_name = Column(String(255), nullable=False)
    last_id_purchase = Column(
        Integer, ForeignKey("dim_purchances.purchance_id"), nullable=False
    )
    supplier_id = Column(
        Integer, ForeignKey("dim_suppliers.supplier_id"), nullable=False
    )

    supplier = relationship("Supplier")
