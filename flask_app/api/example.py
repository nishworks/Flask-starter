import logging

import flask_restful

from flask_app.api import base

log = logging.getLogger(__name__)


class Resource(flask_restful.Resource):
    def get(self):
        return base.json_response({None: None}, 200)
