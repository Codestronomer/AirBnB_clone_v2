#!/usr/bin/env python3
"""
Entry file for flask app
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
