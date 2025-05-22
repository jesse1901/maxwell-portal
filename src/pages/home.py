import streamlit as st  
import streamlit.components.v1 as components    
from figures import figures

if __name__ == "__main__":
    fig = figures()
    fig.efficiency_chart()

    col1, col2 = st.columns([1,1])

    with col1:
      fig.user_stats()
    with col2:
       fig.ampel()