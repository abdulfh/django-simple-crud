FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

ADD . /backend/

RUN pip install -r requirements.txt