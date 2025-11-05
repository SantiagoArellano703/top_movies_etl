from fastapi import FastAPI
from src.adapters.api.routers import download_route

app = FastAPI()
app.include_router(download_route.router)
