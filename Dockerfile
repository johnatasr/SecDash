FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -U pip
RUN pip install -Ur requirements.txt

RUN python /code/manage.py collectstatic --noinput