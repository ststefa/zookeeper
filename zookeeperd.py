#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hallo Welt"

if __name__ == "__main__":
    app.run()
