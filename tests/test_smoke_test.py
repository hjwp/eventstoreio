import grpc
from eventstoreio.protobufs.streams_pb2_grpc import StreamsStub

def test_smoke_test():
    channel = grpc.insecure_channel('localhost:92113')
    stub = StreamsStub(channel)
