import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class login:

    def __init__():
        pass

    def authenticate():
        if not st.experimental_user.is_logged_in:
            if st.button("Log in with Keycloak"):
                st.login()
            st.stop()
        #else:
        #    st.logout()


class charts:

    def __init__(self):
        pass

    def test_chart():
        st.subheader("Maxwell Efficiency")

        # Dummy-Daten generieren
        daten = pd.DataFrame({
            'x': np.arange(1, 11),
            'y': np.random.randint(10, 100, size=10)
        })
        st.line_chart(daten.set_index('x'))

    def generate_user_stats():
        np.random.seed(42)
        user = ["alice", "bob", "carla", "daniel"]
        stats = {
            "username": user,
            "cpu_efficiency_%": np.random.randint(60, 100, size=4),
            "gpu_efficiency_%": np.random.randint(40, 100, size=4),
            "jobs_completed": np.random.randint(10, 100, size=4),
            "lost_cpu_time_h": np.round(np.random.uniform(1, 10, size=4), 2),
            "lost_gpu_time_h": np.round(np.random.uniform(0.5, 8, size=4), 2),
            "running_jobs": np.random.randint(0, 10, size=4),
            "total_runtime_h": np.round(np.random.uniform(20, 200, size=4), 1),
        }

        return pd.DataFrame(stats)  
    
    def show_dashboard(df):
        if df is None or df.empty:
            st.error("Keine Daten verfügbar.")
            return

        st.title("HPC-Cluster Übersicht")

        col1, col2, col3 = st.columns(3)
        col1.metric("Ø CPU-Effizienz", f"{df['cpu_efficiency_%'].mean():.1f}%")
        col2.metric("Jobs insgesamt", df['jobs_completed'].sum())
        col3.metric("Laufende Jobs", df['running_jobs'].sum())

        st.subheader("Nutzer-Statistiken")
        st.dataframe(df, use_container_width=True)

        # st.subheader("Verlorene CPU-Zeit nach Nutzer")
        # fig1, ax1 = plt.subplots()
        # ax1.bar(df["username"], df["lost_cpu_time_h"])
        # ax1.set_ylabel("Verlorene CPU-Zeit (h)")
        # ax1.set_title("CPU Ineffizienz")
        # st.pyplot(fig1)

        # st.subheader("GPU-Effizienz (%)")
        # fig2, ax2 = plt.subplots()
        # ax2.bar(df["username"], df["gpu_efficiency_%"], color='orange')
        # ax2.set_ylabel("Effizienz (%)")
        #st.pyplot(fig2)

