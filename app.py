import streamlit as st
st.title("BMI Calculator App")
weight=st.number_input("Enter your weight(in kg)")
height=st.number_input("Enter your height (in meters)")
if height > 0:
    bmi=weight / (height * height)
    st.write(f"Your BMI is:{bmi}")
