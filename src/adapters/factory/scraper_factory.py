from src.adapters.scrapers.imdb_scraper import IMDBScraper


class ScraperFactory:
    scrapers = {
        "imdb": IMDBScraper,
        # "rottentomatoes": RottenTomatoesScraper
    }

    def get_scraper(self, platform: str):
        scraper_class = ScraperFactory.scrapers.get(platform.lower())
        if not scraper_class:
            raise ValueError(f"Unknown platform: {platform}")
        return scraper_class()
