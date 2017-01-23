""" Version 1 of API. """
from __future__ import absolute_import

import logging

import flask
import flask_restful
from flask_app.api import example

log = logging.getLogger(__name__)

api_blueprint = flask.Blueprint('api', __name__)
api = flask_restful.Api(api_blueprint)

api.add_resource(example.Resource, '/example', endpoint='example')

