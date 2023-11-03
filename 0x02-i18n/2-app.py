#!/usr/bin/env python3

"""
Get locale from request
This module creats a get_locale function to
determine the best match with supported languages
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


# Configure Babel
babel = Babel(app)


class Config:
    """
    Configure class for flask app
    This class sets Babel's default locale and timezone
    """
    LANGUANGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match with supported languages
    This function uses request.accept_languages to determine
    the user's preferred language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Render the index.html template with page title and header
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
