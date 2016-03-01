# -*- coding: utf-8 -*-

import os
import sys
import urllib

from flask.ext.script import Command, Option
from flask.ext.script import Manager

from flask_app import app
from config import APP_DIR, FLASK_APP_NAME, HOST, PORT, WORKERS

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

manager = Manager(app)


class GunicornServer(Command):
    """
        WSGI compliant server
        Gunicorn can spawn multiple flask instances
    """

    def __init__(self):
        pass

    def get_options(self):
        return (
            Option('-h', '--host',
                   dest='host',
                   default=HOST),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=PORT),

            Option('-w', '--workers',
                   dest='workers',
                   type=int,
                   default=WORKERS),
        )

    def run(self, host, port, workers):
        app_name = '%s:%s' % (APP_DIR, FLASK_APP_NAME)
        address = '{0}:{1}'.format(host, port)
        run_args = ['-b', address, '-w', str(workers), app_name]
        os.execvp('gunicorn', [''] + run_args)


manager.add_command("gunicorn", GunicornServer)


@manager.command
def routes():
    """
        Lists all routes currently defined in application
    """
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)
    for line in sorted(output):
        print(line)


@manager.command
def config():
    """
        Lists config defined in application
    """
    keys = sorted(app.config.keys())
    print '\n----------------- Config -------------------\n'
    for key in keys:
        print "{0:40s} {1}".format(key, app.config[key])
    print '\n'


@manager.command
def dirs():
    """
        Lists all important dirs in the project
    """
    print "{0:20s} {1}".format("Template Dir: ", app.template_folder)
    print "{0:20s} {1}".format("Uploads Dir: ", app.config.get('UPLOAD_FOLDER'))

if __name__ == "__main__":
    manager.run()
