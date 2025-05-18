import streamlit as st
import requests

# streamlit run text2sql2/UI/streamlit/frontend.py

st.title("FastAPI + Streamlit Hello App")

text_input = st.text_input("Enter some text:")

if st.button("Submit"):
    if text_input:
        response = requests.post(
            "http://localhost:8000/hello",
            json={"text": text_input}
        )
        if response.status_code == 200:
            st.success(f"Response: {response.json()['message']}")
        else:
            st.error("Something went wrong")
    else:
        st.warning("Please enter some text")

