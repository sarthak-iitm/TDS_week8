import streamlit as st
st.title("TDS Module 8 Assignment")
a = st.number_input("Enter first number: ")
b = st.number_input("Enter second number: ")
c = a + b
st.write("The sum of both numbers is:" , c) 
