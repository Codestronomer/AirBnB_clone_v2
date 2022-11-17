#!/usr/bin/python3
"""
    Route /hbnb to display HBNB HTML page
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """
        Route /hbnb to display HBNB HTML page
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """
        Function to remove SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run()
