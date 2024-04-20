import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEBUG = os.environ.get("DEBUG", "True").lower() in ("true", "1")

MAX_BODY_SIZE = 124 * 1024

VIEWS = {
    "restcraft_app.views.my_view",
}

MIDDLEWARES = {}


try:
    from .my_settings import *  # type: ignore reportMissingImports  # noqa: F403
except ImportError:
    pass
