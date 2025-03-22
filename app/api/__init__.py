from fastapi import APIRouter

from app.api.v1 import auth, location

route = APIRouter()

route.include_router(
    auth.route,
)
route.include_router(
    location.route,
)
