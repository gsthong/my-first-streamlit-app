import streamlit as st
import pickle
import numpy as np

st.title("Ice Cream Sales Prediction")

f = open('model.pickle', 'rb')
model = pickle.load(f)

temperature = st.number_input("Enter temperature (in Celsius)")

revenue = model.predict(np.array(temperature).reshape(-1, 1))

if st. button('Predict'):
	st.success(f"Predicted revenue: {y_new[0][0].2f}")
