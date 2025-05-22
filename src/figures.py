import streamlit as st
import sqlite3
import pandas as pd 
from datetime import datetime, timedelta, date
import pytz
import plotly.express as px

class figures():
    def __init__(self):
        self.conn = sqlite3.connect('max-reports-slurm.sqlite3')
        self.user = "sottocor" #st.experimental_user.preferred_username
        pass
    
    def this_month(self):
        today       = datetime.today()
        first_day   = today.replace(day=1).strftime("%Y-%m-%d")
        first_ts    = int(datetime.strptime(first_day, "%Y-%m-%d").timestamp())     # calculate first day of Month
        return first_ts
    
    def efficiency_chart(self):
        first_ts = self.this_month()
        
        query = f"SELECT JobID, CPUEff * 100 AS CPUEff, Start, End FROM allocations WHERE User = '{self.user}' AND End >= {first_ts}"       # if End after first day of month
    
        df = pd.read_sql(query, self.conn)
        
        if df.empty:
            st.error("Keine Daten verfügbar")
            return
        
        # Convert 'End' to datetime and set timezone to Berlin
        berlin_tz = pytz.timezone('Europe/Berlin')
        df['End'] = pd.to_datetime(df['End'], unit='s', errors='coerce').dt.tz_localize('UTC')      
        df['End'] = df['End'].dt.tz_convert(berlin_tz)
        df['End'] = df['End'].dt.strftime('%Y-%m-%d %H:%M:%S')
        st.header("Your Job-Efficiency this month")
        
        fig = px.line(
            df,
            x='End',
            y='CPUEff',
            hover_data={
                'JobID': True,
                'CPUEff': ':.2f',       # zwei Nachkommastellen
                'End': True
            }
        )
        #fig.update_traces(mode='lines+markers')  # Linien und Punkte

        st.plotly_chart(fig, use_container_width=True)


    def user_stats(self):

        # 1. Ersten Tag des Monats als String und Unix-Timestamp bestimmen
        first_ts = self.this_month()

        # 2. Query mit Timestamp-Filter (wenn End als Unix-Timestamp gespeichert ist)
        query = f"""
            SELECT
                ROUND((TotalCPU / CPUTime) * 100 ,2)   AS CPUEff,
                COUNT(JobID)  AS JobID,
                ROUND((CPUTime / 3600),2) AS total_CPU_hours,
                ROUND((CPUTime- TotalCPU)/3600,2) AS CPU_hours_lost,
                ROUND((TotalCPU / 3600),2) AS CPU_hours_used    
            FROM allocations
            WHERE
                User = '{self.user}'
                AND End >= {first_ts}
        """
        df = pd.read_sql(query, self.conn)

        # 3. Auf leeres Ergebnis prüfen
        if df.empty or pd.isna(df.loc[0, "CPUEff"]):
            st.error("Keine Daten verfügbar")
            return

        # 4. Werte als native Python-Typen extrahieren
        cpu_eff         = float(df.loc[0, "CPUEff"])
        job_cnt         = int(df.loc[0, "JobID"])
        total_hours     = float(df.loc[0, "total_CPU_hours"])
        hours_lost      = float(df.loc[0, "CPU_hours_lost"])
        hours_used      = float(df.loc[0, "CPU_hours_used"])

        st.header("Your Job-Statistics this month")
        c0,c1, c2, c3 = st.columns([1,2,2,6])
        #col1
        c1.metric("Job count this month",       f"{job_cnt}")
        c1.metric("Ø CPU-Efficiency",    f"{cpu_eff:.2f}")

        #col2
        c2.metric("Total CPU-Hours",  f"{total_hours:.2f}")
        c2.metric("CPU-Hours used", f"{hours_used:.2f}")
        c2.metric("CPU-Hours lost", f"{hours_lost:.2f}")

    
    def ampel(self):
        first_ts = self.this_month()
        query = f"""
            SELECT
                ROUND((TotalCPU / CPUTime),2) AS CPU_util    
            FROM allocations
            WHERE
                User = '{self.user}'
                AND End >= {first_ts}
        """
        
        df = pd.read_sql(query, self.conn)

        if df.empty or pd.isna(df.loc[0, "CPU_util"]):
            st.error("Keine Daten verfügbar")
            return
        
        cpu_util = float(df.loc[0, "CPU_util"])

        if cpu_util < 0.3:
            st.error("🚦Your CPU utilization is below 30%. This is considered inefficient.")
        elif cpu_util < 0.5:
            st.warning("🚦Your CPU utilization is between 30% and 50%. This is moderate.")
        else:
            st.success("🚦Your CPU utilization is above 50%. Great job!")