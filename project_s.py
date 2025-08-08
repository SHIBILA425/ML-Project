import streamlit as st
import joblib
import os

# Load the model
model_path =  r"lr_prjct"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please check the file path.")
    st.stop()

# App title
st.title("Price Predictor: Insights for Smarter Decisions")
st.write("An AI-powered tool designed to help you analyze,predict total prices and optimize business decisions effortlessly")



# Input grid
col1, col2, col3 = st.columns(3)

with col1:
    product_price = st.number_input('Enter the product price:', min_value=0.0, step=0.1)
    quantity = st.number_input('Enter the quantity:', min_value=0, step=1)
    profit_margin = st.number_input('Enter the profit margin (%):', min_value=0.0, max_value=100.0, step=0.1)

with col2:
    effective_price = st.number_input('Enter the effective price:', min_value=0.0, step=0.1)
    total_product_value = st.number_input('Enter the total product value:', min_value=0.0, step=0.1)

with col3:
    discounted_total_price = st.number_input('Enter the discounted total price:', min_value=0.0, step=0.1)
    profit = st.number_input('Enter the profit:', min_value=0.0, step=0.1)

# Predict button
if st.button('Check Prediction'):
    try:
        # Ensure the input is a 2D array
        input_data = [[
            product_price,
            quantity,
            profit_margin,
            effective_price,
            total_product_value,
            discounted_total_price,
            profit
        ]]
        predicted = model.predict(input_data)
        st.success(f"The predicted outcome is: {predicted[0]:.2f}. Prediction Successful!!! Unlocking Accurate Insights for Smarter Decisions.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
