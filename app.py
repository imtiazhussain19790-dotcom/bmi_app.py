import streamlit as st
st.title("BMI Calculator App")
weight=st.number_input("Enter your weight(in kg)")
height=st.number_input("Enter your height (in meters)")
if height > 0:
    bmi=weight / (height * height)
    st.write(f"Your BMI is:{bmi}")
    if bmi < 18.5:
        st.warning ("(Underweight)")
    elif 18.5 <= bmi < 25:
        st.success("(Healthy)")
    elif 25 <= bmi < 30:
        st.info("(Overweight)")
    else:
        st.error("(Obesity)")
                                                    
