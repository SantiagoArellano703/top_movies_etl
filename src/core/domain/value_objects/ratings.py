from abc import abstractmethod


class Ratings:
    @abstractmethod
    def normalize(value: float, scale: int):
        if not 0 <= value <= scale:
            raise ValueError(f"The rating must be between 0 and {scale}")

        return (value / scale) * 10
