#!/usr/bin/env python3

"""
Force locale with URL parameter
This module allows you to force a specific locale
using the locale parameter in the url
"""

from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')


# Initialize Babel extension
babel = Babel(app)

app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


# Define a separate function to create the app
def create_app():
    """Return route"""
    return app


# Define a route for the home page
@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """Render the html template"""
    return render_template('3-index.html')


# Define a separate function to handle locale selection
@babel.localeselector
def get_locale():
    """
    Determine the best match wot supported language
    This function uses request.accept_languages and the
    'locale' parameter in the URL to determine the user's
    preferred language
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
