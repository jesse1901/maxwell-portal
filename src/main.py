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


#parent_dir = os.path.dirname(os.path.abspath(__file__))
#logo = os.path.join(parent_dir, "Desy_logo.svg")

pages = ["Home", "Reporting", "Reservations", "Webavail", "Webjobs"]

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