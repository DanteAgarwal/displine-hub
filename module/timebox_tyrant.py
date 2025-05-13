import time

import pyttsx3
import streamlit as st


def timebox_tyrant():
    st.subheader("⏰ Timebox Tyrant")
    task = st.text_input("What task are you doing?")
    minutes = st.slider("How long to work (minutes)?", 1, 120, 25)
    if st.button("Start Focus Session"):
        end_time = time.time() + minutes * 60
        engine = pyttsx3.init()
        st.success("Timer Started")
        while time.time() < end_time:
            time.sleep(10)
        engine.say("You better be working!")
        engine.runAndWait()
