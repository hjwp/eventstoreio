from pathlib import Path
import grpc
from eventstoreio.protobufs.streams_pb2_grpc import StreamsStub
from eventstoreio.protobufs.streams_pb2 import ReadReq

IN_CONTAINER = Path('/src').exists()
HOST = 'eventstore' if IN_CONTAINER  else 'localhost'
TCP_PORT = '2113' if IN_CONTAINER else '21132'
UDP_PORT = '1113' if IN_CONTAINER else '11131'

def test_smoke_test():
    channel = grpc.insecure_channel(f"{HOST}:{TCP_PORT}")
    stub = StreamsStub(channel)
    request = ReadReq()
    response = stub.Read(request)
    assert list(response) == []
