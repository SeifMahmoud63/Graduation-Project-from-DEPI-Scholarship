import streamlit as st
import pickle
import numpy as np
import pandas as pd


with open(r"C:\Users\test\DEPI Project\Project DEPI.pkl", "rb") as f:
    exec=pickle.load(f)

st.title("Product Price Prediction")


payment_sequential = st.number_input("Payment Sequential", min_value=0)
payment_installments = st.number_input("Payment Installments", min_value=0)
product_name_length = st.number_input("Product Name Length", min_value=0)
product_description_length = st.number_input("Product Description Length", min_value=0)
product_photos_qty = st.number_input("Product Photos Quantity", min_value=0)
product_weight_g = st.number_input("Product Weight (g)", min_value=0)
product_length_cm = st.number_input("Product Length (cm)", min_value=0)
product_height_cm = st.number_input("Product Height (cm)", min_value=0)
product_width_cm = st.number_input("Product Width (cm)", min_value=0)
freight_value = st.number_input("Freight Value (Shipping Cost)", min_value=0.0)

order_status = st.selectbox("Order Status", ['delivered', 'shipped', 'canceled', 'processing', 'unavailable', 'invoiced'])
customer_city = st.text_input("Customer City")
product_category_name_english = st.text_input("Product Category")
seller_city = st.text_input("Seller City")


input_data = pd.DataFrame([{
    "payment_sequential": payment_sequential,
    "payment_installments": payment_installments,
    "product_name_lenght": product_name_length,
    "product_description_lenght": product_description_length,
    "product_photos_qty": product_photos_qty,
    "product_weight_g": product_weight_g,
    "product_length_cm": product_length_cm,
    "product_height_cm": product_height_cm,
    "product_width_cm": product_width_cm,
    "freight_value": freight_value,
    "order_status": order_status,
    "customer_city": customer_city,
    "product_category_name_english": product_category_name_english,
    "seller_city": seller_city
}])


if st.button("Predict Price"):
    predicted_log_price = exec.predict(input_data)
    predicted_price = np.expm1(predicted_log_price)  
    st.success(f"Predicted Price: {predicted_price[0]:.2f} EGP")
