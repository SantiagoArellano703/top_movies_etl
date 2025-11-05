from fastapi import APIRouter
from src.adapters.api.models.DownloadRequest import DownloadRequest
from src.adapters.factory.scraper_factory import ScraperFactory
from src.core.application.uses_cases.extract_movies import ExtractMoviesUseCase

router = APIRouter()


@router.post("/download")
def download_movies(request: DownloadRequest):
    # Crear scraper y exporter usando factories
    # scraper = ScraperFactory.create(request.platform)
    # exporter = ExporterFactory.create(request.format)

    # # Crear caso de uso
    # use_case = DownloadMoviesUseCase(scraper, exporter)

    # # Ejecutar el flujo ETL
    # file_path = use_case.execute(limit=request.limit)

    # return {"message": f"Archivo generado: {file_path}"}}
    factory = ScraperFactory()
    scraper = factory.get_scraper(request.platform)
    use_case = ExtractMoviesUseCase(scraper)
    data = use_case.execute()
    return {"message": f"Archivo generado: {data}"}
