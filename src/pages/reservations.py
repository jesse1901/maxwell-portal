import streamlit as st  
import streamlit.components.v1 as components    

st.set_page_config(
    page_title="reservations",
    layout="wide",
    initial_sidebar_state="expanded",
)
components.iframe("https://max-portal.desy.de/reservation/", height=1200,   scrolling=True)
