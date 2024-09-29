# Makefile for Django application

# Установки переменных
PROJECT_NAME = main
MANAGE = python manage.py
DJANGO_SETTINGS_MODULE = $(PROJECT_NAME).settings
PYTHON = python3

.PHONY: help run migrate createsuperuser collectstatic test clean

help:
	@echo "Доступные команды:"
	@echo "  make run                 - Запуск локального сервера"
	@echo "  make migrate             - Применение миграций"
	@echo "  make createsuperuser     - Создание суперпользователя"
	@echo "  make collectstatic       - Сбор статики"
	@echo "  make test                - Запуск тестов"
	@echo "  make clean               - Очистка файлов .pyc и кешей"

# Запуск сервера на localhost:8000
run:
	$(MANAGE) runserver

# Применение миграций
migrate:
	$(MANAGE) migrate

# Создание суперпользователя
createsuperuser:
	$(MANAGE) createsuperuser

# Сбор статики
collectstatic:
	$(MANAGE) collectstatic --noinput

# Запуск тестов
test:
	$(MANAGE) test

# Очистка .pyc файлов и кешей
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

# Установка зависимостей
install:
	$(PYTHON) -m pip install -r requirements.txt

# Создание новых миграций
makemigrations:
	$(MANAGE) makemigrations
