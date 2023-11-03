#!/usr/bin/env python3

"""
Mock User Login and Display Messages
This module creates a Flask app that mocks user login and
displays messages based on user login status
"""

from flask_babel import Babel, _, gettext
from flask import Flask, render_template, request, g


app = Flask(__name__, template_folder='templates')


babel = Babel(app)


# Define a mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Define a function to get a user based on the user
    ID or login_as parameter
    """
    user = users.get(user_id)
    if user:
        return user
    login_as = request.args.get('login_as')
    if login_as:
        user = users.get(int(login_as))
    return user


@app.before_request
def before_request():
    """
    Define a before_request function to set the user
    in the global context
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Render html template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
