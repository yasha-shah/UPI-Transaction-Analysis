import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, load_css

st.set_page_config(page_title='Growth | UPI Analysis', layout='wide', initial_sidebar_state='expanded')

load_css()
df = load_data()
df = df[df['period'] >= '01-01-2018']
st.title('Growth')

st.sidebar.header('Filters')
fy = st.sidebar.multiselect('Select financial year', df['fy'].unique())
if fy:
    df = df[df['fy'].isin(fy)]

df_mom = df
mom_growth_chart = px.bar(df_mom, x='period', y=['volume_growth_mom', 'value_growth_mom'], barmode='group', labels={'period': 'Month', 'value':'Growth %'})
mom_growth_chart.update_xaxes(title='')
mom_growth_chart.update_yaxes(title='Growth %')
mom_growth_chart.update_layout(
    title={
        'text': 'Growth % Month-over-Month (2018 onwards)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 24
        }
    },
    legend_title='',
    margin={
        'l':40,
        'r':40,
        't':80,
        'b':40
    },
    plot_bgcolor='#1b1b1b',
    paper_bgcolor='#1b1b1b'
)
mom_growth_chart.for_each_trace(lambda t: t.update(name=t.name.replace('volume_growth_mom', 'Volume Growth').replace('value_growth_mom', 'Value Growth')))
mom_growth_chart.update_traces(
    hovertemplate=
    '<b>%{x}</b><br>'
    '%{fullData.name}: %{y:.2f}%<extra></extra>'
)
st.plotly_chart(mom_growth_chart, width='stretch')

df_yoy = df[df['period'] >= '01-01-2019']
yoy_growth_chart = px.line(df_yoy, x='period', y='volume_growth_yoy', labels={'period': 'Month', 'volume_growth_yoy': 'Growth %'})
yoy_growth_chart.update_xaxes(title='')
yoy_growth_chart.update_yaxes(title='Growth %', rangemode='tozero')
yoy_growth_chart.update_layout(
    title={
        'text': 'Growth % Month-over-Month (2019 onwards)',
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
yoy_growth_chart.update_traces(
    hovertemplate=
    '<b>%{x}</b><br>'
    'Growth: %{y:,.2f} %<br>'
    '<extra></extra>'
)
st.plotly_chart(yoy_growth_chart, width='stretch')
