from pydantic import BaseModel
from src.config.settings import BASE_LIMIT


class DownloadRequest(BaseModel):
    platform: str
    output_filename: str = "top_movies"
    limit: int = BASE_LIMIT
