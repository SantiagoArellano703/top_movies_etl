from fastapi import FastAPI
from fastapi.responses import Response
from src.adapters.api.routers import download_route

app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(download_route.router)


@app.get("/")
async def root():
    return Response(status_code=204)
