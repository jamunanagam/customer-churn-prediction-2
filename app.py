import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('best_churn_model1.pkl')

def predict(features):
    return model.predict([features])[0]

st.title('Customer Churn Prediction')

# Create input fields for each feature
state_mapping = {
    'Alabama': 0, 'Alaska': 1, 'Arizona': 2, 'Arkansas': 3, 'California': 4,
    'Colorado': 5, 'Connecticut': 6, 'Delaware': 7, 'Florida': 8, 'Georgia': 9,
    'Hawaii': 10, 'Idaho': 11, 'Illinois': 12, 'Indiana': 13, 'Iowa': 14,
    'Kansas': 15, 'Kentucky': 16, 'Louisiana': 17, 'Maine': 18, 'Maryland': 19,
    'Massachusetts': 20, 'Michigan': 21, 'Minnesota': 22, 'Mississippi': 23,
    'Missouri': 24, 'Montana': 25, 'Nebraska': 26, 'Nevada': 27, 'New Hampshire': 28,
    'New Jersey': 29, 'New Mexico': 30, 'New York': 31, 'North Carolina': 32,
    'North Dakota': 33, 'Ohio': 34, 'Oklahoma': 35, 'Oregon': 36, 'Pennsylvania': 37,
    'Rhode Island': 38, 'South Carolina': 39, 'South Dakota': 40, 'Tennessee': 41,
    'Texas': 42, 'Utah': 43, 'Vermont': 44, 'Virginia': 45, 'Washington': 46,
    'West Virginia': 47, 'Wisconsin': 48, 'Wyoming': 49
}
state_name = st.selectbox('State', list(state_mapping.keys()))
state = state_mapping[state_name]
area_code = st.number_input('Area Code', min_value=400, max_value=999, step=1)
voice_plan = st.selectbox('Voice Plan', ['No', 'Yes'])
intl_plan = st.selectbox('International Plan', ['No', 'Yes'])

# Map Yes/No to 0/1
voice_plan = 1 if voice_plan == 'Yes' else 0
intl_plan = 1 if intl_plan == 'Yes' else 0

no_voice_messages = st.number_input('Voice Messages', min_value=0, max_value=100, step=1)
intl_mins = st.number_input('International Minutes', min_value=0.0, step=0.1)
no_of_international_calls = st.number_input('International Calls', min_value=0, max_value=100, step=1)
intl_charge = st.number_input('International Charge', min_value=0.0, step=0.1)
customer_calls = st.number_input('Customer Service Calls', min_value=0, max_value=10, step=1)
total_mins = st.number_input('Total Minutes', min_value=0.0, max_value=1000.0, step=1.0)
total_calls = st.number_input('Total Calls', min_value=0, max_value=500, step=1)
total_charge = st.number_input('Total Charge', min_value=0.0, step=1.0)

# Collect the features into a list
features = [state, area_code, voice_plan, no_voice_messages, intl_plan, intl_mins, no_of_international_calls, intl_charge, customer_calls, total_mins, total_calls, total_charge]

# Predict button
if st.button('Predict'):
    result = predict(features)
    st.write(f'Prediction: {"Churn custumer will quit the company" if result == 1 else "No Churn custumer will not quit the company"}')
