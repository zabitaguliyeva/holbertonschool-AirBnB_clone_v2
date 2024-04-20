#!/usr/bin/python3
""" Flask """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Hello Hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Hello Hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
    """Text"""
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
