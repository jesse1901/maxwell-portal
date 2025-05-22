import streamlit as st  
import streamlit.components.v1 as components    


def show_reporting():
    components.iframe("https://max-portal.desy.de/reporting?embed=true&embed_options=light_theme", height=1200, scrolling=True)



if __name__ == "__main__":
    show_reporting()