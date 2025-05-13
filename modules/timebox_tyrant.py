import streamlit as st
import time
import pyttsx3
from multiprocessing import Process

def timebox_tyrant():
    st.subheader("⏰ Timebox Tyrant")
    task = st.text_input("What task are you doing?")
    minutes = st.slider("How long to work (minutes)?", 1, 120, 25)
    if st.button("Start Focus Session"):
        def timer(minutes):
            end_time = time.time() + minutes * 60
            engine = pyttsx3.init()
            st.success("Timer Started")
            while time.time() < end_time:
                time.sleep(10)
            engine.say("You better be working!")
            engine.runAndWait()

        p = Process(target=timer, args=(minutes,))
        p.start()
