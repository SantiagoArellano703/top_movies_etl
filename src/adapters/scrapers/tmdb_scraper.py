import requests
import logging
from bs4 import BeautifulSoup
from src.core.domain.ports.scraper_port import ScraperPort

logger = logging.getLogger(__name__)


class TMDBScraper(ScraperPort):
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0', # NOQA 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', # NOQA
            'accept-language': 'es-ES,es;q=0.9',
            'referer': 'https://www.themoviedb.org/',
        }
        self.properties = {
            'url': 'https://www.themoviedb.org/movie/top-rated'
        }

    def extract_data(self, **kwargs):
        url = self.properties.get('url')
        limit = kwargs.get('limit')
        page = 0
        movies_json = []

        while limit > 0:
            cards_data = self.get_elements_page(url, page)
            movies_extract = self.create_json_data(cards_data, limit)
            movies_json.extend(movies_extract)
            limit -= len(movies_extract)
            page += 1

        logger.info(f"Extracted {len(movies_json)} movies.")
        return movies_json

    def get_elements_page(self, url: str, page: int):
        url_request = url + "?page=" + str(page)
        response = requests.get(url=url_request, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', class_='card style_1')
        return cards

    def create_json_data(self, cards, limit: int):
        movies = []
        for card in cards:
            title = card.find('h2').text
            rating = card.find('div', class_='user_score_chart').get('data-percent', '0') # NOQA
            date = card.find('p').text
            movies.append({
                'title': title,
                'rating': rating,
                'year': date,
                'platform': 'tmdb'
            })

            limit -= 1
            if limit == 0:
                break

        return movies
