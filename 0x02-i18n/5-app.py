#!/usr/bin/env python3

"""
Mock User Login and Display Messages
This module creates a Flask app that mocks user login and
displays messages based on user login status
"""


from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Union


app = Flask(__name__, template_folder='templates')


# Initialize the Babel extension
babel = Babel(app)


# Define Babel configuration
class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


# Define a mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """
    Define a function to get the user from the session
    based on the login_as parameter
    """
    try:
        login_as = request.args.get('login_as')
        user = users.get(int(login_as))
    except (ValueError, KeyError):
        user = None
    return user


@app.before_request
def before_request():
    """
    Set the user in the global context using the
    before_request decorator
    """
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Route for the home page"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Define a function to get the user's locale for translation
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
