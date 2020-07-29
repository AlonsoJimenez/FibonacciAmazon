#!flask/bin/python
import json
from flask import Flask, Response
from flask import render_template
from helloworld.flaskrun import flaskrun


application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(render_template("calculator.html"), mimetype='text/html', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(render_template("calculator.html"), mimetype='text/html', status=200)

if __name__ == '__main__':
    flaskrun(application)
