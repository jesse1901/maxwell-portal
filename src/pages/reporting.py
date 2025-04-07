import streamlit as st  
import streamlit.components.v1 as components    

st.set_page_config(
    page_title="reporting",
    layout="wide",
    initial_sidebar_state="expanded",
)
components.iframe("https://max-portal.desy.de/reporting", height=1200, scrolling=True)
