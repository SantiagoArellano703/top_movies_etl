from abc import ABC, abstractmethod
from typing import List, Dict
from src.core.domain.entities.movie import Movie
from src.core.domain.value_objects.platform import Platform


class Transformer(ABC):
    @abstractmethod
    def transform(
        self,
        raw_movies: List[Dict],
        platform: Platform
    ) -> List[Movie]:
        pass
