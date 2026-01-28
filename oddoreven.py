import streamlit as st
st.title("Basic logic web page")
st.write("Simple streamlit web app for beginners")
name = st.text_input("Enter your name", "Type here...")
number = st.number_input("Enter a number", step=1)

if st.button("Check"):
    st.info