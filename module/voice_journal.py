import speech_recognition as sr
import streamlit as st

from transformers import pipeline


def voice_journal():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙 Speak now for your journal...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        st.success(f"Transcribed: {text}")
        gpt = pipeline("text-generation", model="gpt2")
        insight = gpt("Reflect on this: " + text, max_length=100)[0]["generated_text"]
        st.write("🧘 Self-Coaching Insight:", insight)
    except Exception as e:
        st.error(f"Error: {e}")
