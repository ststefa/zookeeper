#!/usr/bin/env python3

import configparser

import threading
import uuid
import time
import json
import random

import flask
from werkzeug.exceptions import HTTPException

# Simplistic logging
import logging

logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

app = flask.Flask(__name__)

# Where we keep our threads. A real world implementation would probably use a
# more sophisticated approach
threads = {}

# The "language" by which we compute the status
language = {
    'animals': [],
    'verbs': [],
    'adjectives': [],
    'adverbs': [],
}


class ZookeeperException(HTTPException):
    """ Generic base exception class for zoo-related problems. It inherits
        from HTTPException to allow for simplified flask "over-HTTP" handling
    """
    code = 500


def read_config():
    """ Simplistic config file input without content verification. The filename
        is hardcoded "zookeeper.conf". It has to have sections for every
        element of the language. Each section must contain key-only lines.
    """
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('zookeeper.conf')
    # Optimistically assumes that the file sections match the language
    for block in language.keys():
        for (key, val) in config.items(block):
            language[block].append(key)
    logger.info(f'language: {language}')


def build_status(animal) -> str:
    """ Create the "status" of the animals by randomly building a sentence with
        fixed assembly logic "adjective animal verb adverb"
    """
    adjective = random.choice(language['adjectives']).capitalize()
    verb = random.choice(language['verbs'])
    adverb = random.choice(language['adverbs'])
    return f'{adjective} {animal} {verb} {adverb}'


def worker(id: uuid.UUID, animal: str):
    """ The thread emulating the workload. It randomly waits for 10-20 seconds
        and then assigns the animals status as the threads value. This
        also eliminates the reference to the thread
    """
    logger.debug('thread start')
    time.sleep(random.randrange(10, 20))
    threads[id] = build_status(animal)
    logger.debug('thread end')
    return


def add_thread(animal) -> uuid.UUID:
    """ Create a new worker thread and add it to the global threads
        dictionary
    """
    # see https://docs.python.org/3/library/uuid.html for variations
    new_uuid = uuid.uuid4()
    thread = threading.Thread(target=worker, args=(new_uuid, animal))
    threads[new_uuid] = thread
    thread.start()
    return new_uuid


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.route('/animals')
def get_animals():
    """ Get a list of animals in the zoo. Any animal can be queried
    """
    return json.dumps(language['animals'])


@app.route('/animals/<string:animal>')
def query_status(animal):
    """ Start a status query for an animal
    """
    if animal in language['animals']:
        id = add_thread(animal)
        return json.dumps(str(id))
    else:
        raise ZookeeperException(f'No such animal: {animal}')


@app.route('/query/<uuid:id>')
def show_thread_state(id):
    """ Show the current result of the query. An ongoing query is reflected
        by "..."
    """
    if id not in threads.keys():
        raise ZookeeperException(f'No query with id {id}')
    if isinstance(threads[id], threading.Thread):
        return json.dumps('...')
    else:
        return json.dumps(threads[id])


if __name__ == "__main__":
    read_config()
    app.run()
