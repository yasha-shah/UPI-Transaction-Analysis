import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_css

st.set_page_config(page_title='UPI Trends Dashboard', layout='wide', initial_sidebar_state='expanded')

load_css()

st.title('UPI Transaction Trends (2016-2026)')

st.markdown("""
This project is an analysis of 10 years of UPI (Unified Payments Interface) transaction data collected from NPCI's (National Payments Corporation of India) public portal.  
Python is used for data cleaning, feature engineering, and exploratory data analysis.  
The goal of this project is to understand the growth of India's own digital payment system by transaction volume and value.  
""")

st.divider()

st.subheader('Pages')
st.markdown("""
- Overview: Total volume, value, KPI cards and trend charts
- Growth: Month-over-month and year-over-year growth analysis
- Insights: Avg transaction value, seasonality, banks using UPI
""")

st.divider()

st.subheader('Data source')
st.markdown("""
NPCI UPI Product Statistics: [ncpi.org.in](https://www.npci.org.in/product/upi/product-statistics)  
Period: August 2016-2026  
""")

with st.bottom:
    col1, col2, col3 = st.columns([8, 1, 1])
    col2.markdown('[GitHub](https://github.com/yasha-shah/)')
    col3.markdown('[LinkedIn](https://linkedin.com/in/shah-yasha)')