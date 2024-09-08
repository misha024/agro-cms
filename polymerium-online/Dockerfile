FROM python:3.10

WORKDIR /app

COPY deployment/prod/requirements.prod.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8002", "main.wsgi:application"]