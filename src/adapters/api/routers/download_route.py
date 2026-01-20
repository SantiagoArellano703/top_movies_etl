import logging
from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi import HTTPException

from src.adapters.api.models.DownloadRequest import DownloadRequest
from src.adapters.factory.scraper_factory import ScraperFactory
from src.core.application.uses_cases.download_use_case import DownloadUseCase
from src.config.settings import OUTPUT_EXT, OUTPUT_PATH

router = APIRouter(prefix="/api", tags=["api"])
logger = logging.getLogger(__name__)


@router.post("/top-movies/download")
def download_movies(request: DownloadRequest) -> FileResponse:
    try:
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
    except ValueError as e:
        logger.warning(f"Bad request: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500)
