import logging
from src.adapters.scrapers.tmdb_scraper import TMDBScraper

logger = logging.getLogger(__name__)


class ScraperFactory:
    scrapers = {
        "tmdb": TMDBScraper,
        # "rottentomatoes": RottenTomatoesScraper
    }

    def get_scraper(self, platform: str):
        scraper_class = ScraperFactory.scrapers.get(platform.lower())
        if not scraper_class:
            raise ValueError(f"Unknown platform: {platform}")
        logger.info(f"Init Scraper {scraper_class.__name__}")
        return scraper_class()
