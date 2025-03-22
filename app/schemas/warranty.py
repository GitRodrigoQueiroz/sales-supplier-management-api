from datetime import date
from typing import Optional

from pydantic import BaseModel


class WarrantyBase(BaseModel):
    vehicle_id: int
    repair_date: date
    client_comment: Optional[str] = None
    tech_comment: str
    part_id: int
    classifed_failured: str
    location_id: int
    purchance_id: int


class WarrantyCreate(WarrantyBase):
    pass  # You can add additional fields if needed for creation


class Warranty(WarrantyBase):
    claim_key: int

    class Config:
        orm_mode = True
