import streamlit as st
from client import StockApi


# Create page title

st.set_page_config(page_title="Stock Market app", layout='wide')


# add title for page

st.title("Stock Market app")


# add subheading

st.subheader("By Prajakta Kante")


## add text box for serching company

company = st.text_input("Company Name")


## create function for making connection between stockapi class and app

@st.cache_resource(ttl= 3600)
def fetch_data():
    return StockApi(api_key=st.secrets["API_KEY"])


Stock_api = fetch_data()

## create function for getting symbol

@st.cache_data(ttl= 3600)
def get_symbol(company):
    symbol = Stock_api.search_symbol(company)
    return symbol

@st.cache_data(ttl=3600)
def plot_chart(symbol):
    df = Stock_api.time_series_daily_data(symbol)
    fig = Stock_api.plot_graph(df)
    return fig

if company:

    company_data = get_symbol(company)

    symbols = st.selectbox(company_data)








