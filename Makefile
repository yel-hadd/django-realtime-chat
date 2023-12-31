# Makefile for Realtime Chat App

# Variables
PYTHON = venv/bin/python
PIP = venv/bin/pip
DJANGO_ADMIN = $(PYTHON) manage.py

# venv -> makemigrations

venv:
	if [ ! -d "venv" ]; then \
		python3 -m venv venv; \
		$(PIP) install -r requirements.txt; \
	fi

clean-venv:
	rm -rf venv

migrate: venv makemigrations
	$(DJANGO_ADMIN) migrate

makemigrations: venv
	$(DJANGO_ADMIN) makemigrations

admin: venv
	$(DJANGO_ADMIN) createsuperuser

runserver: venv
	$(DJANGO_ADMIN) runserver

# test:
# 	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m black chatapp/*.py
	$(PYTHON) -m black room/*.py
	$(PYTHON) -m black core/*.py

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf .pytest_cache

.PHONY: install migrate makemigrations createsuperuser runserver test lint clean
