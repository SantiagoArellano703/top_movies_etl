from abc import abstractmethod


class Ratings:
    @abstractmethod
    def normalize(value: float, scale: int):
        if not 0 <= value <= scale:
            raise ValueError(f"The rating must be between 0 and {scale}")

        normalized_value = (value / scale) * 10
        normalized_value = round(normalized_value, 1)
        return normalized_value
