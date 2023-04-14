import streamlit as st

st.title("TDS Module 8 Assignment")

# take three number inputs
a = st.number_input("Enter first number: ")
b = st.number_input("Enter second number: ")
c = st.number_input("Enter third number: ")

# find the largest among the three numbers
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

st.write("The largest number among", a, ",", b, "and", c, "is:", largest)
