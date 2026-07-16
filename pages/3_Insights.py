import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, load_css

st.set_page_config(page_title='Insights | UPI Analysis', layout='wide', initial_sidebar_state='expanded')

load_css()
df = load_data()
df = df[df['period'] >= '01-01-2018']

df['volume_bil'] = df['volume_mil']/1000

st.title('Insights')

avg_txn_value_chart = px.line(df, x='period', y='avg_txn', labels={'period': 'Month', 'avg_txn': 'Avg transaction value (INR)'})
avg_txn_value_chart.update_xaxes(title='')
avg_txn_value_chart.update_yaxes(title='Avg transaction value (INR)')
avg_txn_value_chart.update_layout(
    title={
        'text': 'Average UPI transaction value (2018 onwards)',
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
avg_txn_value_chart.update_traces(
    hovertemplate=
    '<b>%{x}</b><br>'
    'Value: ₹%{y:,.2f}<br>'
    '<extra></extra>',
)
st.plotly_chart(avg_txn_value_chart, width='stretch')

seasonal = df.groupby(['month_num', 'month_name']).agg(avg_volume=('volume_bil', 'mean')).reset_index()

avg_txn_vol_chart = px.bar(seasonal, x='month_name', y='avg_volume', labels={'month_name': 'Month', 'avg_volume': 'Average volume (Bn)'}, text_auto='.2f', )
avg_txn_vol_chart.update_xaxes(title='')
avg_txn_vol_chart.update_yaxes(title='Average volume (Bn)')
avg_txn_vol_chart.update_layout(
    title={
        'text': 'Average monthly transaction volume (2018 onwards)',
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
avg_txn_vol_chart.update_traces(
    hovertemplate=
    '<b>%{x}</b><br>'
    'Volume: %{y:,.2f} Bn<br>'
    '<extra></extra>',
    textposition='outside',
    textfont={
        'size': 14
        }
)

banks_using_upi_chart = px.line(df, x='period', y='banks_using_upi', labels={'period': 'Month', 'banks_using_upi': 'No. of banks using UPI'})
banks_using_upi_chart.update_xaxes(title='')
banks_using_upi_chart.update_yaxes(title='No. of banks')
banks_using_upi_chart.update_layout(
    title={
        'text': 'No. of banks on UPI (2016 onwards)',
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
banks_using_upi_chart.update_traces(
    hovertemplate=
    '<b>%{x}</b><br>'
    'Banks using UPI: %{y}<br>'
    '<extra></extra>',
)


col1, col2 = st.columns(2)
col1.plotly_chart(avg_txn_vol_chart, width='stretch')    
col2.plotly_chart(banks_using_upi_chart, width='stretch')    