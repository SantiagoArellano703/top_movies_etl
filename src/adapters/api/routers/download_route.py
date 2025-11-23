from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.adapters.api.models.DownloadRequest import DownloadRequest
from src.adapters.factory.scraper_factory import ScraperFactory
from src.core.application.uses_cases.extract_movies import ExtractMoviesUseCase
from src.core.application.uses_cases.transform_movies import TransformMoviesUseCase # NOQA
from src.core.application.transformers.movie_transformer import MovieTransformer # NOQA
from src.core.application.uses_cases.export_movies import ExportMoviesUseCase
from src.adapters.exporters.exportCSV import ExportCSV
from src.config.settings import OUTPUT_EXT, OUTPUT_PATH

router = APIRouter()


@router.post("/api/top-movies/export")
def download_movies(request: DownloadRequest) -> FileResponse:
    scraper_factory = ScraperFactory()
    scraper = scraper_factory.get_scraper(request.platform)
    extract_use_case = ExtractMoviesUseCase(scraper)
    data = extract_use_case.execute(limit=request.limit)

    transform_use_case = TransformMoviesUseCase(MovieTransformer())
    cleaned_data = transform_use_case.execute(data)

    export_use_case = ExportMoviesUseCase(ExportCSV())
    file_path = OUTPUT_PATH / f"top_movies{OUTPUT_EXT}"
    file_path_out = export_use_case.execute(cleaned_data, file_path)
    file_name = request.output_filename + OUTPUT_EXT

    return FileResponse(
        path=file_path_out,
        filename=file_name
    )
