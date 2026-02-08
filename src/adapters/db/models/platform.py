from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.adapters.db.models.base import Base


class PlatformModel(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    movies = relationship("MovieModel", back_populates="platform")
