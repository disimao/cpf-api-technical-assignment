# cpf-api

## Setup

### Docker

    $ docker-compose -f dev-ops/docker-compose-dev.yaml build

    $ docker-compose -f dev-ops/docker-compose-dev.yaml up

### Python

    $ python3.10 -m venv .venv

    $ source .venv/bin/activate
    
    $ pip install -U pip

    $ pip install -r requirements.txt 

    $ python manage.py migrate

    $ python manage.py runserver

### Tests

    $ python manage.py test

## Specs

### Validators

Validator is based on [https://www.macoratti.net/alg_cpf.htm#:~:text=O](https://www.macoratti.net/alg_cpf.htm#:~:text=O)
  * [apps/customer/api/v1/validators.py](apps/customer/api/v1/validators.py#L17)

## API

* List endpoint (GET): [http://127.0.0.1:8000/api/v1/customers/](http://127.0.0.1:8000/api/v1/customers/)
  * Pagination: [backend/settings.py](backend/settings.py#L128)
* Create endpoint (POST): [http://127.0.0.1:8000/api/v1/customers/](http://127.0.0.1:8000/api/v1/customers/)
  * Status Code: [422](apps/customer/api/v1/views.py#L23)
* Search endpoint (GET): [http://127.0.0.1:8000/api/v1/customers/?search=111.444.777.35](http://127.0.0.1:8000/api/v1/customers/?search=111.444.777.35)

## ToDo

* Deal with LGPD (GDPR) since it is something that deals with sensitive data
* Change database
