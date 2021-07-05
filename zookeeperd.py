#!/usr/bin/env python3

import configparser

import threading
import uuid
import time
import random

import flask
from werkzeug.exceptions import HTTPException

# Simplistic logging
import logging
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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
    """ Generic base exception class for zoo-related problems. It inherits
        from HTTPException to allow for simplified flask "over-HTTP" handling
    """
    pass

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
    adjective=random.choice(language['adjectives']).capitalize()
    verb=random.choice(language['verbs'])
    adverb=random.choice(language['adverbs'])
    return f'{adjective} {animal} {verb} {adverb}'

def worker(id: uuid.UUID, animal: str):
    """ The thread emulating the workload. It randomly waits for 10-20 seconds
        and then fills the threads value with the animals status
    """
    logger.debug('thread start')
    time.sleep(random.randrange(10, 20))
    threads[id] = build_status(animal)
    logger.debug('thread end')
    return


def add_thread(animal) -> str:
    """ Create a new worker thread and add it to the global threads
        dictionary
    """
    new_uuid = uuid.uuid4()
    thread = threading.Thread(target=worker, args=(new_uuid, animal))
    threads[new_uuid] = thread
    thread.start()
    return str(new_uuid)


@app.errorhandler(Exception)
def handle_exception(e):
    """ Allows the use of regular exceptions in the code by writing it to this
        process' log as well as returning it as a HTTP response
    """
    logger.exception(e)
    return str(e), 500


@app.route('/animals')
def get_animals():
    """ Get a list of animals in the zoo. Any animal can be queried
    """
    return ", ".join(language['animals'])

@app.route('/animals/<string:animal>')
def animals(animal):
    """ Start a status query for an animal
    """
    if animal in language['animals']:
        id = add_thread(animal)
        return id
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
        return '...'
    else:
        return threads[id]


if __name__ == "__main__":
    read_config()
    app.run()
