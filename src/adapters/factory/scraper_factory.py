import logging
from src.core.domain.ports.scraper_port import ScraperPort
from src.core.domain.value_objects.platform import Platform
from src.adapters.scrapers.tmdb_scraper import TMDBScraper

logger = logging.getLogger(__name__)


class ScraperFactory:
    scrapers = {
        Platform.TMDB: TMDBScraper,
    }

    @staticmethod
    def get_scraper(platform: Platform) -> ScraperPort:
        scraper_class = ScraperFactory.scrapers.get(platform)
        if not scraper_class:
            raise ValueError(f"Unknown scraper for: {platform.key}")
        logger.info(f"Init Scraper {scraper_class.__name__}")
        return scraper_class()
