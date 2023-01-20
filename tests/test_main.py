from fastapi.responses import FileResponse
from fastapi import UploadFile


def test_post_image(test_client):
    file = UploadFile(filename="test.jpg")

    response = test_client.post(
        "/images", data={"file": file, "image_title": "test", "image_width": 100, "image_height": 100}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "test"
    assert response.json()["width"] == 100
    assert response.json()["height"] == 100
    assert response.json()["id"] is not None


def test_post_image_unsupported_content_type(test_client):
    file = UploadFile(filename="test.txt")

    response = test_client.post(
        "/images", data={"file": file, "image_title": "test", "image_width": 100, "image_height": 100}
    )

    assert response.status_code == 415
    assert response.json()["detail"] == "Content type not allowed. Only images supported."


def test_get_images(test_client):
    response = test_client.get("/images")

    assert response.status_code == 200
    assert "results" in response.json()
    assert "total_results" in response.json()
    assert "total_pages" in response.json()


def test_get_image_by_id(test_client):
    response = test_client.get("/images/1")

    assert response.status_code == 200
    assert isinstance(response, FileResponse)


def test_get_image_by_id_not_found(test_client):
    response = test_client.get("/images/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Image not found"
