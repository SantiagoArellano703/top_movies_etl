import uuid
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict
from datetime import datetime


@dataclass
class Movie:
    title: str
    year: int
    rating: float
    platform: str
    duration_minutes: Optional[int] = None
    director: Optional[str] = None
    genre: Optional[List[str]] = None
    extracted_at: Optional[datetime] = None
    source_url: Optional[str] = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        self._validate()

    def _validate(self):
        if not self.title or not self.title.strip():
            raise ValueError("The title cannot be empty")

        if not 0 <= self.rating <= 10:
            raise ValueError(f"Invalid rating: {self.rating}")

        if self.year is not None and self.year < 1888:
            raise ValueError("The year cannot be less than 1888")

    def to_dict(self, include_id: bool = False) -> Dict:
        dictionary = asdict(self)
        if not include_id:
            dictionary.pop("id", None)
        return dictionary
