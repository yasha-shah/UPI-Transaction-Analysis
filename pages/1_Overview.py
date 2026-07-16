import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, load_css

st.set_page_config(page_title='Overview | UPI Analysis', layout='wide', initial_sidebar_state='expanded')

load_css()
df = load_data()

df['volume_bil'] = df['volume_mil']/1000
df['value_l_cr'] = df['value_cr']/100000

st.title('Overview')

st.sidebar.header('Filters')
year = st.sidebar.multiselect('Select year', df['year'].unique())
if year:
    df = df[df['year'].isin(year)]

col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Volume', f'{df['volume_bil'].sum() :,.1f} Bn')
col2.metric('Total Value', f'₹{df['value_l_cr'].sum() :,.1f}L Cr')
col3.metric('Avg transaction value', f'₹{df['avg_txn'].mean() :,.0f}')
col4.metric('Banks using UPI', f'{df['banks_using_upi'].iloc[-1] :.0f}')
monthly_vol_chart = px.line(df, x='period', y='volume_bil', labels={'period': 'Month', 'volume_bil': 'Volume (Bn)'})
monthly_vol_chart.update_xaxes(title='')
monthly_vol_chart.update_yaxes(title='Volume (Bn)')
monthly_vol_chart.update_layout(
    title={
        'text': 'Monthly UPI transaction volume',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
monthly_vol_chart.update_traces(
    hovertemplate=
    '<b>%{x}</b><br>'
    'Volume: %{y:,.2f} Bn<br>'
    '<extra></extra>'
)

monthly_value_chart = px.line(df, x='period', y='value_l_cr', labels={'period': 'Month', 'value_l_cr': 'Value (L Cr INR)'})
monthly_value_chart.update_xaxes(title='')
monthly_value_chart.update_yaxes(title='Value (Lakh Cr INR)')
monthly_value_chart.update_layout(
    title={
        'text': 'Monthly UPI transaction value',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
monthly_value_chart.update_traces(
    hovertemplate=
    '<b>%{x}</b><br>'
    'Value: ₹%{y:,.2f}L Cr<br>'
    '<extra></extra>'
)

chart1, chart2 = st.columns(2)
chart1.plotly_chart(monthly_vol_chart, width='stretch')
chart2.plotly_chart(monthly_value_chart, width='stretch')
