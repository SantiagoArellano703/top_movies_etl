from sqlalchemy.orm import Session
from typing import List
from src.core.domain.ports.repository_port import MovieRepositoryPort
from src.core.domain.entities.movie import Movie


class MovieRepository(MovieRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def save_movie(self, movie: Movie, **kwargs):
        pass

    def get_movie_by_id(self, id: int, **kwargs) -> Movie:
        pass

    def update_movie(self, id: int, **kwargs):
        pass

    def delete_movie(self, id: int, **kwargs):
        pass

    def list_movies(self, **kwargs) -> List[Movie]:
        pass
