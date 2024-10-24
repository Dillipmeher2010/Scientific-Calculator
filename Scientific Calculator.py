import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator App")

# Input method selection
input_method = st.radio("Choose input method", ("Slider", "Number Input"))

# Conditional input fields based on the selected method
if input_method == "Slider":
    num1 = st.slider("Select the first number", min_value=-100, max_value=100, value=0)  # Adjust range as needed
    num2 = st.slider("Select the second number", min_value=-100, max_value=100, value=0)  # Adjust range as needed
else:  # Number Input
    num1 = st.number_input("Enter the first number", value=0)
    num2 = st.number_input("Enter the second number", value=0)

# Dropdown for operation selection
operation = st.selectbox("Choose the operation", (
    "Add", "Subtract", "Multiply", "Divide", 
    "Square Root (of first number)", "Exponentiation", 
    "Sine (in degrees)", "Cosine (in degrees)", "Tangent (in degrees)", 
    "Logarithm (base 10) of first number"
))

# Perform calculation based on user input
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result of {num1} * {num2} is: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of {num1} / {num2} is: {result}")
        else:
            st.error("Error: Division by zero is not allowed.")
    elif operation == "Square Root (of first number)":
        if num1 >= 0:
            result = math.sqrt(num1)
            st.success(f"The square root of {num1} is: {result}")
        else:
            st.error("Error: Cannot take the square root of a negative number.")
    elif operation == "Exponentiation":
        result = num1 ** num2
        st.success(f"{num1} raised to the power of {num2} is: {result}")
    elif operation == "Sine (in degrees)":
        result = math.sin(math.radians(num1))
        st.success(f"The sine of {num1} degrees is: {result}")
    elif operation == "Cosine (in degrees)":
        result = math.cos(math.radians(num1))
        st.success(f"The cosine of {num1} degrees is: {result}")
    elif operation == "Tangent (in degrees)":
        result = math.tan(math.radians(num1))
        st.success(f"The tangent of {num1} degrees is: {result}")
    elif operation == "Logarithm (base 10) of first number":
        if num1 > 0:
            result = math.log10(num1)
            st.success(f"The logarithm (base 10) of {num1} is: {result}")
        else:
            st.error("Error: Logarithm of non-positive numbers is undefined.")
