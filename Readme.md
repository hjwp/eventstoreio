# Eventstoreio

an attempt at a  grpc client for eventstore based on grpcio.

current status:  not even remotely working.


## Running tests

first you will need to `docker login` to be able to get the nightlies docker
image. more info at 
https://help.github.com/en/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages and
https://help.github.com/en/packages/publishing-and-managing-packages/about-github-packages#about-tokens


then:

```sh
make test
# which runs
# docker-compose build
# docker-compose run tests
```

or, to run them locally

```sh
python3.8 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e /src
pytest tests
```



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

