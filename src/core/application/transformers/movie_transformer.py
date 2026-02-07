import re
from typing import List, Dict

from .transformer import Transformer
from src.core.domain.entities.movie import Movie
from src.core.domain.value_objects.ratings import Ratings
from src.core.domain.value_objects.platform import Platform
# from src.core.application.utils.ratings_values import RATINGS_VALUES

# RATING_DEFAULT = RATINGS_VALUES.get("default")
# PLATFORM_DEFAULT = "tmdb"


class MovieTransformer(Transformer):
    def transform(self, raw_movies: List[Dict], platform: Platform) -> List[Movie]: # NOQA
        movies = []

        for raw_movie in raw_movies:
            try:
                movie = self._transform_single_movie(
                    raw_movie=raw_movie,
                    platform=platform
                )
                movies.append(movie)
            except Exception as e:
                print(f"Error transforming movie: {e}")
                continue

        return movies

    def _transform_single_movie(
            self, raw_movie: Dict, platform: Platform
        ) -> Movie: # NOQA
        clean_title = self._clean_title(raw_movie.get('title', ''))
        clean_year = self._parse_year(raw_movie.get('year', ''))
        clean_rating = self._parse_rating(raw_movie.get('rating', ''))
        rating_normalized = Ratings.normalize(
            value=clean_rating,
            scale=platform.scale
        )

        return Movie(
            title=clean_title,
            year=clean_year,
            rating=rating_normalized,
            platform=platform.name
        )

    def _clean_title(self, title: str) -> str:
        if not title:
            return "Unknown Title"

        return title.strip()

    def _parse_year(self, year_str: str) -> int:
        if not year_str or not isinstance(year_str, str):
            return 0
        pattern = r"\b(19|20)\d{2}\b"
        match = re.search(pattern, year_str)
        if match:
            return int(match.group(0))

        return 0

    def _parse_rating(self, rating_str: str) -> float:
        try:
            if '/' in rating_str:
                rating_str = rating_str.split('/')[0]
            return float(rating_str)
        except Exception:
            return 0.0
