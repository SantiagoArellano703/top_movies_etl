from abc import ABC, abstractmethod
from src.core.domain.entities.movie import Movie
from typing import List


class MovieRepositoryPort(ABC):
    @abstractmethod
    def save_movie(self, movie: Movie):
        pass

    @abstractmethod
    def get_movie_by_id(self, id: int) -> Movie:
        pass

    @abstractmethod
    def update_movie(self, id: int):
        pass

    @abstractmethod
    def delete_movie(self, id: int):
        pass

    @abstractmethod
    def list_movies(self, limit: int | None = None) -> List[Movie]:
        pass
