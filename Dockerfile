FROM python:3.10.0-alpine
WORKDIR /code
RUN apk add --no-cache build-base 
RUN apk --no-cache add postgresql-dev
RUN pip install --upgrade pip
# Avoid Issue when docker-compose up / build
RUN python3 -m pip install psycopg2-binary
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
