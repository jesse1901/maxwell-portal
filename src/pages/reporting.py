import streamlit as st  
import streamlit.components.v1 as components    


def show_reporting():
    st.header("1")
    components.iframe("https://max-portal.desy.de/reporting?embed=true&embed_options=light_theme", height=1200, scrolling=True)
