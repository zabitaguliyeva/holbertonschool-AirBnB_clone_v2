#!/usr/bin/python3
"""0-hello_route.py"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Hello HBnB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """C"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Python"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """Number template"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_route(n):
    """Number odd or even"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, odd_or_even="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
