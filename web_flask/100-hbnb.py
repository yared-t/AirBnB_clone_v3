#!/usr/bin/python3
# Author: MikiasHailu

""" This will flask App that integrates with AirBnB static HTML Template """
from flask import Flask, render_template, url_for
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def teardown_db(exception):
    """ This will after each request, this method calls """
    storage.close()


@app.route('/hbnb')
def hbnb_filters(the_id=None):
    """ This will handles request to custom template with states, cities & amentities  """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('100-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users)

if __name__ == "__main__":
    """ MAIN Flask App """
    app.run(host=host, port=port)
