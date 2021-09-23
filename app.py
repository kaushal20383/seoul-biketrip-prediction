# pip install streamlit
import streamlit as st
from model import predict_duration
import numpy as np

st. set_page_config(page_title="Seoul Bike Trip Duration Prediction App", page_icon="***", layout ="wide")

with st.form("prediction_form"):
    st.header("Enter the deciding factors: ")
    distance = st.number_input('Distance: ', value=0, format='%d')
    haversine = st.number_input('Haversine: ')
    phour = st.slider('Pickup hour: ', 0, 23, value=0, format='%d')
    pmin = st.slider('Pickup minutes: ', 0, 59, value=0, format='%d')
    dhour = st.slider('Drop hour: ', 0, 23, value=0, format='%d')
    dmin = st.slider('Drop minute: ', 0, 59, value=0, format='%d')
    temp = st.number_input('Temp: ')
    humid = st.number_input('Humid: ')
    solar = st.number_input('Solar: ')
    dust = st.number_input('Dust: ')

    submit_val = st.form_submit_button('Predict Duration')
if submit_val:
    attribute = np.array([distance, haversine, phour, pmin, dhour,
                        dmin, temp, humid, solar, dust]).reshape(1,-1)
    if attribute.shape == (1,10):
        print('attribute valid')
        print(attribute)
        value = predict_duration(attributes= attribute)
        st.header("Here is the result: ")
        st.success(f'The Duration predicted is {value} mins')
