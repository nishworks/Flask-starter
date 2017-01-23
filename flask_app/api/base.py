from __future__ import absolute_import

import decimal
import json
import logging

import flask

log = logging.getLogger(__name__)


def json_handler(obj):
    """ Handles non-serializable objects """
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    try:
        return str(obj)
    except TypeError:
        return obj.__dict__


def json_response(response, status_code, message=None, errors=None, headers=None):
    """ Return a http json response """
    response = {
        'uri': flask.request.path,
        'message': message,
        'status': status_code,
        'request-params': flask.g.request_args,
        'request-method': flask.request.method,
        'response': response,
        'errors': errors
    }
    resp = flask.make_response(
        json.dumps(response, default=json_handler),
        status_code,
        {'Content-Type': 'application/json',
         'Access-Control-Allow-Origin': '*'})
    resp.headers.extend(headers or {})
    return resp
