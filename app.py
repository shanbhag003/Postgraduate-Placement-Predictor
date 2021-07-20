#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH

model = pickle.load(open('knn_model.pkl','rb'))
app = Flask(__name__)

def predict():
    ssc_p = input("Enter your SSC Percentage: ", type = float)
    
    hsc_p = input("Enter your HSC Percentage: ", type = float)
    
    degree_p = input("Enter your Graduation Percentage: ", type = float)
    
    mba_p = input("Enter your MBA Percentage: ", type = float)
    
    etest_p = input("Enter your Aptitude Score (Out of 100): ", type = int)
    
    gender_M = input("Enter Gender: ", ['M', 'F'])
    if (gender_M == 'M'):
        gender_M = 1
    else:
        gender_M = 0
        
    hsc_b_Others = input("Enter HSC Board of Education: ", ['Others', 'Central'])
    if (hsc_b_Others == 'Others'):
        hsc_b_Others = 1
    else:
        hsc_b_Others = 0
    
    hsc_s_Commerce = input("Enter HSC Specialization: ", ['Commerce', 'Science', 'Arts'])
    if (hsc_s_Commerce == 'Commerce'):
        hsc_s_Commerce = 1
        hsc_s_Science = 0
    elif (hsc_s_Commerce == 'Science'):
        hsc_s_Commerce = 0
        hsc_s_Science = 1
    else:
        hsc_s_Commerce = 0
        hsc_s_Science = 0
    
    degree_t_Others = input("Enter Graduation Specialization: ", ['Sci_Tech', 'Comm_Mgmt', 'Others'])
    if (degree_t_Others == 'Others'):
        degree_t_Others = 1
        degree_t_Sci_Tech = 0
    elif (degree_t_Others == 'Sci&Tech'):
        degree_t_Others = 0
        degree_t_Sci_Tech = 1
    else:
        degree_t_Others = 0
        degree_t_Sci_Tech = 0
    
    workex_Yes = input("Do you have work experience? ", ['Yes', 'No'])
    if (workex_Yes == 'Yes'):
        workex_Yes = 1
    else:
        workex_Yes = 0
    
    specialisation_Mkt_HR = input("Enter Post Graduation Specialization: ", ['Mkt_HR', 'Mkt_Fin'])
    if (specialisation_Mkt_HR == 'Mkt&HR'):
        specialisation_Mkt_HR = 1
    else:
        specialisation_Mkt_HR = 0
    
    prediction = model.predict([[ssc_p, hsc_p, degree_p, mba_p, etest_p, gender_M, hsc_b_Others, hsc_s_Commerce,
                                degree_t_Others, workex_Yes, specialisation_Mkt_HR]])
    output = prediction
    
    if output == 0:
        put_text("Chances of getting placed are quite low. You need to work hard on developing your skills.")
    else:
        put_text("You are more likely to get placed.")

app.add_url_rule('/tool', 'webio_view', webio_view(predict), methods = ['GET', 'POST', 'OPTIONS'])

#if __name__ = '__main__':
    #predict()

#app.run(host = 'Localhost', port = 80)

