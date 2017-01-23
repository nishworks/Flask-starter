__doc__ = """

        http://flask.pocoo.org/docs/0.10/quickstart/

        render_template renders the variables and html, returning plain text string.
        Notice how we directly return string in hello_world example
"""

import logging

from flask import Flask, render_template
from flask_app import utils

utils.setup_root_logger_handler()
app = Flask(__name__)


log = logging.getLogger(__name__)

@app.route('/simple')
def template_example():
    return render_template('simple_template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])

@app.route('/')
def hello_world():
    log.info('Root path')
    return 'Hello World! <br /> <a href="simple"> Simple template </a>'

if __name__ == '__main__':
    app.run()
