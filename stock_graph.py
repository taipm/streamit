from Stocks import get_stock_data_from_api
import streamlit as st
import pandas as pd
import numpy as np

st.title('Stock graph')

stock = "HPG"

data = get_stock_data_from_api(stock)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data['Volume'], bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
st.line_chart(data['Close'])