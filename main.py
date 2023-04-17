import os
import json
import logging
from flask import Flask, make_response
from flask_restful import Api
from simplexml import dumps

app = Flask(__name__)
api = Api(app)

# Write to application access log
app.logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('access.log')
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.before_request
def log_request_info(request):
    app.logger.info('Request: %s %s %s %s', request.method, request.url, request.headers, request.get_data())

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

@app.route("/api/headers")
def headers():
    headers=[
        "HTTP/1.x 200 OK",
        "Transfer-Encoding: chunked",
        "Date: Sat, 28 Nov 2009 04:36:25 GMT",
        "Server: nginx",
        "Connection: close",
        "X-Powered-By: W3 Total Cache/0.8",
        "Cache-Control: max-age=3600, public",
        "Content-Type: text/html; charset=UTF-8",
        "Last-Modified: Sat, 28 Nov 2009 03:50:37 GMT",
        "Content-Encoding: gzip",
        "Vary: Accept-Encoding, Cookie, User-Agent"
    ]
    return '<br>'.join(headers)


@app.post("/api/post")
def post():
    body = ['<h1>App is working</h1>', '<p><strong>Finally can get some coffee</strong></p>']
    return '<br>'.join(body)