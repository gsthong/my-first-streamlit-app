import streamlit as st
import pickle
import numpy as np

st.title("Ice Cream Sales Prediction")

f = open('model.pickle', 'rb')
model = pickle.load(f)

# x_new= (np.array(st.number_input("Input Temperature"))).reshape(-1,1)
# y_new = model.predict(x_new)
temperature = st.number_input("Enter temperature (in Celsius)")
y_new = model.predict(np.array(temperature).reshape(-1, 1))

if st. button('Predict'):
	st.write('Revenue Prediction')
	st.success(y_new[0][0])
