#!/usr/bin/python3
""" Flask """
from flask import Flask
from flask import render_template

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_pytext(text="is cool"):

    """Text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def hello_num(n):

    """Text"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_template(n):
    """Text"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hello_odd_even(n):
    """Text"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, odd_even="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, odd_even="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
