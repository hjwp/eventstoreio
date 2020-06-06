from pathlib import Path
import grpc
from eventstoreio.protobufs.streams_pb2_grpc import StreamsStub
from eventstoreio.protobufs.streams_pb2 import ReadReq

IN_CONTAINER = Path('/src').exists()
HOST = 'eventstore' if IN_CONTAINER  else 'localhost'
HTTP_PORT = '2113' if IN_CONTAINER else '21132'
TCP_PORT = '1113' if IN_CONTAINER else '11131'

# debugging ssl errors
import os
os.environ["GRPC_TRACE"] = "tsi"
os.environ["GRPC_VERBOSITY"] = "DEBUG"

def test_smoke_test():
    print(f"connecting to {HOST}:{TCP_PORT}")
    credentials = grpc.ssl_channel_credentials(root_certificates=Path('server_ca.pem').read_bytes())
    options = (('grpc.ssl_target_name_override', 'eventstoredb-node'),)
    channel = grpc.secure_channel(f"{HOST}:{TCP_PORT}", credentials=credentials, options=options)
    # grpc.channel_ready_future(channel).result()
    stub = StreamsStub(channel)
    request = ReadReq()
    response = stub.Read(request)
    assert list(response) == []
