import streamlit as st
import pickle

f = open('model.pickle', 'rb')
model = pickle.load(f)

def predict_revenue(temperature):
    revenue = model.predict([[temperature]])
    return revenue[0]

st.title("Ice Cream Sales Prediction")
temperature = st.number_input("Enter temperature (in Celsius)")
revenue = predict_revenue(temperature)
st.write(f"Predicted revenue: {revenue}")
