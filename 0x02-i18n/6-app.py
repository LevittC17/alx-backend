#!/usr/bin/env python3

"""
Use User's preferred Locale
This module creates a Flask app that uses a user's
preferred locale based on priority
"""


from flask_babel import Babel, _, gettext
from flask import Flask, render_template, request, g


app = Flask(__name__, template_folder='templates')


# Initialize Babel extension
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Define a function to get a user's preferred locale
    based on priority
    """
    # Priority 1: Locale from URL parameters
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    # Priority 2: Locale from user settings
    if g.user and 'locale' in g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Priority 3: Locale from request header
    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        header_locale = header_locale.split(',')[0].split(';')[0]
        if header_locale in app.config['LANGUAGES']:
            return header_locale

    # Priority 4: Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


# Define a mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Define a function to get the user based on the
    login_as parameter
    """
    user_id = request.args.get('login_as')
    return users.get(int(user_id)) if user_id else None


@app.before_request
def before_request():
    """
    Set the user in the global contect using the
    before_request decorator
    """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """
    Define a route for the home page
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
