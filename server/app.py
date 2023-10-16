#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:num>')
def count(num):
    result = ''
    for i in range(num):
        result += str(i) + '<br>'
    return result



if __name__ == '__main__':
    app.run(port=5555, debug=True)
