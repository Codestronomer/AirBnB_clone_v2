#!/usr/bin/python3
"""This module defines and runs a flask application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception):
    """
    Removes SQLAlchemy session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run()
