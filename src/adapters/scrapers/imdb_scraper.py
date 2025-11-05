from src.core.domain.ports.scraper_port import ScraperPort


class IMDBScraper(ScraperPort):
    def extract_data(self):
        data = "Hola hice scraping!!!"
        return data
