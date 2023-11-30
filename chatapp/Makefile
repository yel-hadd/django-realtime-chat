# Makefile for Realtime Chat App

# Variables
PYTHON = python
PIP = pip
DJANGO_ADMIN = $(PYTHON) manage.py

# Commands
install:
	$(PIP) install -r requirements.txt

migrate:
	$(DJANGO_ADMIN) migrate

makemigrations:
	$(DJANGO_ADMIN) makemigrations

createsuperuser:
	$(DJANGO_ADMIN) createsuperuser

runserver:
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
