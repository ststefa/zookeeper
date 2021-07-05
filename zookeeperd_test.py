#!/usr/bin/env python3

import pytest
import requests

import zookeeperd

@pytest.fixture(scope='module')
def server():
    print('*****SETUP*****')
    daemon = StudentData()
    db.connect('data.json')
    yield db
    print('******TEARDOWN******')
    db.close()

def request_test(server):
    ### test plain invocation ###
    #assert tuple._overlaps((1, 1), (1, 1)) == True
    res = requests.get('https://localhost:5000')
    print(res)
