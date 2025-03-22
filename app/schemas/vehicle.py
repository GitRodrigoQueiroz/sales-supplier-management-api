from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PropulsionTypeEnum(str, Enum):
    electric = "electric"
    hybrid = "hybrid"
    gas = "gas"


class VehicleBase(BaseModel):
    model: str
    prod_date: date
    year: int
    propulsion: PropulsionTypeEnum


class VehicleCreate(VehicleBase):
    pass  # You can add additional fields if needed for creation


class Vehicle(VehicleBase):
    vehicle_id: int

    class Config:
        orm_mode = True
