
run:
	python manage.py runserver

all-migrate:
	python manage.py makemigrations carro
	python manage.py makemigrations categorias
	python manage.py makemigrations empresa
	python manage.py makemigrations paginas
	python manage.py migrate

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

install:
	poetry env use /usr/bin/python3
	poetry lock
	poetry install
	poetry run pre-commit install

pre-commits:
	poetry run pre-commit run -a
