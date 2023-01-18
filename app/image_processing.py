import shutil

from PIL import Image
from fastapi import UploadFile


def find_path(image_title: str, filename: str) -> str:
    file_extension = filename.split(".")[1]
    return "image_data/" + image_title + "." + file_extension


def store_image(file: UploadFile, path: str, image_width: int, image_height: int) -> None:
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    with Image.open(path) as image_to_resize:
        resized_image = image_to_resize.resize((image_width, image_height))
        resized_image.save(path)
