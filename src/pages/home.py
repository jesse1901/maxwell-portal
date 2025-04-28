import streamlit as st  
import streamlit.components.v1 as components    
from functions import charts, login

def show_home():
    #st.title("Home")
    
    charts.test_chart()
    data = charts.generate_user_stats()
    charts.show_dashboard(data)