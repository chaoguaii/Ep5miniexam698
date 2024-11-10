import pandas as pd
import streamlit as st
import pickle

# Load the trained pipeline
model_path = 'model_penguin_66130701711.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title("Penguin Species Predictor")

# รับข้อมูลจากผู้ใช้งาน
island = st.selectbox("Select Island", ["Torgersen", "Biscoe", "Dream"])
culmen_length = st.number_input("Culmen Length (mm)", min_value=0.0, step=0.1)
culmen_depth = st.number_input("Culmen Depth (mm)", min_value=0.0, step=0.1)
flipper_length = st.number_input("Flipper Length (mm)", min_value=0.0, step=0.1)
body_mass = st.number_input("Body Mass (g)", min_value=0.0, step=1.0)
sex = st.selectbox("Sex", ["MALE", "FEMALE"])

# Create input data
input_data = pd.DataFrame({
    'island': [island],
    'culmen_length_mm': [culmen_length],
    'culmen_depth_mm': [culmen_depth],
    'flipper_length_mm': [flipper_length],
    'body_mass_g': [body_mass],
    'sex': [sex]
})

if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        st.subheader(f"Predicted Species: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
