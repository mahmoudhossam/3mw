# 3megawatt


3Megawatt technical task

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

| License  | [MIT](https://opensource.org/licenses/MIT) |
| ------------- | ------------- |

-------------------------------------------------------------

## Main stack

* [SQLite](https://sqlite.org/)
* [Python](https://python.org/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)

## Setup

To get the app up and running, run `docker-compose up` and visit `localhost:8000` to view the app

To run the tests, run `docker-compose ./manage.py test`

## Rationale

I use docker to ease development and simplify first-time setup.

SQLite is used for the sake of simplicity, in a real world application I usually use [PostgreSQL](https://www.postgresql.org/).

Summary logic is implemented in a Django model manager to ease testing and to separate application logic from view code.

I wrote tests for most of the critical functionality, those can be run in a CI to help with deployment to production.

Tests run with an in-memory instance of SQLite to speed up testing.
