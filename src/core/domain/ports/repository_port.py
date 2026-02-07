from abc import ABC, abstractmethod
from src.core.domain.entities.movie import Movie
from typing import List


class MovieRepositoryPort(ABC):
    @abstractmethod
    def save_movie(self, movie: Movie, **kwargs):
        pass

    @abstractmethod
    def get_movie_by_id(self, id: int, **kwargs) -> Movie:
        pass

    @abstractmethod
    def update_movie(self, id: int, **kwargs):
        pass

    @abstractmethod
    def delete_movie(self, id: int, **kwargs):
        pass

    @abstractmethod
    def list_movies(self, **kwargs) -> List[Movie]:
        pass
