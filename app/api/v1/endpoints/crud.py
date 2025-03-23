from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.schemas import (
    LocationCreate,
    LocationUpdate,
)
from app.services.auth import check_token_exp, get_payload
from app.services.db_service import get_session
from app.services.location import LocationUseCases

router = APIRouter(prefix="/crud", tags=["CRUD's"])


@router.post("/location/create")
def location_create(
    locations_create: list[LocationCreate],
    payload: dict = get_payload,
    session: Session = get_session,
):
    check_token_exp(payload.get("exp"))
    lc = LocationUseCases(db_session=session)
    lc.bulk_insert_locations(locations=locations_create)
    return {"message": "Location created successfully"}


@router.post("/location/update")
def location_update(
    locations_update: list[LocationUpdate],
    payload: dict = get_payload,
    session: Session = get_session,
):
    check_token_exp(payload.get("exp"))
    lc = LocationUseCases(db_session=session)
    lc.bulk_update_locations(locations=locations_update)
    return {"message": "Location updated successfully"}


@router.post("/location/delete")
def location_delete(
    location_ids: list[int],
    payload: dict = get_payload,
    session: Session = get_session,
):
    check_token_exp(payload.get("exp"))
    lc = LocationUseCases(db_session=session)
    lc.bulk_delete_locations(location_ids=location_ids)
    return {"message": "Location deleted successfully"}
