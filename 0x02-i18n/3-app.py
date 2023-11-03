#!/usr/bin/env python3

"""
Parametrize templates with Babel
This module parametrizes templates uding the
gettext function
"""


from flask import Flask, render_template
from flask_babel import Babel, _, gettext


app = Flask(__name__)


# Configure Babel
babel = Babel(app)


class Config:
    """
    Config class for Flask app
    This class sets Babel's default locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with supported languages
    This function uses request.accept_languages to
    determine the user's preferred language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index.html template with parametrized
    page title and header
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
