import logging
from typing import get_args
import streamlit as st
import requests
from src import constants

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

API_ENDPOINT = "http://127.0.0.1:8080/getnode"

def text_to_seq(user_input:str) -> str:
    output = ""
    try:
        payload = {
            "query": user_input
        }
        response = requests.post(API_ENDPOINT, json=payload, timeout=60)
        response_data = response.json()
        output=response_data["sequence"]
    except Exception as e:
        logger.exception("error occoured while calling translation service")
    return output

st.title("text to seq chat bot")
user_input = st.text_input("Type prompt to get possible sequence: ")

if st.button("Send"):
    if user_input:
        output = text_to_seq(user_input)
        # Display response
        st.write("Response:")
        for line in output.split('\n'):
            st.write(line)
    else:
        st.warning("Please enter a message before sending.")
    
# run streamlit app
# streamlit run main.py
# python3 -m streamlit run main.py