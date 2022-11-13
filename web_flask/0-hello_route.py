#!/usr/bin/env python3
"""
Entry file for flask app
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return f"Hello HBNB!"
