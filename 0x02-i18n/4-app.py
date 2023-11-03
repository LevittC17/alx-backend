#!/usr/bin/env python3

"""
Force locale with URL parameter
This module allows you to force a specific locale
using the locale parameter in the URL
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext


app = Flask(__name__)


# Configure Babel
babel = Babel(app)


class Config:
    """
    Config class for Flask app.
    This class sets Babel's default locale and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match with supported languages.
    This function uses request.accept_languages and the 'locale'
    parameter in the URL to determine the user's preferred language
    """
    user_locale = request.args.get('locale')
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template with
    parametrized page title and header
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
