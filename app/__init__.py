from fastapi import FastAPI

from app.api import route

app = FastAPI(
    title="Vehicles Warranties Management API",
    description="Vehicles Warranties Management API",
    version="v.1",
)
app.include_router(route)
