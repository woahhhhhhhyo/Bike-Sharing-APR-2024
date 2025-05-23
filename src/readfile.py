def txtfile(filename):
    with open(filename) as readfile:
     words = readfile.read().split()
    return words
import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file

UPLOAD_FOLDER='.'

def uploadf(filename):
    f = request.files['file']
    f.save(filename)
    return "Upload success"
