import grpc
import person_pb2
import person_pb2_grpc

print('Code block to test the grpc service, run the tests.')
channel = grpc.insecure_channel('127.0.0.1:50001')
stub = person_pb2_grpc.PersonServiceStub(channel)
res = stub.Get(person_pb2.Empty())
print(res)
