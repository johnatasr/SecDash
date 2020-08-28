FROM python:3.6-stretch
ENV PYTHONUNBUFFERED 1

RUN sudo apt-get update
RUN sudo apt-get -y install libssl1.0

RUN apt-get install libpq-dev python-psycopg2 openssl -y

#FreeTDS
RUN apt-get autoremove freetds-dev freetds-bi
RUN apt-get install wget \
    && apt-get install libc6-dev

#Django Setup
RUN pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install psycopg2-binary
RUN pip install setuptools==45
RUN pip install django-werkzeug
RUN pip install django-extensions
RUN pip install -Ur /code/requirements.txt uwsgi gevent

WORKDIR /code
COPY . /code/

RUN python manage.py collectstatic --noinput