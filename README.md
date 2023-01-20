# Image Hosting API

This API allows users to upload images and host them on local file storage with a Postgres database. The API also allows users to fetch previously uploaded images.


### Stack

* Python 3.10
* FastAPI
* SQLAlchemy
* postgres

### Requirements

* Docker
* docker-compose

### Installation

1. Clone the repository

    `git clone https://github.com/michaldanielewicz/image-host`  
  

2. Change directory to the cloned repository

    `cd image-host`


3. Edit `.env.template` file

    ```
    POSTGRES_USER=*edit_this_value*
    POSTGRES_PASSWORD={{POSTGRES_PASSWORD}}
    ...
    ```


4. Rename `.env.template` to `.env`


5. Build the Docker image:

    `make build`


6. To run containers:

   `make up`


### Usage

Available endpoints:

    POST /images: Upload an image
    GET /images: Fetch all images
    GET /images/{image_id}: Fetch a specific image by ID

Upload an image by making a POST request to `http://0.0.0.0:3030/images` with the following form data:

    file: the image file to be uploaded
    image_title: the title of the image
    image_width: the width of the image
    image_height: the height of the image

Fetch all images by making a GET request to `http://0.0.0.0:3030/images`

Fetch a specific image (by id) by making a GET request to `http://0.0.0.0:3030/images/<image_id>`

You can recall all the available endpoints and documentation at http://0.0.0.0:3030/redoc or http://0.0.0.0:3030/redoc.


### Dev

You can enter the container with app by typing `make bash`

### Not implemented yet

* Tests for endpoints and crud operations undergoing in draft merge request [here](https://github.com/michaldanielewicz/image-host/pull/1).

### Tests

To run tests:
    
    make test