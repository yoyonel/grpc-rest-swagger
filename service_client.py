import grpc
from service_pb2 import StringMessage
from service_pb2_grpc import YourServiceStub


def run():
    channel = grpc.insecure_channel('localhost:50053')
    stub = YourServiceStub(channel)
    response = stub.Echo(StringMessage(value="Hello there"))
    print("Greeter client received: " + response.value)


if __name__ == '__main__':
    run()
