FROM python:3.7-alpine

COPY . /location_kafka_producer
WORKDIR /location_kafka_producer

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
# COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]