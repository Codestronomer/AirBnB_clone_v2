#!/usr/bin/python3
"""
Entry file for flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Returns C + the specified text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Displays python followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_text(n):
    """Displays number followed by text"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """Renders a HTML Page only if n is a integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """Renders a HTML page only if n is a integer"""
    even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, even_or_odd=even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
