FROM docker.io/python:3.7

ADD static /app/static
ADD templates /app/templates
ADD utils /app/utils
ADD manage.py /app
ADD Procfile /app
ADD requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD gunicorn --threads 4 --bind 0.0.0.0:80 manage:app