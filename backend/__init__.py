from fastapi import FastAPI
from backend.app.api import route

app = FastAPI(
    title="titulo",
    description="description",
    version="v.1",
)
app.include_router(route)
