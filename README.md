# Shopbridge Product module API
## About
This is a assignmnet for shopbridge product inventory API
## Features
With this API;
- You can create, view, update, and delete a product
## Technology stack
Tools used during the development of this API are;
- [Docker](https://docs.docker.com/install/) - Docker is an open platform for developing, shipping, and running applications.
- [Django](https://www.djangoproject.com) - a python web framework
- [Django REST Framework](http://www.django-rest-framework.org) - a flexible toolkit to build web APIs
- [PostgreSQL](https://www.postgresql.org/) - Postgres SQL
- [daphne](https://pypi.org/project/daphne/) - Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP 
- [nginx](https://www.nginx.com) - Nginx, stylized as NGIИX, is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
## Requirements
- docker
- docker-compose
### Todo
- [x] Data store design
- [x] API and service logic
- [x] Unit Test Coverage
- [x] Asynchronous
- [x] Pagination
- [x] JWT Authentication
- [x] Data validations
- [x] Exception handlings
- [x] Add docker configurations
- [x] Configure staticfiles
- [x] Add docker configurations
- [x] Deployment ready
#### Admin panel
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/admin` | Admin panel for Product Admin
#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/auth/register/` | Register a user
POST | `/api/token/` | Get JWT token
POST | `/api/v1/products/` | Adds a product
GET | `/api/v1/products/` | Product list
GET | `/api/v1/products/{pk}` | Product by id
PUT | `/api/v1/products/{pk}` | update by id
DELETE | `/api/v1/products/{pk}` | Delete by id
GET | `/api/v1/products/?page=2` | Products by page number

### Usage 
1. Using docker-compose.
Dockerfile and docker-compose files are configured to be production ready
Prefer to use this method

    `$ git clone https://github.com/bkalyankumar/thinkbridge_shopbridge_backend.git`
    
    `$ cd thinkbridge_shopbridge_backend`    
    `$ docker-compose up --build`

2. Without docker
 
Ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

Then, Git clone this repo to your PC

    $ git clone https://github.com/bkalyankumar/thinkbridge_shopbridge_backend.git
    $ cd thinkbridge_shopbridge_backend
Create a virtual environment

    $ python -m venv venv && source .venv/bin/activate
Install dependancies

    $ pip install -r requirements.txt
Make migrations & migrate

    $ python manage.py makemigrations && python manage.py migrate
Create Super user
    
    $ python manage.py createsuperuser

### Launching the app
    $ python manage.py runserver

### Run Tests
    $ python manage.py test