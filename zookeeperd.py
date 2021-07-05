#!/usr/bin/env python3

import configparser

import threading
import uuid
import time
import random

from typing import Dict

from flask import Flask, escape, request

import logging
# Simplistic logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Where we keep our threads. A real world implementation would probably use a
# more sophisticated approach
threads = Dict[uuid.UUID, threading.Thread]

language = {
    'animals': [],
    'verbs': [],
    'adjectives': [],
    'adverbs': [],
}


def read_config():
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('zookeeper.conf')
    for block in language.keys():
        for (key, val) in config.items(block):
            language[block].append(key)
    logger.info(f'language: {language}')


def worker():
    print('start')
    time.sleep(random.randrange(10, 20))
    print('end')
    return


def add_thread(animal) -> uuid.UUID:
    t = threading.Thread(target=worker)
    new_uuid = uuid.UUID()
    threads[new_uuid] = t
    t.start()
    return new_uuid


@app.route("/ping")
def ping():
    name = request.args.get("name", "World")
    return f"pong {escape(name)}"


@app.route('/lookup/<string:animal>')
def lookup(animal):
    if animal in language.animals:
        id = add_thread(animal)
    else:
        raise


@app.route('/query/<uuid:id>')
def show_thread_state(id):
    return f'id {id}'


if __name__ == "__main__":
    read_config()
    app.run()
