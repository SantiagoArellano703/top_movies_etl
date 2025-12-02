from abc import ABC, abstractmethod
from typing import List
from src.core.domain.entities.movie import Movie


class ExportPort(ABC):
    @abstractmethod
    def export_data(self, data: List[Movie], file_path: str, **kwargs) -> str:
        pass
