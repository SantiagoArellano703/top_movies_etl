from pydantic import BaseModel


class DownloadRequest(BaseModel):
    platform: str
    format: str
    limit: int = 50
