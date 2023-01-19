import os

from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):
    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    SERVER = os.environ.get("POSTGRES_SERVER")
    DB = os.environ.get("POSTGRES_DB")

    ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/gif", "image/tiff", "image/bmp", "video/webm"}
    IMAGE_STORAGE = "image_data"


@lru_cache
def get_config() -> Config:
    return Config()


config = get_config()
