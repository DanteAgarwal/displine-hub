import streamlit as st
import speech_recognition as sr
from modules.llm_model import get_model_response

def voice_journal():
    st.subheader("🎙 Voice Journal")
    recognizer = sr.Recognizer()

    # Use a pre-recorded audio file for testing
    audio_file_path = "path_to_your_audio_file.wav"  # Replace with the path to your audio file
    with sr.AudioFile(audio_file_path) as source:
        st.info("🎙 Using pre-recorded audio for testing...")
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"Transcribed: {text}")

        # Get insights using the LLM model
        messages = [
            {
                "role": "user",
                "content": f"Reflect on this: {text}"
            }
        ]
        insight = get_model_response(messages)
        st.write("🧘 Self-Coaching Insight:", insight)
    except Exception as e:
        st.error(f"Error: {e}")
