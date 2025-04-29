import streamlit as st
import sqlite3
import pandas as pd 


class figures():
    def __init__(self):
        self.conn = sqlite3.connect('max-reports-slurm.sqlite3')
        pass
    
    def efficiency_chart(self):
        user = st.experimental_user.preferred_username
        query = f"SELECT CPUEff, End FROM allocations WHERE User = {user}"
        df = pd.read_sql(query, self.conn)
        df['End'] = pd.to_datetime(df['End'])
        st.line_chart(df)