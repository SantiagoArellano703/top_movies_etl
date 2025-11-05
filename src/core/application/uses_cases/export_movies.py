from typing import List, Dict
from src.core.domain.ports.export_port import ExportPort


class ExportMoviesUseCase:
    def __init__(self, exporter: ExportPort):
        self.exporter = exporter

    def execute(self, data: List[Dict], filename: str):
        return self.exporter.export_data(data, filename)
