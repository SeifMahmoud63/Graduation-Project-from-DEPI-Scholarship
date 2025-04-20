import streamlit as st
import pickle
import numpy as np

with open(r"C:\Users\test\DEPI Project\Project DEPI.pkl","rb") as f:
    pipeline = pickle.load(f)

st.title("Product Price Prediction")

length = st.number_input("Product Length (cm)")
height = st.number_input("Product Height (cm)")
width = st.number_input("Product Width (cm)")
weight = st.number_input("Product Weight (g)")
desc_length = st.number_input("Description Length")
volume = length * height * width

user_input = np.array([[weight, volume, height, desc_length]])

predicted_log_price = pipeline.predict(user_input)
predicted_price = np.exp(predicted_log_price)

st.success(f"Predicted Price: {predicted_price[0]:.2f} EGP")
