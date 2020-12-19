import os
import socket

from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return 'Running...'

hostname = socket.gethostname()

@app.route('/greetings')
def hello():
    return 'Hello World from %s' %hostname

app.run(host="0.0.0.0", debug = True)