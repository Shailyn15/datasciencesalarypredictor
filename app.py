import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("final_trained_model.pkl", "rb") as file:
    model = pickle.load(file)

# OPTIONAL: Print the model's expected features
st.write("Expected columns:", model.feature_names_in_)

# Title
st.title("Data Science Salary Predictor")

# Description
st.write("This web application predicts data scientist salaries based on your background. Please fill in the details below:")

# Define country mapping
country_mapping = {
    "United States": 0,
    "India": 1,
    "United Kingdom": 2,
    "Canada": 3,
    "Spain": 4,
    "Germany": 5,
    "France": 6,
    "Australia": 7,
    "China": 8,
    "Brazil": 9,
    "Other": 10
}

# User selects country
selected_country = st.selectbox("🌍 Country of Residence", list(country_mapping.keys()))
Country = country_mapping[selected_country]

# Other inputs
ML_Spend = st.slider("💸 Money Spent on ML/Cloud Services (Past 5 Years)", 0, 5, 2)
Years_of_ML_Experience = st.slider("🧠 Years of Machine Learning Experience", 0, 5, 2)  # <-- updated name
Company_Size = st.slider("🏢 Company Size", 0, 4, 2)
Age = st.slider("🎂 Your Age", 18, 70, 30)
Education_Level = st.slider("🎓 Highest Education Level", 0, 3, 1)

# Prediction
if st.button("💵 Predict Salary"):
    # Build dictionary with user's inputs
    features = {
        'Country': Country,
        'ML_Spend': ML_Spend,
        'Years_of_ML_Experience': Years_of_ML_Experience,  # <-- updated key
        'Company_Size': Company_Size,
        'Age': Age,
        'Education_Level': Education_Level
    }
    
    # Create DataFrame
    input_data = pd.DataFrame([features])

    # Reorder columns exactly to match what the model expects
    expected_columns = list(model.feature_names_in_)
    input_data = input_data[expected_columns]

    # Predict
    predicted_salary = model.predict(input_data)[0]

    # Display
    st.success(f"💰 Estimated Salary: **${predicted_salary:,.2f}**")

# Footer
st.markdown("---")
st.markdown(
    "<small>📘 Built with ❤️ using Streamlit — by your future data scientist!</small>",
    unsafe_allow_html=True
)
