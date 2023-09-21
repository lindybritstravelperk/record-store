# Record Store

## Project Overview

This project creates a simple artist API and the tracks associated with the artist. The following has to be enabled by the API:

* Creating an artist, with or without tracks.
* Querying all the artists and seeing their information (`first_name`, `last_name`) and tracks. An optional name filter can be added to the query.
* Querying a single artist and seeing their information (`first_name`, `last_name`) and tracks.
* Updating an artist's information (`first_name`, `last_name`).
* Updating an artist's tracks by replacement.
* Deleting an artist.

## Running the Project

* Make sure that you start Docker locally.
* Run `docker-compose up`.
* View the API endpoints on `http://localhost:8000/`

## Accessing the Admin

* To create a superuser, run the command `docker-compose exec app python manage.py createsuperuser`
(assuming that the services are already running with `docker-compose`).
* Fill out the username, email, and password fields.
* Navigate to `http://localhost:8000/admin/` and log in with the superuser credentials.

## Migrations

* Create migrations by running `docker-compose exec app python manage.py makemigrations`.
* Apply migrations by running `docker-compose exec app python manage.py migrate`.

## Testing

* To run the tests, run `docker-compose exec app pytest`.
* To see all the details of the tests, run `docker-compose exec app pytest -vv`.


