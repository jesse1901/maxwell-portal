import streamlit as st
import pandas as pd 
import streamlit.components.v1 as components
from functions import charts, login

st.set_page_config(
    page_title="Portal",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title("Zentrales Web-Portal")
 
charts.test_chart()
data = charts.generate_user_stats()
charts.show_dashboard(data)


# Beispiel-Webseiten einbett