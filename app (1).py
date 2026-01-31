import streamlit as st

st.title("Mera Pehla Streamlit App in Colab")
st.write("Hello! Ye Colab me Streamlit app hai.")

name = st.text_input("Apna naam likho:")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Apni age choose karo", 0, 100, 20)
st.write(f"Apki age: {age}")
