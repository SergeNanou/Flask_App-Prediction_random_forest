#importing libraries
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import os
from sklearn.model_selection import train_test_split
import flask
import pickle
from flask import Flask, render_template, request
import numpy 
import re
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
 
#prediction function
def ValuePredictor(to_predict_list):
    to_predict = numpy.array(to_predict_list).reshape(1,6)
    classifier = pickle.load(open('mypicklefile',"rb"))
    #classifier = joblib.load('classifier.joblib')
    #loaded_model_1 = list(loaded_model.values())[0]           
    result = classifier.predict(to_predict)
    
@app.route('/result',methods = ['POST'])

def result():
    result_1 = ""
    if request.method == 'POST':
        to_predict_list= request.form.to_dict()
        to_predict_list_1=list(to_predict_list.values())
        to_predict_list = to_predict_list_1[0:6]
        country = int(to_predict_list_1[6])
        #to_predict_list = list(map(int,to_predict_list))
        to_predict = numpy.array(to_predict_list).reshape(1,6)
        # Error checking
        #data = request.get_json(force=True)

        # Convert JSON to numpy array
        #predict_request = [data['sl'],data['sw'],data['pl'],data['pw'],data['pk']]
        #predict_request = np.array(predict_request)


        
        #loaded_model = pickle.load(open('mypicklefile',"rb"))
        classifier = joblib.load('classifier.joblib')
                
        result = classifier[country].predict(to_predict)
        L_1 = [10,11,12,13,14,15,16,17,18]
        L_2 = [20,22,23,24,25,26,27,28]
        if result[0] in L_1:
            result_1 = "MILITARY CRISES"
        elif result[0] in L_2:
            result_1 = "REBELS CRISES"
        elif result[0] in [40,44,45,46,47,48]:
            result_1 = "POLITICAL CRISES"
        elif result[0] in [50,55,57,58]:
            result_1 = "RIOTERS CRISES"
        elif result[0] in [60,66,67,68,78]:
            result_1 = "PROTESTERS CRISES"
        else: 
            result_1 = "OTHER ACTION"
        
        
    return render_template("result.html", prediction = result_1)

if __name__ == "__main__":
    app.run(debug =True)