FROM python:3.10

WORKDIR /app

COPY deployment/prod/requirements.prod.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

RUN apt-get update && \
    apt-get install -y nginx certbot python3-certbot-nginx cron && \
    rm -rf /var/lib/apt/lists/*

COPY deployment/prod/nginx.conf /etc/nginx/nginx.conf

RUN echo "0 0 * * * root sleep $((85*24*60*60)) && certbot renew --nginx && nginx -s reload" > /etc/cron.d/certbot-renew
RUN chmod 0644 /etc/cron.d/certbot-renew
RUN crontab /etc/cron.d/certbot-renew

CMD ["sh", "-c", "cron && gunicorn --bind 127.0.0.1:8001 main.wsgi:application & nginx -g 'daemon off;'"]
