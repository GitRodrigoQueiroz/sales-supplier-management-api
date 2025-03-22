from fastapi import APIRouter

from app.api.v1 import location, token, user

route = APIRouter()

route.include_router(
    token.route,
)
route.include_router(
    user.route,
)
route.include_router(
    location.route,
)
