import streamlit as st
import os
import pandas as pd 
import streamlit.components.v1 as components
import pages as pg
from functions import charts, login
from streamlit_navigation_bar import st_navbar

st.set_page_config(
    page_title="Portal",
    layout="wide",
    initial_sidebar_state="collapsed",)

options = {
    "show_menu": True,
    "show_sidebar": False,
}

#login.authenticate()

pages = [
    st.Page("pages/home.py", title="Home", url_path="home"),
    st.Page("pages/reporting.py", title="Reporting", url_path="reporting"),
    st.Page("pages/reservations.py", title="Reservation", url_path="reservation"),
    st.Page("pages/webavial.py", title="Webavial", url_path="webavail"),
    st.Page("pages/webjobs.py", title="Webjobs", url_path="webjobs"),
]

# Only call this once in the whole app
page = st_navbar(pages, options=options, set_path=True)

if page:
    page.run()