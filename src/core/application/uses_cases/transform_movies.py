from typing import List, Dict
from src.core.domain.entities.movie import Movie
from src.core.application.transformers.base_transformer import Transformer # NOQA


class TransformMoviesUseCase:
    def __init__(self, transformer: Transformer):
        self.transformer = transformer

    def execute(
            self, raw_data: List[Dict]
    ) -> List[Movie]:
        cleaned_data = self.transformer.transform(raw_data)
        return cleaned_data
