from typing import Optional

from pydantic import BaseModel


class SupplierBase(BaseModel):
    supplier_name: str
    location_id: int


class SupplierCreate(SupplierBase):
    pass  # You can add additional fields if needed for creation


class Supplier(SupplierBase):
    supplier_id: int

    class Config:
        orm_mode = True
