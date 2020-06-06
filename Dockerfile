FROM python:3.8-slim-buster
RUN apt-get update && apt install -yq \
    curl
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY src /src
RUN pip install -e /src
COPY tests /tests
