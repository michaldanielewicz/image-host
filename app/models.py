from pydantic import BaseModel


class ImageModel(BaseModel):
    id: str
    url: str
    title: str
    width: str
    height: str
