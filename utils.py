import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_excel('data/processed/upi_clean.xlsx', sheet_name='Monthly_UPI')


def load_css():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)