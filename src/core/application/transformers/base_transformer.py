from abc import ABC, abstractmethod
from typing import List, Dict
from src.core.domain.entities.movie import Movie


class Transformer(ABC):
    @abstractmethod
    def transform(
        self,
        raw_movies: List[Dict]
    ) -> List[Movie]:
        pass
