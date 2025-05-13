import streamlit as st
from modules.llm_model import get_model_response

def habitforge():
    st.subheader("🔨 HabitForge Coach")
    cue = st.text_input("Cue")
    craving = st.text_input("Craving")
    response = st.text_input("Response")
    reward = st.text_input("Reward")

    if st.button("Log Habit Loop"):
        st.success(f"Loop Saved: Cue: {cue}, Craving: {craving}, Response: {response}, Reward: {reward}")

        # Get suggestions using the LLM model
        messages = [
            {
                "role": "user",
                "content": f"Suggest improvements for this habit loop: Cue: {cue}, Craving: {craving}, Response: {response}, Reward: {reward}"
            }
        ]
        suggestion = get_model_response(messages)
        st.write("💡 Suggested Improvements:", suggestion)
