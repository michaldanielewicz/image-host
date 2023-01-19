from fastapi import FastAPI, Response, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.schemas import ImageCreate
from . import crud, models, schemas
from .config import config
from .database import engine, get_db
from .image_processing import create_path, store_file, resize_image


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/images", response_model=schemas.Image)
def post_image(
    file: UploadFile, image_title: str, image_width: int, image_height: int, db: Session = Depends(get_db)
) -> Response:

    if file.content_type not in config.ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Content type not allowed. Only images supported.")

    path = create_path(image_title, file.filename)
    store_file(file, path)
    resize_image(path, image_width, image_height)

    image = ImageCreate(url=path, title=image_title, width=image_width, height=image_height)
    return crud.create_image(db=db, image=image)


@app.get("/images", response_model=list[schemas.Image])
def get_images(db: Session = Depends(get_db)) -> Response:
    return crud.get_all_images(db=db)


@app.get("/images/{image_id}")
def get_image_by_id(image_id: int, db: Session = Depends(get_db)) -> FileResponse:
    db_image = crud.get_image(db, image_id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(db_image.url)
