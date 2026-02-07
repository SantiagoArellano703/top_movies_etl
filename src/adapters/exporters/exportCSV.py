import pandas as pd

from src.core.domain.ports.export_port import ExportPort


class ExportCSV(ExportPort):
    def export_data(self, data, file_path, **kwargs):
        df = pd.DataFrame([movie.to_dict() for movie in data])
        df.to_csv(file_path, index=False, encoding='utf-8')
        return file_path
