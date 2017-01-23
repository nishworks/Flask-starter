import logging

import os
import sys

# Following code is to fix few issues related to python imports
# TODO: Remove this code with better solution
current_dir = os.path.dirname(os.path.abspath(__file__))
top_level_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
if top_level_dir not in sys.path:
    sys.path.append(top_level_dir)

import flask_script
from flask_app import webapp, utils

utils.setup_root_logger_handler()

log = logging.getLogger(__name__)

__doc__ = """

    Manager, Command and Option are Flask extensions that makes it develop with Flask.
    They provide a nice CLI with various default commands. More commands can be added
    by creating a command using 'Command' base class or '@manager.command' decorator.

    Run:
        python manage.py
        This will give you list of commands and descriptions
    Example Command execution:
        python manage.py runserver


"""

manager = flask_script.Manager(webapp.app)

manager.add_command("runserver", flask_script.Server(host="127.0.0.1", port=5000, use_reloader=True, threaded=True))


@manager.command
def routes():
    """
        Lists all routes currently defined in application
    """
    output = []
    for rule in webapp.app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = "{:50s} {:20s} {}".format(rule.endpoint, methods, rule)
        output.append(line)
    for line in sorted(output):
        print(line)


@manager.command
def config():
    """
        Lists config defined in application
    """
    keys = sorted(webapp.app.config.keys())
    print('\n----------------- Config -------------------\n')
    for key in keys:
        print("{0:40s} {1}".format(key, webapp.app.config[key]))
    print('\n')


if __name__ == "__main__":
    manager.run()
