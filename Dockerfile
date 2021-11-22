FROM python:3.10.0-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
