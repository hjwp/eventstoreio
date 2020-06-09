import socket
from contextlib import closing
from pathlib import Path

import grpc
import pytest
import requests

from eventstoreio.protobufs.streams_pb2_grpc import StreamsStub
from eventstoreio.protobufs.streams_pb2 import ReadReq

IN_CONTAINER = Path('/src').exists()
HOST = 'eventstore' if IN_CONTAINER  else 'localhost'
HTTP_PORT = 2113 if IN_CONTAINER else 21132
TCP_PORT = 1113 if IN_CONTAINER else 11131
CERT_PATH = Path(('/' if IN_CONTAINER else '') + 'certs/dev.crt')

# debugging ssl errors
import os
os.environ["GRPC_TRACE"] = "secure_endpoint,tsi,tcp"
os.environ["GRPC_VERBOSITY"] = "DEBUG"

def test_http_port_is_open():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        assert sock.connect_ex((HOST, HTTP_PORT)) == 0

def test_tcp_port_is_open():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        assert sock.connect_ex((HOST, TCP_PORT)) == 0

def test_cert_is_valid():
    if not IN_CONTAINER:
        os.environ["REQUESTS_CA_BUNDLE"] = str(CERT_PATH)
    r = requests.get(f"https://{HOST}:{HTTP_PORT}")
    assert r.ok

def test_smoke_test():
    print(f"connecting to {HOST}:{TCP_PORT}")
    if IN_CONTAINER:
        os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "./certs/dev.crt"
    else:
        os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "/certs"


    credentials = grpc.ssl_channel_credentials(
        root_certificates=CERT_PATH.read_bytes()
    )
    if IN_CONTAINER:
        options = (('grpc.ssl_target_name_override', 'eventstore'),)
    else:
        options = (('grpc.ssl_target_name_override', 'localhost'),)

    channel = grpc.secure_channel(
        f"{HOST}:{TCP_PORT}", credentials=credentials, options=options
    )
    stub = StreamsStub(channel)
    request = ReadReq()
    response = stub.Read(request)
    assert list(response) == []
