import streamlit as st
import pandas as pd 
import streamlit.components.v1 as components
import pages as pg
from functions import charts, login
from streamlit_navigation_bar import st_navbar


st.set_page_config(
    page_title="Portal",
    layout="wide",
    initial_sidebar_state="collapsed",)

pages = ["Home","Reporting", "Reservations", "Webavail", "Webjobs"]

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(pages, options=options)

functions = {
    "Home": pg.show_home,
    "Reporting": pg.show_reporting,
    "Reservations": pg.show_reservations,
    "Webavail": pg.show_webavail,
    "Webjobs": pg.show_webjobs,
}

go_to = functions.get(page)
if go_to:
    go_to()