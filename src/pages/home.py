import streamlit as st  
import streamlit.components.v1 as components    
from functions import charts, login
from figures import figures

def card(title, descr, link):
    st.markdown(f"""
    <a href="{link}" style="text-decoration: none; color: inherit;">
      <div class="card">
        <h3>{title}</h3>
        <p>{descr}</p>
      </div>
    </a>
    """, unsafe_allow_html=True)

def show_home():
    st.markdown("""
    <style>
    .card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    transition: box-shadow .2s;
    cursor: pointer;
    }
    .card:hover {
    box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

#    col1, col2 = st.columns(2)
#    with col1:
#        card("Dokumentation", "Öffne die Docs", "pages/reporting.py")
#    with col2:
#        card("Analytics", "Zu deinen Statistiken", "https://example.com/stats")

    st.title("HPC-Cluster Übersicht")
    f = figures()
    f.efficiency_chart()
    f.user_stats()


show_home()