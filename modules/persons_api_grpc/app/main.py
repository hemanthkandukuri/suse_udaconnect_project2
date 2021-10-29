# runner file for gRPC

from concurrent import futures

import grpc
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.sql import text

import person_pb2
import person_pb2_grpc

DB_USER = os.environ["DB_USERNAME"]
DB_PASS = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def Get(self, request, context):
        print("A request came to GET Persons on GRPC")
        response = person_pb2.ListOfPersonMessages()
        print("response", response)
        engine = create_engine(
            f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
            echo=True
        )
        conn = engine.connect()
        query = text("SELECT * FROM Person")
        print("Executed the DB Query on Postgres")
        result = conn.execute(query)
        print("Result", result.__dict__)
        for person_row in result:
            print(person_row)
            person = person_pb2.PersonMessage(
                id=person_row.id,
                first_name=person_row.first_name,
                last_name=person_row.last_name,
                company_name=person_row.company_name
            )
            response.persons_list.append(person)
        print(response)
        return response

    def Create(self, request, context):
        # Not implementing Create via gRPC call for now.
        # Needs the entire DB schema and models mapping. Will do it later if additional requirements are foreseen.
        # or possibly this is not even required, because create calls can be mapped via REST endpoint
        return


# Setup the gRPC server config and run it.
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(), server)

# Setting up gRPC on 5000 port

print("Server starting on port 5000...")
server.add_insecure_port("[::]:5000")
server.start()
try:
    while True:
        # up and running for 2 days.. can
        time.sleep(172800)
except KeyboardInterrupt:
    server.stop(0)
