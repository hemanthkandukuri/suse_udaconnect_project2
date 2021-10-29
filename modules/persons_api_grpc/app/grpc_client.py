import grpc

import app.person_pb2
import app.person_pb2_grpc

print("Requesting grpc-server...")
channel = grpc.insecure_channel("localhost:30003")
stub = person_pb2_grpc.PersonServiceStub(channel)
response = stub.Get(person_pb2.Empty())
print('---30003-------response----------\n', response)
print(response.persons_list)

print("Requesting grpc-server...")
channel = grpc.insecure_channel("localhost:5000")
stub = person_pb2_grpc.PersonServiceStub(channel)
response = stub.Get(person_pb2.Empty())
print('---5000-------response----------\n', response)
print(response.persons_list)
