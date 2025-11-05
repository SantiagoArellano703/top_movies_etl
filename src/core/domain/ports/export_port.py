from abc import ABC, abstractmethod
from typing import List, Dict


class ExportPort(ABC):
    @abstractmethod
    def export_data(self, data: List[Dict], filename: str) -> str:
        pass
