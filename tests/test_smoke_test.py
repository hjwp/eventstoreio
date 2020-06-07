import socket
from contextlib import closing
from pathlib import Path

import grpc
import pytest

from eventstoreio.protobufs.streams_pb2_grpc import StreamsStub
from eventstoreio.protobufs.streams_pb2 import ReadReq

IN_CONTAINER = Path('/src').exists()
HOST = 'eventstore' if IN_CONTAINER  else 'localhost'
HTTP_PORT = 2113 if IN_CONTAINER else 21132
TCP_PORT = 1113 if IN_CONTAINER else 11131

# debugging ssl errors
import os
os.environ["GRPC_TRACE"] = "tcp,secure_endpoint,transport_security,tsi"
os.environ["GRPC_VERBOSITY"] = "DEBUG"

def test_http_port_is_open():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        assert sock.connect_ex((HOST, HTTP_PORT)) == 0

def test_tcp_port_is_open():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        assert sock.connect_ex((HOST, TCP_PORT)) == 0

def test_smoke_test():
    print(f"connecting to {HOST}:{TCP_PORT}")

    # credentials = grpc.ssl_channel_credentials()
    # credentials = grpc.ssl_channel_credentials(root_certificates=Path('server_ca.pem').read_bytes())
    credentials = grpc.ssl_channel_credentials(root_certificates=Path('server_cert.pem').read_bytes())

    # options=None
    # options = (('grpc.ssl_target_name_override', 'eventstoredb-node'),)
    options = (('grpc.ssl_target_name_override', 'localhost'),)


    channel = grpc.secure_channel(f"{HOST}:{TCP_PORT}", credentials=credentials, options=options)
    stub = StreamsStub(channel)
    request = ReadReq()
    response = stub.Read(request)
    assert list(response) == []
