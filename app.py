import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load model and preprocessor
@st.cache_resource
def load_artifacts():
    model = load_model("models/model_keras.h5")
    preprocessor = joblib.load("utils/preprocessor.pkl")
    return model, preprocessor

model, preprocessor = load_artifacts()

# App title
st.title("Loan Stacking Detection App")

# Sidebar instructions
st.sidebar.header("User Input Features")

# Collect user inputs
def user_input_features():
    age = st.sidebar.slider("Age", 18, 80, 30)
    income = st.sidebar.number_input("Income", 1000, 100000, 40000)
    employment_status = st.sidebar.selectbox("Employment Status", ["Employed", "Self-Employed", "Unemployed"])
    education_level = st.sidebar.selectbox("Education Level", ["High School", "Bachelors", "Masters", "PhD"])
    region = st.sidebar.selectbox("Region", ["Nairobi", "Mombasa", "Kisumu", "Other"])
    number_of_active_loans = st.sidebar.slider("Number of Active Loans", 0, 10, 2)
    apps_installed = st.sidebar.slider("Number of Apps Installed", 1, 20, 6)
    loan_frequency_last_30_days = st.sidebar.slider("Loans in Last 30 Days", 0, 10, 3)
    repayment_ratio_overall = st.sidebar.slider("Repayment Ratio", 0.0, 1.0, 0.75)
    credit_limit_utilization = st.sidebar.slider("Credit Limit Utilization", 0.0, 1.0, 0.6)
    device_or_ID_shared = st.sidebar.checkbox("Device or ID Shared?")
    loan_amount = st.sidebar.number_input("Loan Amount", 100, 50000, 10000)
    interest_rate = st.sidebar.slider("Interest Rate (%)", 5.0, 30.0, 15.0)
    loan_grade = st.sidebar.selectbox("Loan Grade", ["A", "B", "C", "D", "E"])
    loan_term_days = st.sidebar.slider("Loan Term (Days)", 10, 365, 30)
    debt_to_income_ratio = st.sidebar.slider("Debt-to-Income Ratio", 0.0, 1.0, 0.4)
    delinquencies_last_2yrs = st.sidebar.slider("Delinquencies Last 2 Years", 0, 5, 1)
    public_records = st.sidebar.slider("Public Records", 0, 5, 0)
    revolving_utilization = st.sidebar.slider("Revolving Utilization", 0.0, 1.0, 0.7)
    total_credit_lines = st.sidebar.slider("Total Credit Lines", 1, 20, 5)
    is_default = st.sidebar.checkbox("Is Default?")

    data = {
        "age": age,
        "income": income,
        "employment_status": employment_status,
        "education_level": education_level,
        "region": region,
        "number_of_active_loans": number_of_active_loans,
        "apps_installed": apps_installed,
        "loan_frequency_last_30_days": loan_frequency_last_30_days,
        "repayment_ratio_overall": repayment_ratio_overall,
        "credit_limit_utilization": credit_limit_utilization,
        "device_or_ID_shared": device_or_ID_shared,
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "loan_grade": loan_grade,
        "loan_term_days": loan_term_days,
        "debt_to_income_ratio": debt_to_income_ratio,
        "delinquencies_last_2yrs": delinquencies_last_2yrs,
        "public_records": public_records,
        "revolving_utilization": revolving_utilization,
        "total_credit_lines": total_credit_lines,
        "is_default": is_default
    }

    return pd.DataFrame([data])

input_df = user_input_features()

# Display user input
st.subheader("User Input Parameters")
st.write(input_df)

# Align columns to what the preprocessor expects
expected_columns = preprocessor.feature_names_in_  # Columns expected by the preprocessor

# Reindex input_df so it has all expected columns (missing filled with 0 or False)
input_df_aligned = input_df.reindex(columns=expected_columns, fill_value=0)

# Convert boolean columns to int if necessary (e.g. device_or_ID_shared, is_default)
bool_cols = [col for col in expected_columns if input_df_aligned[col].dtype == 'bool']
for col in bool_cols:
    input_df_aligned[col] = input_df_aligned[col].astype(int)

# Preprocess input
try:
    input_processed = preprocessor.transform(input_df_aligned)

except Exception as e:
    st.error(f"Error in preprocessing: {str(e)}")
    st.stop()

# Predict
prediction = model.predict(input_processed)
predicted_class = int((prediction > 0.5).astype(int)[0][0])
confidence = float(prediction[0][0])

# Show result
st.subheader("Prediction")
if predicted_class == 1:
    st.error(f"🚨 Loan Stacking Detected! Confidence: {confidence:.2f}")
else:
    st.success(f"✅ Not Loan Stacking. Confidence: {1 - confidence:.2f}")
