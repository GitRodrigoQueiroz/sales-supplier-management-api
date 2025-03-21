from pydantic import BaseModel


class Location(BaseModel):
    location_id: int
    market: str
    country: str
    province: str
    city: str
