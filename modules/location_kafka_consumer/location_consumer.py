import json
import os

from kafka import KafkaConsumer
from sqlalchemy import create_engine

DB_USER = os.environ["DB_USERNAME"]
DB_PASS = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_URL])


def save_in_db(location_json):
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        echo=True
    )
    conn = engine.connect()
    person_id = int(location_json["person_id"])
    latitude = int(location_json["latitude"])
    longitude = int(location_json["longitude"])

    insert_query = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" .format(
        person_id, latitude, longitude
    )
    print(insert_query)
    conn.execute(insert_query)


while True:
    raw_messages = consumer.poll(timeout_ms=1000, max_records=5000)
    for topic_partition, messages in raw_messages.items():
        location_message_as_json = json.loads(messages.value.decode())
        save_in_db(location_message_as_json)
# referred the while loop block from, https://blog.datasyndrome.com/a-tale-of-two-kafka-clients-c613efab49df
