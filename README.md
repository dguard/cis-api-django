<p align="center">
  <a href="https://www.djangoproject.com/" target="blank"><img src="https://www.django-rest-framework.org/img/logo.png" width="320" alt="Django Logo" /></a>
</p>

# CIS API Django
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django (3.0)
- Django REST Framework


| Service | Repo |
| --- | --- |
| Frontend Angular 📦 | [cis-front-angular](https://github.com/dguard/cis-front-angular) |
| API 🐍| cis-api-django (you are inside) |



## Captures
<p align="center">
  <img src="/captures/postman-api-v1.png" alt="screenshot" />
</p>


## Installation
```
    virtualenv -p python3 venv
    source venv/bin/activate

    pip install -r requirements.txt

    # update files inside static directory
    python manage.py collectstatic

    # apply migrations
    python manage.py migrate
```

## Running
```
    # rest api
    ./run-api.sh

    # worker update valutes
    ./run-update-valutes.sh

    # worker webhooks
    ./run-webhooks-celery.sh

    # websocket server
    ./run-websocket-server.sh

    # worker websocket notification clients
    ./run-notify-websocket-clients.sh
```


#### Valutes

Endpoint | CRUD Method | Result

`valutes` | GET | Get all valutes

`valutes/:id` | GET | Get a single valute


#### Webhooks

Endpoint | CRUD Method | Result

`webhooks` | GET | Get all webhooks

`webhooks/:id` | GET | Get a single webhook

`webhooks`| POST | Create a new webhook

`webhooks/:id` | PUT | Update a webhook

`webhooks/:id` | DELETE | Delete a webhook

#### Websocket
`ws://${WEBSOCKET_HOST}:8765/` | Connect to websocket


#### Graphql
`graphql` | Initialize Graphql interface
