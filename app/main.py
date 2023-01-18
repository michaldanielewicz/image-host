import random
import shutil

import psycopg2
from fastapi import FastAPI, Response, UploadFile, HTTPException
from fastapi.responses import FileResponse
from PIL import Image

from app.const import ALLOWED_CONTENT_TYPES
from app.models import ImageModel

app = FastAPI()


@app.post("/images")
def post_image(file: UploadFile, image_title: str, image_width: int, image_height: int):

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Content type not allowed. Only images supported.")

    # image processing:
    # ------------------------
    # i dunno if i need to save it first but suppose it works like this

    file_extension = file.filename.split(".")[1]
    path = image_title + "." + file_extension
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    # after saving file we need to resize it

    with Image.open(path) as image_to_resize:
        image_to_resize = image_to_resize.resize((image_width, image_height))
        image_to_resize.save(path)
    # -------------------------

    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="app_db")
    cur = conn.cursor()

    image_id = random.randint(1, 1000)

    cur.execute(
        f"INSERT INTO photo (id, url, title, width, height) VALUES ('{image_id}', '{path}', '{image_title}', '{image_width}', '{image_height}')"
    )
    conn.commit()
    cur.close()
    conn.close()

    return Response(status_code=201)


@app.get("/images")
def get_images():
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="app_db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM photo ORDER BY id DESC")
    rows = cur.fetchall()

    formatted_images = []
    for row in rows:
        formatted_images.append(
            ImageModel(
                id=row[0],
                url=row[1],
                title=row[2],
                width=row[3],
                height=row[4],
            )
        )
    cur.close()
    conn.close()
    return formatted_images


@app.get("/images/{image_id}")
def get_image_by_id(image_id: int):
    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="app_db")

    cur = conn.cursor()
    cur.execute(f"SELECT id, url, title, width, height FROM photo WHERE id = {image_id}")

    image = cur.fetchone()

    cur.close()
    conn.close()

    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    image_model = ImageModel(id=str(image_id), url=image[1], title=image[2], width=image[3], height=image[4])

    return FileResponse(image[1], headers=dict(image_model))
