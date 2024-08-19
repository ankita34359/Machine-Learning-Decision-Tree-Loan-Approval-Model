import streamlit as st
import joblib
import pandas as pd
import numpy as np



st.header("Loan Approval Model")

initial_payment = st.number_input("Enter the initial payment amount")

final_payment = st.number_input("Enter the final payment amount")

credit_score = st.number_input("Enter the credit score")

model = joblib.load(r"C:\Users\Lenovo\OneDrive\Desktop\Juypter_projects\loan_model_DecisionTree.pkl")

input_array = np.array([[initial_payment, final_payment, credit_score]])

button = st.button("Submit")

if button:
    output = model.predict(input_array)
    st.info(f"Your loan status is {output}")