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

@pytest.fixture(scope='module')
def testling():
    testling = zookeeperd.app
    return testling

def request_test(testling):
    ### test plain invocation ###
    #assert tuple._overlaps((1, 1), (1, 1)) == True
    res = requests.get('https://localhost:5000')
    print(res)
