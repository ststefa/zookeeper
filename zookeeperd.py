#!/usr/bin/env python3

import configparser

import threading
import uuid
import time
import random

import flask
from werkzeug.exceptions import HTTPException

import logging
# Simplistic logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

app = flask.Flask(__name__)

# Where we keep our threads. A real world implementation would probably use a
# more sophisticated approach
threads = {}

language = {
    'animals': [],
    'verbs': [],
    'adjectives': [],
    'adverbs': [],
}


class ZookeeperException(HTTPException):
    pass


def read_config():
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('zookeeper.conf')
    for block in language.keys():
        for (key, val) in config.items(block):
            language[block].append(key)
    logger.info(f'language: {language}')

def build_status(animal) -> str:
    adjective=random.choice(language['adjectives']).capitalize()
    verb=random.choice(language['verbs'])
    adverb=random.choice(language['adverbs'])
    return f'{adjective} {animal} {verb} {adverb}'

def worker(id: uuid.UUID, animal: str):
    logger.debug('thread start')
    time.sleep(random.randrange(10, 20))
    threads[id] = build_status(animal)
    logger.debug('thread end')
    return


def add_thread(animal) -> str:
    new_uuid = uuid.uuid4()
    thread = threading.Thread(target=worker, args=(new_uuid, animal))
    threads[new_uuid] = thread
    thread.start()
    return str(new_uuid)


@app.errorhandler(Exception)
def handle_exception(e):
    logger.exception(e)
    return str(e), 500


@app.route('/animals')
def get_animals():
    return ", ".join(language['animals'])

@app.route('/animals/<string:animal>')
def animals(animal):
    if animal in language['animals']:
        id = add_thread(animal)
        return id
    else:
        raise ZookeeperException(f'No such animal: {animal}')


@app.route('/query/<uuid:id>')
def show_thread_state(id):
    if id not in threads.keys():
        raise ZookeeperException(f'No query with id {id}')
    if isinstance(threads[id], threading.Thread):
        return '...'
    else:
        return threads[id]


if __name__ == "__main__":
    read_config()
    app.run()
