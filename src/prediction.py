from sklearn import datasets
from joblib import load
import numpy as np
import json

from flask import request, jsonify
import pandas as pd

import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics


UPLOAD_FOLDER='.'

def upload(filename):
    f = request.files['file']
    f.save(filename)
    return filename

def new(filename):
    my_model = load('bike_sharing_model.pkl')
    name = upload(filename)
    old_df = pd.read_csv(name, index_col =[0])


    missing_value=["Undefined"]
    day = ['dteday']
    features = ['season', 'mnth', 'holiday', 'weekday', 'weathersit', 'atemp', 'windspeed', 'hum']

    df = old_df[features]
    day_df = old_df[day]

    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])

    x = df[features]#.values.reshape(-1,1)

    pca = PCA(n_components=6, whiten = False, random_state = 2019)
    pca.fit(x)

    test_data=pca.transform(x)
    #print('data shape', test_np.shape)

    test_np = test_data#.to_numpy()

    #print('data shape', test_np.shape)
    pred = my_model.predict(test_np)
    
    #pred = scaler.inverse_transform(pred)

    pred_list = pred.tolist()
    #day_list = day_df.tolist()
    #days = day_df.to_numpy()

    
    #df_plot = pd.DataFrame({'Day of Year': days, 'Number of Bikers': pred})
    #pred_list = df_plot.to_numpy()
    '''
    df_plot.plot.scatter(x = 'Day of Year', y = 'Number of Bikers')
    plt.title("Linear Regression of Bike Model")
    
    
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format = 'png')
    bytes_image.seek(0)
    return bytes_image
    '''

    json_str = json.dumps(pred_list)
    return json_str
