import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("final_trained_model.pkl", "rb") as file:
    model = pickle.load(file)

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

# Country input (dropdown)
selected_country = st.selectbox("🌍 Country of Residence", list(country_mapping.keys()))
Country = country_mapping[selected_country]

# Other input fields
ML_Spend = st.slider("💸 Money Spent on ML/Cloud Services (Past 5 Years)", 0, 5, 2,
                     format="%d",
                     help="0 = $0, 1 = $1-99, 2 = $100-999, 3 = $1,000-9,999, 4 = $10,000-99,999, 5 = $100,000+")
Years_ML_Experience = st.slider("🧠 Years of Machine Learning Experience", 0, 5, 2,
                                format="%d",
                                help="0 = 0 years, 1 = <1 year, 2 = 1-2 years, 3 = 3-5 years, 4 = 5-10 years, 5 = 10+ years")
Company_Size = st.slider("🏢 Company Size", 0, 4, 2,
                         format="%d",
                         help="0 = 0-49, 1 = 50-249, 2 = 250-999, 3 = 1000-4999, 4 = 5000+ employees")
Age = st.slider("🎂 Your Age", 18, 70, 30)
Education_Level = st.slider("🎓 Highest Education Level", 0, 3, 1,
                             format="%d",
                             help="0 = Less than Bachelor's, 1 = Bachelor's, 2 = Master's, 3 = Doctoral")

# Prediction
if st.button("💵 Predict Salary"):
    # Build input DataFrame
    input_data = pd.DataFrame([{
        'Country': Country,
        'ML_Spend': ML_Spend,
        'Years_ML_Experience': Years_ML_Experience,
        'Company_Size': Company_Size,
        'Age': Age,
        'Education_Level': Education_Level
    }], columns=[
        'Country', 'ML_Spend', 'Years_ML_Experience', 'Company_Size', 'Age', 'Education_Level'
    ])

    # Make prediction
    predicted_salary = model.predict(input_data)[0]

    # Display result
    st.success(f"💰 Estimated Salary: **${predicted_salary:,.2f}**")

# Footer
st.markdown("---")
st.markdown(
    "<small>📘 Built with ❤️ using Streamlit — by your future data scientist!</small>",
    unsafe_allow_html=True
)
