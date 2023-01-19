import tempfile

import pytest

from app.image_processing import create_path


@pytest.mark.parametrize(
    "image_title, filename, expected_path",
    [
        ("title", "image.png", f"image_data/title.png"),
        ("tricky_title", "image_jpg.jpg", f"image_data/tricky_title.jpg"),
        ("123456", "picture.gif", f"image_data/123456.gif"),
    ],
)
def test_create_path(image_title, filename, expected_path):
    assert create_path(image_title, filename, "image_data") == expected_path


def test_create_path_raises_file_exists_error():
    image_title = "test_image_title"
    filename = "image.jpg"

    with tempfile.TemporaryDirectory() as temp_dir, open(f"{temp_dir}/test_image_title.jpg", "wb") as file:
        file.write(b"data")
        with pytest.raises(FileExistsError):
            create_path(image_title, filename, temp_dir)
