from typing import List, Dict
from src.core.domain.ports.scraper_port import ScraperPort


class ExtractMoviesUseCase:
    def __init__(self, scraper: ScraperPort):
        self.scraper = scraper

    def execute(self, **kwargs) -> List[Dict]:
        data = self.scraper.extract_data(**kwargs)
        return data
