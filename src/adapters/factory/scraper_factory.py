from src.adapters.scrapers.tmdb_scraper import TMDBScraper


class ScraperFactory:
    scrapers = {
        "tmdb": TMDBScraper,
        # "rottentomatoes": RottenTomatoesScraper
    }

    def get_scraper(self, platform: str):
        scraper_class = ScraperFactory.scrapers.get(platform.lower())
        if not scraper_class:
            raise ValueError(f"Unknown platform: {platform}")
        return scraper_class()
