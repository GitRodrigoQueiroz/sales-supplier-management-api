from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.models import Part, Purchase
from app.services.db_service import get_session

router = APIRouter(
    prefix="/analytcs",
    tags=["Analytcs"],
)


@router.get("/purchance/{purchance_id}/total_amount")
def get_purchance_by_id(
    purchance_id: int,
    session: Session = get_session,
):
    """Get total spend amount by purchance_id"""
    purchance = (
        session.query(Purchase, Part)
        .join(Part, Purchase.part_id == Part.part_id)
        .filter(Purchase.purchance_id == purchance_id)
        .first()
    )

    if not purchance:
        return {"error": "Purchance not found"}

    purchance_data, part_data = purchance

    return {"total_amount": purchance_data.units * part_data.unit_price}
