from typing import List, Dict
from src.core.domain.ports.scraper_port import ScraperPort


class ExtractMoviesUseCase:
    def __init__(self, scraper: ScraperPort):
        self.scraper = scraper

    def execute(self) -> List[Dict]:
        return self.scraper.extract_data()
