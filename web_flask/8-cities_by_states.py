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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders states list"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run()
