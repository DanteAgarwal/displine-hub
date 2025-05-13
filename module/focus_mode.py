import os
import subprocess

import streamlit as st


def focus_mode():
    st.subheader("🚀 Focus Mode Launcher")
    allowed = st.text_area("Allowed apps (comma-separated)").split(",")
    if st.button("Launch Focus Mode"):
        running = subprocess.check_output("tasklist", shell=True).decode()
        for line in running.splitlines():
            for app in allowed:
                if app.strip().lower() not in line.lower():
                    os.system(f"taskkill /f /im {line.split()[0]}")
        st.success("Non-allowed apps terminated.")
