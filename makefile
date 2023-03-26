migrate:
	cd ./website/ && python manage.py migrate
	# cd "website" && python manage.py migrate

makemigrations:
	cd ./website/ && python manage.py makemigrations

admin:
	cd ./website/ && python manage.py createsuperuser

run:
	cd ./website/ && python manage.py runserver

poetry:
	pip install poetry