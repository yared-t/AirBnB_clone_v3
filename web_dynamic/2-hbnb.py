#!/usr/bin/python3
#Author: MikiasHailu
""" this moudle will flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ This fucniton will close the Session """
    storage.close()


@app.route('/2-hbnb/', strict_slashes=False)
def hbnb():
    """ this is the hbnb fucniton """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)
    cache_id = uuid.uuid4()

    return render_template('2-hbnb.html',
            states=st_ct,
            amenities=amenities,
            places=places,
            cache_id=cache_id)

    if __name__ == "__main__":
        """ This is the main funciton """
    app.run(host='0.0.0.0', port=5000)
