from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from src.adapters.db.models.base import Base

movies_genres_table = Table(
    "movies_genres",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id")),
    Column("genre_id", Integer, ForeignKey("genres.id")),
)


class GenreModel(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    movies = relationship(
        "MovieModel",
        secondary=movies_genres_table,
        back_populates="genre"
    )
