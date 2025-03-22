from pydantic import BaseModel


class Part(BaseModel):
    part_id: int
    supplier_id: int
