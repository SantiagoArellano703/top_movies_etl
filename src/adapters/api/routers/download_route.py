from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.adapters.api.models.DownloadRequest import DownloadRequest
from src.adapters.factory.scraper_factory import ScraperFactory
from src.core.application.uses_cases.download_use_case import DownloadUseCase
from src.config.settings import OUTPUT_EXT, OUTPUT_PATH

router = APIRouter(prefix="/api", tags=["api"])


@router.post("/top-movies/export")
def download_movies(request: DownloadRequest) -> FileResponse:
    scraper = ScraperFactory.get_scraper(request.platform)
    use_case = DownloadUseCase(scraper)
    file_path = OUTPUT_PATH / f"top_movies{OUTPUT_EXT}"
    output_filepath = use_case.execute(
        limit=request.limit,
        file_path=file_path
    )
    file_name = request.output_filename + OUTPUT_EXT
    return FileResponse(
        path=output_filepath,
        filename=file_name
    )
