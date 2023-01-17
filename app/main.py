from fastapi import FastAPI, Response

app = FastAPI()


@app.post("/images")
def post_image() -> Response:
    return Response(status_code=200)


@app.get("/images")
def get_images() -> Response:
    return Response(status_code=200)


@app.get("/images/{image_id}")
def get_image_id(image_id: int) -> Response:
    return Response(status_code=200)
