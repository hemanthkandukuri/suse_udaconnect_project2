import grpc
import app.person_pb2 as person_pb2
import app.person_pb2_grpc as person_pb2_grpc

print("Requesting grpc-server...")
channel = grpc.insecure_channel("localhost:5000")
stub = person_pb2_grpc.PersonServiceStub(channel)
response = stub.Get(person_pb2.Empty())
print('---5000-------response----------\n', response)
print(response.persons_list)

person_pb2_grpc.PersonServiceStub(grpc.insecure_channel("localhost:5000", options=(('grpc.enable_http_proxy', 0),))).Get(person_pb2.Empty()).__str__