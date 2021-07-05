#!/usr/bin/env python3

import configparser

import threading
import uuid
import time
import random

from flask import Flask, escape, request

app = Flask(__name__)

threads = {}

config = configparser.ConfigParser(allow_no_value=True)
config.read('zookeeper.conf')

def worker():
    print('start')
    time.sleep(random.randrange(10, 20))
    print('end')
    return


def add_thread(animal) -> uuid.UUID:
    t = threading.Thread(target=worker)
    new_uuid=uuid.UUID()
    threads[new_uuid]=t
    t.start()
    return new_uuid


@app.route("/ping")
def ping():
    name = request.args.get("name", "World")
    return f"pong {escape(name)}"


@app.route('/lookup/<string:animal>')
def lookup(animal):
    if animal in config.animals:
        id=add_thread(animal)


@app.route('/query/<uuid:id>')
def show_thread_state(id):
    return f'id {id}'


if __name__ == "__main__":
    app.run()
