import streamlit as st  
import streamlit.components.v1 as components    
from functions import charts, login
from figures import figures

def show_home():
    #st.title("Home")
    st.title("HPC-Cluster Übersicht")
    f = figures()
    f.efficiency_chart()
    f.user_stats()

 #   charts.test_chart()
 #   data = charts.generate_user_stats()
 #   charts.show_dashboard(data)