__doc__ = """

        http://flask.pocoo.org/docs/0.10/quickstart/

        render_template renders the variables and html, returning plain text string.
        Notice how we directly return string in hello_world example
"""

import logging
import os
import sys

# Following code is to fix few issues related to python imports
# TODO: Remove this code with better solution
current_dir = os.path.dirname(os.path.abspath(__file__))
top_level_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
if top_level_dir not in sys.path:
    sys.path.append(top_level_dir)


from flask import Flask, render_template
from flask_assets import Environment

from flask_app import utils
from flask_app.api import api_blueprint

utils.setup_root_logger_handler()
app = Flask(__name__)
assets = Environment(app)
log = logging.getLogger(__name__)
app.config['ASSETS_DEBUG'] = True
app.register_blueprint(api_blueprint, url_prefix='/api/v1/')


@app.route('/')
def index():
    return render_template('base_template.html')


if __name__ == '__main__':

    app.run()
