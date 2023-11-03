#!/usr/bin/env python3

"""
Basic Babel Setup
This module configures Babel for a Flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)


class Config:
    """
    Configure class for Flask app
    This class sets Babel's default locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """
    Render the index.html template with page title
    and header
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
