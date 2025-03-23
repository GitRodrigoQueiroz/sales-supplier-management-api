from typing import Optional

from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.models import Location, Part, Purchase, Supplier
from app.services.db_service import get_session

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"],
)


@router.get("/supplier/get_by_id/{supplier_id}")
def get_supplier_by_id(
    supplier_id: int,
    session: Session = get_session,
):
    """Get supplier details by supplier ID"""
    supplier = (
        session.query(Supplier, Location)
        .join(Location, Supplier.location_id == Location.location_id)
        .filter(Supplier.supplier_id == supplier_id)
        .first()
    )

    if not supplier:
        return {"error": "Supplier not found"}

    supplier_data, location_data = supplier

    return {
        "supplier": supplier_data,
        "location": location_data,
    }


@router.get("/supplier/get_by_location")
def get_supplier_by_filters(
    market: Optional[str] = None,
    country: Optional[str] = None,
    province: Optional[str] = None,
    city: Optional[str] = None,
    session: Session = get_session,
):
    """Get supplier details by supplier filters"""
    query = session.query(Supplier, Location).join(
        Location, Supplier.location_id == Location.location_id
    )

    if market:
        query = query.filter(Supplier.market == market)
    if country:
        query = query.filter(Location.country == country)
    if province:
        query = query.filter(Location.province == province)
    if city:
        query = query.filter(Location.city == city)

    suppliers = query.all()

    if not suppliers:
        return {"error": "Supplier not found"}

    result = []
    for supplier_data, location_data in suppliers:
        result.append({"supplier": supplier_data, "location": location_data})

    return result


@router.get("/part/get_by_id/{part_id}")
def get_part_by_id(
    part_id: int,
    session: Session = get_session,
):
    """Get part details by part ID"""
    part = (
        session.query(Part, Supplier)
        .join(Supplier, Part.supplier_id == Supplier.supplier_id)
        .filter(Part.part_id == part_id)
        .first()
    )

    if not part:
        return {"error": "Part not found"}

    part_data, supplier_data = part

    return {
        "part": part_data,
        "supplier": supplier_data,
    }


@router.get("/purchance/get_by_id/{purchance_id}")
def get_purchance_by_id(
    purchance_id: int,
    session: Session = get_session,
):
    """Get purchance details by part ID"""
    purchance = (
        session.query(Purchase, Part)
        .join(Part, Purchase.part_id == Part.part_id)
        .filter(Purchase.purchance_id == purchance_id)
        .first()
    )

    if not purchance:
        return {"error": "Purchance not found"}

    purchance_data, part_data = purchance

    return {
        "purchance": purchance_data,
        "part": part_data,
    }
