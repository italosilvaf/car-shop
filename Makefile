
run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

install:
	poetry env use /usr/bin/python3
	poetry lock
	poetry install
	poetry run pre-commit install

pre-commits:
	poetry run pre-commit run -a