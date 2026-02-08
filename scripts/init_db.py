from src.adapters.db.connection import engine
from src.adapters.db.models.base import Base
from src.adapters.db.models.movie import MovieModel  # NOQA
from src.adapters.db.models.platform import PlatformModel  # NOQA
from src.adapters.db.models.genre import GenreModel  # NOQA

Base.metadata.create_all(bind=engine)
