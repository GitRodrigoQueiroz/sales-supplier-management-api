from enum import Enum

from pydantic import BaseModel


class PurchaseTypeEnum(str, Enum):
    bulk = "bulk"
    warranty = "warranty"


class Purchase(BaseModel):
    purchance_type: PurchaseTypeEnum
    purchance_date: str
    part_id: int
