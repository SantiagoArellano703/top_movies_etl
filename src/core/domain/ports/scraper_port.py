from abc import ABC, abstractmethod
from typing import List, Dict


class ScraperPort(ABC):
    @abstractmethod
    def extract_data(self, **kwargs) -> List[Dict]:
        pass
