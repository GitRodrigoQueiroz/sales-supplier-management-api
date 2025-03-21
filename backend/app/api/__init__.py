from fastapi import APIRouter

from backend.app.api.v1 import token, user

route = APIRouter()

route.include_router(
    token.route,
)
route.include_router(
    user.route,
)
