FROM python:3.10.0-alpine

WORKDIR /code

RUN apk add --no-cache build-base 
RUN apk --no-cache add postgresql-dev

ENV VIRTUAL_ENV = /opt/venv
RUN python -m venv $VIRTUAL_ENV

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .