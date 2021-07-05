#!/usr/bin/env python3

import configparser

import threading
import uuid
import time
import random

from typing import Dict

from flask import Flask, escape, request

from werkzeug.exceptions import HTTPException

import logging
# Simplistic logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Where we keep our threads. A real world implementation would probably use a
# more sophisticated approach
threads = {}

language = {
    'animals': [],
    'verbs': [],
    'adjectives': [],
    'adverbs': [],
}


class ZookeeperException(BaseException):
    pass


def read_config():
    config = configparser.ConfigParser(allow_no_value=True)
    config.read('zookeeper.conf')
    for block in language.keys():
        for (key, val) in config.items(block):
            language[block].append(key)
    logger.info(f'language: {language}')


def error(message: str):
    logger.error(message)
    return message


def worker(id: uuid.UUID, animal: str):
    logger.debug('thread start')
    time.sleep(random.randrange(10, 20))
    threads[id] = animal
    logger.debug('thread end')
    return


def add_thread(animal) -> uuid.UUID:
    new_uuid = uuid.UUID()
    t = threading.Thread(target=worker, args=(new_uuid, animal))
    threads[new_uuid] = t
    t.start()
    return new_uuid


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    else:
        return str(e), 500


@app.route("/ping")
def ping():
    name = request.args.get("name", "you")
    return f"pong {escape(name)}"


@app.route('/lookup/<string:animal>')
def lookup(animal):
    if animal in language['animals']:
        id = add_thread(animal)
        return id
    else:
        return error(f'No such animal: {animal}')


@app.route('/list')
def list_threads():
    return ", ".join(threads.keys())


@app.route('/query/<uuid:id>')
def show_thread_state(id):
    if id not in threads.keys():
        return error(f'No such thread: {id}')
    if isinstance(threads[id], threading.Thread):
        return '...'
    else:
        return threads[id]


if __name__ == "__main__":
    read_config()
    app.run()
