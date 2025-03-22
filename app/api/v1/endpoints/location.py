from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.schemas import (
    LocationCreate,
    LocationUpdate,
)
from app.services.auth_service import get_current_user
from app.services.db_service import get_session
from app.services.location import LocationUseCases

route = APIRouter(prefix="/location")


@route.post("/create")
def location_create(
    locations_create: list[LocationCreate],
    user: dict = get_current_user,
    session: Session = get_session,
):
    lc = LocationUseCases(db_session=session)
    lc.bulk_insert_locations(locations=locations_create)
    return {"message": "Locations registered successfully"}


# @route.post("/read")
# def user_register(
#     locations: list[LocationCreate],
#     user: dict = get_current_user,
#     session: Session = get_session,
# ):
#     lc = LocationUseCases(db_session=session)
#     lc.bulk_insert_locations(locations=locations)
#     return {"message": "Locations registered successfully"}


@route.post("/update")
def location_update(
    locations_update: list[LocationUpdate],
    user: dict = get_current_user,
    session: Session = get_session,
):
    lc = LocationUseCases(db_session=session)
    lc.bulk_update_locations(locations=locations_update)
    return {"message": "Location updated successfully"}


@route.post("/delete")
def location_delete(
    location_ids: list[int],
    user: dict = get_current_user,
    session: Session = get_session,
):
    lc = LocationUseCases(db_session=session)
    lc.bulk_delete_locations(location_ids=location_ids)
    return {"message": "Location deleted successfully"}
