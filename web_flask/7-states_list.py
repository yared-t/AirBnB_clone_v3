#!/usr/bin/python3
# Author: MikiasHailu
""" This sript will starts a flask web application """
from flask import Flask, render_template
from models import FileStorage
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """ This function will handle teardown """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ This function to render states """
    states = storage.all('State').values()
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
