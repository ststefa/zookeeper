#!/usr/bin/env python3

import json
import time
import uuid
from typing import List

import flask
import pytest

import zookeeperd


@pytest.fixture
def app():
    zookeeperd.read_config()
    yield zookeeperd.app
    print("Waiting for threads to complete")


def config_test():
    """ Any element of the language must contain at least five items """
    zookeeperd.read_config()
    for item in ["animals", "verbs", "adjectives", "adverbs"]:
        assert len(zookeeperd.language[item]) > 5


def http_404_test(client):
    """ An invalid URI must result in a HTTP 404 response """
    res = client.get('nonexistingmethod')
    assert res.status_code == 404
    result = json.loads(res.data)
    for key in ["code", "name", "description"]:
        assert key in result.keys()


def animals_test(client):
    """ Must return a JSON list of animals """
    res = client.get(flask.url_for(zookeeperd.get_animals.__name__))
    assert res.status_code == 200
    result = json.loads(res.data)
    assert isinstance(result, List)
    assert len(result) > 5


def query_unknown_animal_test(client):
    """ Querying an unknown animal must result in an HTTP 500 response """
    res = client.get(
        flask.url_for(zookeeperd.start_query.__name__, animal="monsters"))
    assert res.status_code == 500
    result = json.loads(res.data)
    for key in ["code", "name", "description"]:
        assert key in result.keys()


def query_response_test(client):
    """ Querying an existing animal must return a UUID """
    res = client.get(
        flask.url_for(zookeeperd.start_query.__name__, animal="zebras"))
    assert res.status_code == 200
    result = json.loads(res.data)
    assert uuid.UUID(result)


def query_ongoing_test(client):
    """ Polling an ongoing query must result in HTTP 202 """
    res = client.get(
        flask.url_for(zookeeperd.start_query.__name__, animal="zebras"))
    assert res.status_code == 200
    id = uuid.UUID(json.loads(res.data))
    res2 = client.get(flask.url_for(zookeeperd.query_result.__name__, id=id))
    assert res2.status_code == 202
    result = json.loads(res2.data)
    assert result == "..."


def query_result_test(client):
    """ Polling a completed query must return a sentence of the language """
    res = client.get(
        flask.url_for(zookeeperd.start_query.__name__, animal="zebras"))
    id = uuid.UUID(json.loads(res.data))
    time.sleep(20)
    res2 = client.get(flask.url_for(zookeeperd.query_result.__name__, id=id))
    assert res2.status_code == 200
    result = json.loads(res2.data)
    assert isinstance(result, str)
    result_elements = result.split(" ")
    assert len(result_elements) == 4
    groups = ['adjectives', 'animals', 'verbs', 'adverbs']
    for i in range(len(groups)):
        assert result_elements[i].lower() in zookeeperd.language[groups[i]]
