# Eventstoreio

a grpc client for eventstore based on grpcio


## Dev notes

* initial pb2 creation:

```sh
python -m grpc_tools.protoc --proto_path=Eventstore/src/Protos/Grpc --python_out=src/eventstoreio/protobufs --grpc_python_out=src/eventstoreio/protobufs Eventstore/src/Protos/Grpc/*
python -m grpc_tools.protoc --proto_path=Eventstore/src/Protos --python_out=src/eventstoreio/protobufs --grpc_python_out=src/eventstoreio/protobufs Eventstore/src/Protos/ClientAPI/*
mv src/eventstoreio/protobufs/ClientAPI/* src/eventstoreio/protobufs
```

* fix imports

```sh
sed -i 's/^import \(.\+\) as/from . import \1 as/' src/eventstoreio/protobufs/*.py
```

