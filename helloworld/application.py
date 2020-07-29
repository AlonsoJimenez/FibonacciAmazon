#!flask/bin/python
import json
from flask import Flask, Response
from flask import render_template
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return render_template("calculator.html")

@application.route('/', methods=['POST'])
def post():
    return render_template("calculator.html")

if __name__ == '__main__':
    flaskrun(application)
