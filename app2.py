import streamlit as st
import pickle
import numpy as np

st.title("Revenue Prediction")

f = open('model.pickle', 'rb')
model = pickle.load(f)

temperature = st.number_input("Enter temperature (in Celsius)")
y_new = model.predict(np.array(temperature).reshape(-1, 1))

if st. button('Predict'):
	st.write('Revenue Prediction')
	st.success(y_new[0][0])
