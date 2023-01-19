import os
import shutil

from PIL import Image
from fastapi import UploadFile


def create_path(image_title: str, filename: str) -> str:
    _, file_extension = os.path.splitext(filename)
    return f"image_data/{image_title}{file_extension}"


def store_file(file: UploadFile, path: str) -> None:
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)


def resize_image(path: str, image_width: int, image_height: int) -> None:
    with Image.open(path) as image:
        image.resize((image_width, image_height)).save(path, optimize=True)
