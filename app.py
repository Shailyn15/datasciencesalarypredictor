import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("final_trained_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title for the app
st.title("Data Science Salary Predictor")

# Description
st.write("This web application predicts data scientist salaries based on your background. Please fill in the details below:")

# Input fields
Country = st.slider("1. Country Code (e.g., 0 = US, 1 = India, 2 = UK, etc.)", min_value=0, max_value=10, step=1)
ML_Spend = st.slider("2. How much money have you spent on ML/cloud computing services? [0 = $0, 1 = $1-99, 2 = $100-999, 3 = $1000-9999, 4 = $10,000-99,999, 5 = $100,000+]", min_value=0, max_value=5, step=1)
Years_ML_Experience = st.slider("3. Years of machine learning experience? [0 = 0 years, 1 = <1 year, 2 = 1-2 years, 3 = 3-5 years, 4 = 5-10 years, 5 = 10+ years]", min_value=0, max_value=5, step=1)
Company_Size = st.slider("4. Company size [0 = 0-49 employees, 1 = 50-249, 2 = 250-999, 3 = 1000-4999, 4 = 5000+]", min_value=0, max_value=4, step=1)
Age = st.slider("5. Your age", min_value=18, max_value=70, step=1)
Education_Level = st.slider("6. Education level [0 = Less than Bachelor's, 1 = Bachelor's, 2 = Master's, 3 = Doctoral]", min_value=0, max_value=3, step=1)

# Prediction
if st.button("Predict Salary"):
    input_data = pd.DataFrame({
        "Country": [Country],
        "ML_Spend": [ML_Spend],
        "Years_ML_Experience": [Years_ML_Experience],
        "Company_Size": [Company_Size],
        "Age": [Age],
        "Education_Level": [Education_Level]
    })

    # Predict
    predicted_salary = model.predict(input_data)[0]

    # Display
    st.subheader(f"Predicted Salary: ${predicted_salary:,.2f} per year")
