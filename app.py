# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020
@author: Fred Bone
"""
import joblib as joblib
import numpy as np
import pickle
import pandas as pd
from config import config

#from flasgger import Swagger
import streamlit as st

#app=Flask(__name__)
#Swagger(app)

#pickle_in = open("classifier.pkl","rb")
#classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_term_deposit(*args):
    """ Predict if the client will subscribe a term deposit .
    ---
    parameters:
      - name: age
        in: query
        type: number
        required: true
      - name: job
        in: query
        type: string
        required: true
      - name: marital
        in: query
        type: string
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    Random_Forest = joblib.load(filename='./Random_Forest.pkl')
    #input_data = pd.DataFrame([[age, job, marital, education, default, balance, housing,
    #   loan, contact, day, month, campaign, pdays, previous, poutcome]])
    #prediction = Random_Forest.predict([[variance, skewness, curtosis, entropy]])
    prediction =  pd.DataFrame([age, job])
    print(prediction)
    return prediction


def main():
    st.title("Bank Direct Marketing")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Clients' Term Deposit Subscription Prediction App </h2>
    </div>
    """
    JOB_LIST = config.JOB_LIST
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("age", "Type Here")
    job = st.selectbox("job", JOB_LIST)
    marital = st.text_input("marital", "Type Here")
    education = st.text_input("education", "Type Here")
    default = st.text_input("default", "Type Here")
    balance = st.text_input("balance", "Type Here")
    housing = st.text_input("housing", "Type Here")
    loan = st.text_input("loan", "Type Here")
    contact = st.text_input("contact", "Type Here")
    day = st.text_input("day", "Type Here")
    month = st.text_input("month", "Type Here")
    campaign = st.text_input("campaign", "Type Here")
    pdays = st.text_input("pdays", "Type Here")
    previous = st.text_input("previous", "Type Here")
    poutcome = st.text_input("poutcome", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_term_deposit(variance, skewness, curtosis, entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
