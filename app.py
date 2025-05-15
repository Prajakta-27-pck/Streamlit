import streamlit as st
from client import StockApi


# Create page title

st.set_page_config("Stock Market app")


# add title

st.title("Stock Market app")


# add subheading

st.subheader("By Prajakta Kante")


## add text box for serching company

company = st.text_input("Company Name")


## create function for making connection between stockapi class and app

@st.cache_resource(ttl= 3600)
def fetch_data():
    return StockApi()


## create function for getting symbol







