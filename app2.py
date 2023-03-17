import streamlit as st
import pickle
import numpy as np

st.title("Ice Cream Sales Prediction")

f = open('model.pickle', 'rb')
model = pickle.load(f)

temperature = st.number_input("Input Temperature")

y_new = model.predict(np.array(temperature).reshape(-1, 1))

if st. button('Predict'):
	st.write('Revenue Prediction')
	st.success(st.success(y_new[0][0]))
