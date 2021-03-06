import logging
import os
from datetime import datetime, timedelta
from typing import Dict, List

from app.application import db
from app.models import Connection, Location, Person
from sqlalchemy.sql import text

import grpc
import app.person_pb2 as person_pb2
import app.person_pb2_grpc as person_pb2_grpc

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("ConnectionService-api")

GRPC_HOST = os.environ.get("UDACONNECT_PERSONS_GRPC_SERVICE_HOST")
GRPC_PORT = os.environ.get("UDACONNECT_PERSONS_GRPC_SERVICE_PORT")
PERSONS_GRPC_URL = GRPC_HOST + ':' + GRPC_PORT


class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5) -> List[Connection]:
        """
        Finds all persons who have been within a given distance of a given person_id within a date range.

        This will run rather quickly locally, but this is an expensive method and will take a bit of time to run on
        large datasets. This is by design: what are some ways or techniques to help make this data integrate more
        smoothly for a better user experience for API consumers?
        """
        locations: List = db.session.query(Location).filter(
            Location.person_id == person_id
        ).filter(Location.creation_time < end_date).filter(
            Location.creation_time >= start_date
        ).all()

        # Cache all users in memory for quick lookup
        person_map: Dict[str, Person] = {person.id: person for person in PersonService.retrieve_all()}

        # Prepare arguments for queries
        data = []
        for location in locations:
            data.append(
                {
                    "person_id": person_id,
                    "longitude": location.longitude,
                    "latitude": location.latitude,
                    "meters": meters,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": (end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
                }
            )

        query = text(
            """
        SELECT  person_id, id, ST_X(coordinate), ST_Y(coordinate), creation_time
        FROM    location
        WHERE   ST_DWithin(coordinate::geography,ST_SetSRID(ST_MakePoint(:latitude,:longitude),4326)::geography, :meters)
        AND     person_id != :person_id
        AND     TO_DATE(:start_date, 'YYYY-MM-DD') <= creation_time
        AND     TO_DATE(:end_date, 'YYYY-MM-DD') > creation_time;
        """
        )
        result: List[Connection] = []
        for line in tuple(data):
            for (
                    exposed_person_id,
                    location_id,
                    exposed_lat,
                    exposed_long,
                    exposed_time,
            ) in db.engine.execute(query, **line):
                location = Location(
                    id=location_id,
                    person_id=exposed_person_id,
                    creation_time=exposed_time,
                )
                location.set_wkt_with_coords(exposed_lat, exposed_long)

                result.append(
                    Connection(
                        person=person_map[exposed_person_id], location=location,
                    )
                )

        return result


class PersonService:
    @staticmethod
    def retrieve_all() -> List[Person]:
        persons_array = []
        print('PERSONS_GRPC_URL --------->', PERSONS_GRPC_URL)
        channel = grpc.insecure_channel(PERSONS_GRPC_URL)
        stub = person_pb2_grpc.PersonServiceStub(channel)
        response = stub.Get(person_pb2.Empty())

        for _person in response.persons_list:
            person_current = Person()
            person_current.id = _person.id
            person_current.first_name = _person.first_name
            person_current.last_name = _person.last_name
            person_current.company_name = _person.company_name
            persons_array.append(person_current)

        return persons_array
