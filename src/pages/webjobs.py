import streamlit as st  
import streamlit.components.v1 as components    


def show_webjobs():
    components.iframe("https://max-portal.desy.de/webjobs/", height=1200, scrolling=True)


show_webjobs()