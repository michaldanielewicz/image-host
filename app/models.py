from pydantic import BaseModel


class ImageModel(BaseModel):
    id: int
    url: str
    title: str
    width: str
    height: str
