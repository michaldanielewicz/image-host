from typing import Union

from sqlalchemy.orm import Session

from . import models, schemas


def get_image(db: Session, image_id: int) -> Union[models.Image, None]:
    return db.query(models.Image).filter(models.Image.id == image_id).first()


def get_all_images(db: Session):
    return db.query(models.Image).all()


def get_all_images_by_title(db: Session, image_title: str) -> Union[list[models.Image], None]:
    return db.query(models.Image).filter(models.Image.title.like(f"%{image_title}%")).all()


def create_image(db: Session, image: schemas.ImageCreate) -> models.Image:
    db_image = models.Image(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
