from fastapi import APIRouter

from app.api.v1 import analytcs, auth, crud, metadata

route = APIRouter(prefix="/v1")

route.include_router(
    auth.route,
)
route.include_router(
    crud.router,
)
route.include_router(
    metadata.router,
)
route.include_router(
    analytcs.router,
)
