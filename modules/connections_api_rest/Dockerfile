FROM python:3.7-alpine

COPY . /connections_api_rest
WORKDIR /connections_api_rest

# RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
# COPY requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]