import streamlit as st  
import streamlit.components.v1 as components    


def show_webavail():
    components.iframe("https://max-portal.desy.de/webavail/", height=1200, scrolling=True)

show_webavail()