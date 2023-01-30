LOCAL := poetry run python3 manage.py

install:
		poetry install


start:
		$(LOCAL) runserver 8080

run-gunicorn:
		export DJANGO_SETTINGS_MODULE=task_manager.settings
		poetry run gunicorn task_manager.wsgi --log-file


# service commands
shell:
		$(LOCAL) shell_plus

collectstatic:
		$(LOCAL) collectstatic


secretkey:
		poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'

export:
# 	poetry export -f requirements.txt -o requirements.txt
	poetry export --without-hashes --format=requirements.txt > requirements.txt


# make translate messages commands
messages:
		django-admin makemessages --ignore="static" --ignore=".env"  -l ru

compilemess:
		poetry run django-admin compilemessages



# migrate commands
migrat:
		$(LOCAL) makemigrations
		$(LOCAL) migrate


migrations:
		$(LOCAL) makemigrations
migrate:
		$(LOCAL) migrate
migrate-rw:
		railway run python manage.py migrate


# test commands
#test:
#		poetry run pytest
#test-cov:
#		poetry run pytest --cov

test:
	$(LOCAL) test
# test1:
# 	$(LOCAL) test --with-coverage --cover-xml

test-cov:
	poetry run coverage run ./manage.py test
	poetry run coverage xml

# test:
# 	poetry run pytest -vv
# 	echo 'Lint checkup process...'
# 	poetry run flake8 page_loader
#
# test_cov:
# 	poetry run pytest --cov=page_loader tests/ --cov-report xml



# linter & check commands1
lint:
		poetry run flake8 task_manager users tasks labels statuses


selfcheck:
		poetry check

# complex commands
check: selfcheck test lint

build: check
		poetry build

lang_check:
		curl http://127.0.0.1:8080 -H "Accept-Language: ru"


PORT ?= 8000
db:
	python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

start1:
	python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

setup:
	poetry install
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

.PHONY: install test lint selfcheck check build shell migrate collectstatic secretkey