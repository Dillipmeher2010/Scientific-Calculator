import streamlit as st
import numpy as np

# Title of the application
st.title("Scientific Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Dropdown for operations
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Power", "Sine", "Cosine", "Tangent"])

# Calculation based on the selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    result = num1 / num2 if num2 != 0 else "Error! Division by zero."
elif operation == "Square Root":
    result = np.sqrt(num1)
elif operation == "Power":
    result = np.power(num1, num2)
elif operation == "Sine":
    result = np.sin(np.radians(num1))
elif operation == "Cosine":
    result = np.cos(np.radians(num1))
elif operation == "Tangent":
    result = np.tan(np.radians(num1))

# Displaying the result
st.write("Result:", result)
