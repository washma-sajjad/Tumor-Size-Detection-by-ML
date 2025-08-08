import streamlit as st
st.title("Hello, Everyone👋")
st.write("Welcome to Tumor Size Predictor – A non-invasive gene-based estimation tool powered by Machine Learning.")
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title('Tumor Size Prediction from Gene Expression')

uploaded_file = st.file_uploader("Upload your gene expression dataset (.csv)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of Dataset:", data.head())

    X = data.drop(columns=['Tumor_Size_cm'])
    y = data['Tumor_Size_cm']

    model = LinearRegression()
    model.fit(X, y)

    st.subheader("Enter Gene Expression Values for Prediction")

    input_data = []
    for gene in X.columns:
        value = st.number_input(f"Enter expression value for {gene}", min_value=0.0, max_value=20.0, step=0.1)
        input_data.append(value)

    if st.button('Predict Tumor Size'):
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)
        st.success(f"Predicted Tumor Size: {prediction[0]:.2f} cm")
else:
    st.info("Please upload the CSV file to continue.")
