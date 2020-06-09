FROM python:3.8-slim-buster
RUN apt-get update && apt install -yq \
     curl

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# install our self-signed CA and tell python requests to use the system ca certs
COPY ./certs /certs
RUN cp /certs/dev.crt /usr/local/share/ca-certificates/ && update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

COPY src /src
RUN pip install -e /src
COPY tests /tests
