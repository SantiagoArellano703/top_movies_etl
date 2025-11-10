from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.adapters.api.models.DownloadRequest import DownloadRequest
from src.adapters.factory.scraper_factory import ScraperFactory
from src.core.application.uses_cases.extract_movies import ExtractMoviesUseCase
from src.core.application.uses_cases.transform_movies import TransformMoviesUseCase # NOQA
from src.core.application.transformers.movie_transformer import MovieTransformer # NOQA
from src.core.application.uses_cases.export_movies import ExportMoviesUseCase
from src.core.application.exporters.exportCSV import ExportCSV

router = APIRouter()


@router.post("/download")
def download_movies(request: DownloadRequest):
    scraper_factory = ScraperFactory()
    scraper = scraper_factory.get_scraper(request.platform)
    extract_use_case = ExtractMoviesUseCase(scraper)
    data = extract_use_case.execute(limit=request.limit)

    transform_use_case = TransformMoviesUseCase(MovieTransformer())
    cleaned_data = transform_use_case.execute(data)

    export_use_case = ExportMoviesUseCase(ExportCSV())
    file_path = export_use_case.execute(cleaned_data, "top_movies.csv")
    return FileResponse(path=file_path, filename="movies.csv")
