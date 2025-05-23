from sklearn import datasets
from joblib import load
import numpy as np
import json
import matplotlib.pyplot as plt
from flask import Flask, send_file, render_template
import os
import io
from flask import request, jsonify
import pandas as pd

UPLOAD_FOLDER='.'

def upload(filename):
    f = request.files['file']
    f.save(filename)
    return filename

def gen_plot(name):
   # my_model = load('logs_heart_mdl.pkl')
    #name = upload(filename)
    # HARD CODED test in here so when I upload I must name my file test
    test_data = pd.read_csv(name, index_col =[0])
    test_data.plot(kind='hist').get_figure()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format = 'png')
    bytes_image.seek(0)
    return bytes_image

def disp_plot(name):
    plot = gen_plot(name)
    #plot.savefig(os.path.join('static', 'images', 'plot.png'))
    #return render_template('test.html')
    return send_file(plot, mimetype='image/png')

def html(name):
    test_data = pd.read_csv(name, index_col =[0])
    plot = test_data.plot(kind='hist').get_figure()
    plot.savefig(os.path.join('static', 'images', 'plot.png'))
    return render_template('new.html')

def html_hello():
    return render_template('hello_template.html')
