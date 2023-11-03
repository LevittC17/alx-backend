#!/usr/bin/env python3
'''
Use Babel to get user locale
'''

from flask_babel import Babel
from flask import Flask, render_template, request

# Create the Flask app with a custom template folder
app = Flask(__name__, template_folder='templates')

# Initialize Babel extension
babel = Babel(app)

# Define supported languages and configure the app
app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


# Define a separate function to create the app
def create_app():
    return app


# Define a route for the home page
@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    return render_template('3-index.html')


# Define a separate function to handle locale selection
@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
