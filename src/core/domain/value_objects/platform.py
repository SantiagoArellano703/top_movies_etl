from enum import Enum


class Platform(Enum):

    @property
    def key(self):
        return self.value[0]

    @property
    def name(self):
        return self.value[1]

    @property
    def scale(self):
        return self.value[2]

    @classmethod
    def from_key(cls, key: str):
        for platform in cls:
            if platform.key == key:
                return platform
        raise ValueError(f"Unknown platform key: {key}")

    TMDB = ("tmdb", "The Movie Database", 100)
