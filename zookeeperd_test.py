#!/usr/bin/env python3

import pytest
import requests

import zookeeperd

#def server():
#    print('*****SETUP*****')
#    daemon = StudentData()
#    db.connect('data.json')
#    yield db
#    print('******TEARDOWN******')
#    db.close()

@pytest.fixture #(scope='module')
def testling():
    testling = zookeeperd.app
    testling.run()
    return testling

def language_test():
    for item in ["animals", "verbs", "adjectives", "adverbs"]:
        assert item in zookeeperd.language.keys()


def config_test():
    zookeeperd.read_config()
    for item in ["animals", "verbs", "adjectives", "adverbs"]:
        assert len(zookeeperd.language[item]) > 5


def request_test(testling):
    res = requests.get('http://localhost:5000/animals')
    print(res)
