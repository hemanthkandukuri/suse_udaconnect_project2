import grpc
import app.person_pb2 as person_pb2
import app.person_pb2_grpc as person_pb2_grpc
import os
# print("Requesting grpc-server...")
# channel = grpc.insecure_channel("localhost:5000")
# stub = person_pb2_grpc.PersonServiceStub(channel)
# response = stub.Get(person_pb2.Empty())
# print('---5000-------response----------\n', response)
# print(response.persons_list)

GRPC_HOST = os.environ.get("UDACONNECT_PERSONS_GRPC_SERVICE_HOST")
GRPC_PORT = os.environ.get("UDACONNECT_PERSONS_GRPC_SERVICE_PORT")
PERSONS_GRPC_URL = GRPC_HOST + ':' + GRPC_PORT

resp = person_pb2_grpc.PersonServiceStub(grpc.insecure_channel(PERSONS_GRPC_URL, options=(('grpc.enable_http_proxy', 0),))).Get(person_pb2.Empty())
print('---GRPC_HOST:GRPC_PORT-------response----------\n', resp)
