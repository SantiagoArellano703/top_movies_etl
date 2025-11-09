from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Movie:
    title: str
    year: int
    rating: float
    platform: str
    duration_minutes: int = None
    director: str = None
    genre: List[str] = None
    extracted_at: datetime = None
    source_url: str = None

    def __post_init__(self):
        self._validate()

    def _validate(self):
        if not self.title or not self.title.strip():
            raise ValueError("The title cannot be empty")

        if not 0 <= self.rating <= 10:
            raise ValueError(f"Invalid rating: {self.rating}")

        if self.year is not None and self.year < 1888:
            raise ValueError("The year cannot be less than 1888")
