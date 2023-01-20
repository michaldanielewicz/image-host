import io
import os

from PIL import Image

from app.config import config


def create_path(image_title: str, filename: str, directory: str = config.IMAGE_STORAGE) -> str:
    _, file_extension = os.path.splitext(filename)
    path = f"{directory}/{image_title}{file_extension}"
    if os.path.exists(path):
        raise FileExistsError
    return path


def save_resized_image(content: bytes, image_width: int, image_height: int, path: str) -> None:
    with Image.open(io.BytesIO(content)) as image:
        image.resize((image_width, image_height)).save(path, optimize=True)
