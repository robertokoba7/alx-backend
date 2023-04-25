#!/usr/bin/env python3
"""
basic flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """
    Config class for Babel object
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
# babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the user's preferred language by
    checking the Accept-Language header.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """render a HTML file"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
