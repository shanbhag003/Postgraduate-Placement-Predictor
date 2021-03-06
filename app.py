#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import jsonify
import requests
import pickle
import argparse
import numpy as np
import sklearn
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio import start_server

model = pickle.load(open('knn_model.pkl','rb'))
app = Flask(__name__)

def predict():
        
    ssc_p = input("Enter your SSC Percentage: ", type = FLOAT)
    
    hsc_b_Others = select("Enter HSC Board of Education: ", ['Others', 'Central'])
    if (hsc_b_Others == 'Others'):
        hsc_b_Others = 1
    else:
        hsc_b_Others = 0
    
    hsc_s_Commerce = select("Enter HSC Specialization: ", ['Commerce', 'Science', 'Arts'])
    if (hsc_s_Commerce == 'Commerce'):
        hsc_s_Commerce = 1
        hsc_s_Science = 0
    elif (hsc_s_Commerce == 'Science'):
        hsc_s_Commerce = 0
        hsc_s_Science = 1
    else:
        hsc_s_Commerce = 0
        hsc_s_Science = 0
    
    hsc_p = input("Enter your HSC Percentage: ", type = FLOAT)
    
    degree_t_Others = select("Enter Graduation Specialization: ", ['Sci_Tech', 'Comm_Mgmt', 'Others'])
    if (degree_t_Others == 'Others'):
        degree_t_Others = 1
        degree_t_Sci_Tech = 0
    elif (degree_t_Others == 'Sci&Tech'):
        degree_t_Others = 0
        degree_t_Sci_Tech = 1
    else:
        degree_t_Others = 0
        degree_t_Sci_Tech = 0
    
    degree_p = input("Enter your Graduation Percentage: ", type = FLOAT)
    
    specialisation_Mkt_HR = select("Enter Post Graduation Specialization: ", ['Mkt_HR', 'Mkt_Fin'])
    if (specialisation_Mkt_HR == 'Mkt&HR'):
        specialisation_Mkt_HR = 1
    else:
        specialisation_Mkt_HR = 0
    
    mba_p = input("Enter your MBA Percentage: ", type = FLOAT)
    
    etest_p = input("Enter your Aptitude Score (Out of 100): ", type = NUMBER)
    
    workex_Yes = select("Do you have work experience? ", ['Yes', 'No'])
    if (workex_Yes == 'Yes'):
        workex_Yes = 1
    else:
        workex_Yes = 0
    
    
    
    prediction = model.predict([[ssc_p, hsc_p, degree_p, mba_p, etest_p, hsc_b_Others, hsc_s_Commerce, hsc_s_Science,
                                 degree_t_Others, degree_t_Sci_Tech, workex_Yes, specialisation_Mkt_HR]])
    output = prediction
    
    if output == 0:
        put_text("Your chances of getting placed are quite low. Try working on developing your skills.")
    else:
        put_text("You are more likely to get placed.")

app.add_url_rule('/tool', 'webio_view', webio_view(predict), methods = ['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)

#if __name__ = '__main__':
    #predict()

#app.run(host = 'Localhost', port = 80)

