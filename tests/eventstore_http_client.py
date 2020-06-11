import json
import uuid
from dataclasses import dataclass
from typing import List
from pathlib import Path

import requests

IN_CONTAINER = Path('/src').exists()
HOST = 'eventstore' if IN_CONTAINER  else 'localhost'
HTTP_PORT = 2113 if IN_CONTAINER else 21132
TCP_PORT = 1113 if IN_CONTAINER else 11131
CERT_PATH = Path(('/' if IN_CONTAINER else '') + 'certs/dev.crt')

@dataclass
class _Event:
    stream: str
    data: dict


def publish_event(stream: str, event_type: str, data: dict):
    if not IN_CONTAINER:
        os.environ["REQUESTS_CA_BUNDLE"] = str(CERT_PATH)
    eventstore_uri = f'https://{HOST}:{HTTP_PORT}/streams/{stream}'
    headers = {
        "Content-Type": "application/json",
        "ES-EventType": event_type,
        "ES-EventId": uuid.uuid4().hex,
    }
    r = requests.post(
        eventstore_uri,
        data=json.dumps(data),
        headers=headers,
        auth=('admin', 'changeit'),
    )
    assert r.status_code == 201, f"Status: {r.status_code}\nResponse: {r.text}"


def get_events(stream: str) -> List[dict]:
    es_config = config.get_eventstore_config()
    es_uri = f'http://{es_config["host"]}:{es_config["http_port"]}/streams/{stream}?embed=body'
    r = requests.get(
        es_uri,
        headers={"Accept": "application/json"},
        timeout=0.5,
        auth=(es_config["username"], es_config["password"]),
    )
    if r.status_code == 404:
        raise ValueError("The stream {} does not exist yet.".format(stream))

    if r.status_code != 200:
        raise Exception(f"Got response {r}")

    return r.json()["entries"]


# TODO: 5 second wait was added to avoid a race of e2e test straight after
# container rebuilds. 5s is a very long time to wait for an event.  add a general
# wait_for_eventstore with scope=session
# @tenacity.retry(reraise=True, stop=stop_after_delay(5))
# def wait_for_event(stream: str, event_type: str, **kwargs) -> _Event:
#     events = get_events(stream)
#     for event in events:
#         if not event["eventType"] == event_type:
#             continue
#         data = json.loads(event["data"])
#         if all(expected_value == data.get(key) for key, expected_value in kwargs.items()):
#             return _Event(stream=event["streamId"], data=data)
#     raise Exception(f"No events matching {kwargs} in {events}")
