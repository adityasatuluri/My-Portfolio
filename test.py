import streamlit as st

from rag_llama import ragLlama

st.set_page_config(page_title="Aditya Satuluri", layout="wide")

st.write(ragLlama())