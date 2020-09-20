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


CAT_VAR = config.CAT_VAR
NUM_VAR = config.NUM_VAR

#app=Flask(__name__)
#Swagger(app)

#pickle_in = open("classifier.pkl","rb")
#classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_term_deposit(age, job, marital, education, default, balance, housing, loan, contact, day, month, campaign, pdays, previous, poutcome):
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
    classifier = joblib.load(filename='./model/Random_Forest.pkl')
    file = open("./processing/disc.obj",'rb')
    disc = pickle.load(file)
    file.close()
    # input_var = [age, job, marital, education, default, balance, housing, loan, contact, day, month, campaign, pdays, previous, poutcome]
    input_data = pd.DataFrame([age, job, marital, education, default, balance, housing, loan, contact, day, month, campaign, pdays, previous, poutcome]).T
    input_data.columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
       'loan', 'contact', 'day', 'month', 'campaign', 'pdays', 'previous',
       'poutcome']

    input_data[CAT_VAR] = input_data[CAT_VAR].astype('category')
    input_data[NUM_VAR] = input_data[NUM_VAR].astype('int')
    # Discretization
    input_data = disc.transform(input_data)
    # Arbitrarily encoding
    file = open("./processing/enc.obj",'rb')
    enc_loaded = pickle.load(file)
    file.close()
    input_data = enc_loaded.transform(input_data.astype(str))
    # Making prediction
    prediction = classifier.predict(input_data)
    prediction = np.where(prediction < 1, 'no', 'yes')
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
    MARITAL_LIST = config.MARITAL_LIST
    EDUCATION_LIST = config.EDUCATION_LIST
    DEFAULT_LIST = config.DEFAULT_LIST
    HOUSING_LIST = config.HOUSING_LIST
    LOAN_LIST = config.LOAN_LIST
    CONTACT_LIST = config.CONTACT_LIST
    DAY_LIST = config.DAY_LIST
    MONTH_LIST = config.MONTH_LIST
    POUTCOME_LIST = config.POUTCOME_LIST

    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("Age", "Type Here")
    balance = st.text_input("balance", "Type Here")
    campaign = st.text_input("Campaign", "Type Here")
    pdays = st.text_input("Pdays", "Type Here")
    previous = st.text_input("Previous", "Type Here")
    job = st.selectbox("Job", JOB_LIST)
    marital = st.selectbox("Marital", MARITAL_LIST)
    education = st.selectbox("Education", EDUCATION_LIST)
    default = st.selectbox("Default", DEFAULT_LIST)
    housing = st.selectbox("Housing", HOUSING_LIST)
    loan = st.selectbox("Loan", LOAN_LIST)
    contact = st.selectbox("Contact", CONTACT_LIST)
    day = st.selectbox("Day", DAY_LIST)
    month = st.selectbox("Month", MONTH_LIST)
    poutcome = st.selectbox("Poutcome", POUTCOME_LIST)
    result = ""
    if st.button("Predict"):
        result = predict_term_deposit(age, job, marital, education, default, balance, housing, loan, contact, day, month, campaign, pdays, previous, poutcome)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
