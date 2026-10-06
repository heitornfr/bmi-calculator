import streamlit as st

st.title("BMI Calculator")
st.write("Calculate your Body Mass Index")

weight = st.number_input(
    "Weight (Kg)",
    min_value=1.0,
    max_value=500.0,
    value=None,
    step=0.1,
    placeholder="Enter your weight"
)

height = st.number_input(
    "Height (m)",
    min_value=0.5,
    max_value=2.5,
    value=None,
    step=0.01,
    placeholder="Enter your height"
)

gender = st.radio(
    "Gender",
    ["Man", "Woman"],
    horizontal=True
)

if st.button("Calculate BMI"):
    if weight is None or height is None:
        st.warning("Please enter your weight and height.")
    else:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            st.write("You are underweight.")
        elif bmi < 25:
            st.write("Your weight is normal.")
        elif bmi < 30:
            st.write("You are overweight.")
        elif bmi < 35:
            st.write("Class 1 obesity.")
        elif bmi < 40:
            st.write("Class 2 obesity.")
        else:
            st.write("Morbid obesity.")
