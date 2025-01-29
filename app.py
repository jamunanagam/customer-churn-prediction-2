import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('best_churn_model1.pkl')

def predict(features):
    return model.predict([features])[0]

st.title('Customer Churn Prediction')

# Create input fields for each feature
state = st.number_input('State', min_value=0, max_value=50, step=1)
area_code = st.number_input('Area Code', min_value=100, max_value=999, step=1)
voice_plan = st.selectbox('Voice Plan', [0, 1])
voice_messages = st.number_input('Voice Messages', min_value=0, max_value=100, step=1)
intl_plan = st.selectbox('International Plan', [0, 1])
intl_mins = st.number_input('International Minutes', min_value=0.0, max_value=20.0, step=0.1)
intl_calls = st.number_input('International Calls', min_value=0, max_value=20, step=1)
intl_charge = st.number_input('International Charge', min_value=0.0, max_value=5.0, step=0.1)
customer_calls = st.number_input('Customer Service Calls', min_value=0, max_value=10, step=1)
total_mins = st.number_input('Total Minutes', min_value=0.0, max_value=1000.0, step=1.0)
total_calls = st.number_input('Total Calls', min_value=0, max_value=500, step=1)
total_charge = st.number_input('Total Charge', min_value=0.0, max_value=100.0, step=1.0)

# Collect the features into a list
features = [state, area_code, voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, customer_calls, total_mins, total_calls, total_charge]

# Predict button
if st.button('Predict'):
    result = predict(features)
    st.write(f'Prediction: {"Churn" if result == 1 else "No Churn"}')
