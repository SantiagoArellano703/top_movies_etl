import logging
from src.core.domain.ports.export_port import ExportPort
from src.core.domain.ports.scraper_port import ScraperPort
from src.core.application.transformers.transformer import Transformer # NOQA
from src.core.application.transformers.movie_transformer import MovieTransformer # NOQA
from src.adapters.exporters.exportCSV import ExportCSV

logger = logging.getLogger(__name__)


class DownloadUseCase:
    MIN_LIMIT = 1
    MAX_LIMIT = 1000

    def __init__(
        self,
        scraper: ScraperPort,
        transformer: Transformer = MovieTransformer(),
        exporter: ExportPort = ExportCSV()
    ):
        self.scraper = scraper
        self.transformer = transformer
        self.exporter = exporter

    def execute(self, limit: int, file_path: str):
        self.validate_limit(limit)
        raw_movies = self.scraper.extract_data(limit=limit)
        logger.info(f"Extracted {len(raw_movies)} movies")
        cleaned_data = self.transformer.transform(raw_movies)
        logger.info("Transformed data, ready to export")
        output_filepath = self.exporter.export_data(cleaned_data, file_path)
        logger.info(f"Exported data to {file_path}")
        return output_filepath

    def validate_limit(self, limit):
        if limit < self.MIN_LIMIT:
            raise ValueError(f"Limit must be at least {self.MIN_LIMIT}, got {limit}") # NOQA
        if limit > self.MAX_LIMIT:
            raise ValueError(f"Limit must be at most {self.MAX_LIMIT}, got {limit}") # NOQA
