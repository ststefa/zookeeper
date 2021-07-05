#!/usr/bin/env python3

import threading
import uuid

from flask import Flask, escape, request

app = Flask(__name__)

threads={}

def worker():
    """thread worker function"""
    print 'Worker'
    return

def add_thread() -> uuid.uuid:
    pass

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

@app.route("/ping")
def ping():
    name = request.args.get("name", "World")
    return f"pong {escape(name)}"

@app.route('/lookup/<string:animal>')
def show_thread_state(tid):
    return f'tid {tid}'

@app.route('/list/<uuid:tid>')
def show_thread_state(tid):
    return f'tid {tid}'

if __name__ == "__main__":
    app.run()
