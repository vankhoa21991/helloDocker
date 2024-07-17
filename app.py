import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

if st.button('Say hello'):
    st.write('Hello, World!')