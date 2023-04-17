import os
import json
from flask import Flask, make_response
from flask_restful import Api
from simplexml import dumps

app = Flask(__name__)
api = Api(app)

@api.representation('application/xml')
def output_xml(data, code, headers=None):
  resp = make_response(dumps({'response' : data}), code)
  resp.headers.extend(headers or {})
  return resp

@api.representation('application/json')
def output_json(data, code, headers=None):
  resp = make_response(json.dumps({'response' : data}), code)
  resp.headers.extend(headers or {})
  return resp

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/environment")
def environment():
    return '<br>'.join(os.environ)
