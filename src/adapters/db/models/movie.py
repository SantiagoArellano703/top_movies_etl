from sqlalchemy import (
    Column, Integer, String, Float, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from src.adapters.db.models.genre import movies_genres_table
from src.adapters.db.models.base import Base


class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    duration_minutes = Column(Integer)
    director = Column(String)
    extracted_at = Column(DateTime)
    source_url = Column(String)
    internal_id = Column(String)
    platform = relationship("PlatformModel", back_populates="movies")
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    genre = relationship(
        "GenreModel",
        secondary=movies_genres_table,
        back_populates="movies"
    )
