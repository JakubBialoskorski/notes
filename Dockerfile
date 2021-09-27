FROM docker.io/python:3.9

ENV SQLALCHEMY_CONFIG='mysql://USER:PASSWORD@DATABASE_URI/DATABASE_NAME'

ADD static /app/static
ADD templates /app/templates
ADD utils /app/utils
ADD manage.py /app
ADD Procfile /app
ADD requirements.txt /app
ADD tests.py /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD gunicorn --workers=3 --threads=3 --bind 0.0.0.0:80 manage:app