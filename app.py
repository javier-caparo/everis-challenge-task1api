import os
import socket
import math

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def start():
    return 'Running...'

hostname = socket.gethostname()

@app.route('/greetings')
def hello():
    return 'Hello World from %s' %hostname

@app.route('/square/', methods=['GET'])
def square():
    if 'x' in request.args:
        x = int(request.args['x'])
        sq = math.pow(x,x)
        return 'Square of %d is %d' % (x, sq)
    else:
        return 'Error: No Number was provided. Please specify a number.'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug = True)