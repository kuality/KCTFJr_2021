#!/usr/bin/env/pyhon3

import os
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('flask_debug_pin.html')

@app.route('/<path:file>')
def file(file):
    return open(file).read()



app.run(host='0.0.0.0',port=8000,threaded=True,debug=True)