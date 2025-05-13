import streamlit as st
import sqlite3
import pandas as pd 
from datetime import datetime, timedelta, date
import pytz


class figures():
    def __init__(self):
        self.conn = sqlite3.connect('max-reports-slurm.sqlite3')
        pass
    
    def efficiency_chart(self):
        #user = st.experimental_user.preferred_username
        user = "abekov"
        query = f"SELECT CPUEff * 100 AS CPUEff, End FROM allocations WHERE User = '{user}'"
        df = pd.read_sql(query, self.conn)
        
        if df.empty:
            st.error("Keine Daten verfügbar")
            return
        
        berlin_tz = pytz.timezone('Europe/Berlin')
        df['End'] = pd.to_datetime(df['End'], unit='s', errors='coerce').dt.tz_localize('UTC')
        df['End'] = df['End'].dt.tz_convert(berlin_tz)
        df['End'] = df['End'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df = df.set_index('End')
        st.line_chart(df)
    
    def user_stats(self):
        #user = st.experimental_user.preferred_username
        user = "abekov"
        query = f"SELECT AVG(CPUEff) AS CPUEff, COUNT(JobID) AS JobID FROM allocations WHERE User = '{user}' LIMIT 500"
        df = pd.read_sql(query, self.conn)
        
        if df.empty:
            st.error("Keine Daten verfügbar")
            return
                
        col1, col2 = st.columns(2)
        col1.metric("Ø CPU-Effizienz",  df['CPUEff'])
        col2.metric("Jobs insgesamt", df['JobID'])
        