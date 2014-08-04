env_create:
	virtualenv -p python2.7 .venv

env_install:
	pip install -r requirements.txt

# `make env`
env:
	@echo source .venv/bin/activate

clean_pyc:
	find . -name "*.pyc" -delete

run:
	cd app; python ../manage.py runserver
