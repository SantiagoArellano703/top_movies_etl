import os
from pathlib import Path


BASE_LIMIT = 50
OUTPUT_EXT = ".csv"
OUTPUT_PATH = Path(os.getenv("OUTPUT_PATH", "/data/output"))
