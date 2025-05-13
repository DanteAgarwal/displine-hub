import streamlit as st


def habitforge():
    st.subheader("🔨 HabitForge Coach")
    cue = st.text_input("Cue")
    craving = st.text_input("Craving")
    response = st.text_input("Response")
    reward = st.text_input("Reward")
    if st.button("Log Habit Loop"):
        st.success(
            f"Loop Saved: Cue: {cue}, Craving: {craving}, Response: {response}, Reward: {reward}"
        )
