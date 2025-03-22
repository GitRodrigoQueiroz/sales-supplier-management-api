from fastapi import FastAPI

from app.api import route

app = FastAPI(
    title="Sales Supplier Management API",
    description="Sales Supplier Management API",
    version="v.1",
)
app.include_router(route)
