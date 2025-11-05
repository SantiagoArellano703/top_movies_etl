from abc import ABC, abstractmethod


class ScraperPort(ABC):
    @abstractmethod
    def extract_data(self):
        pass
