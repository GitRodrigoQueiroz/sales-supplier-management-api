from typing import Optional

from pydantic import BaseModel


class LocationCreate(BaseModel):
    market: str
    country: str
    province: str
    city: str


class LocationUpdateData(BaseModel):
    market: Optional[str] = None
    country: Optional[str] = None
    province: Optional[str] = None
    city: Optional[str] = None


class LocationUpdate(BaseModel):
    location_id: int
    data: LocationUpdateData
