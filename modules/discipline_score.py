import streamlit as st

from modules.db import c


def discipline_score():
    st.subheader("📈 Discipline Score")
    habits_done = len(
        [r for r in c.execute("SELECT * FROM habits WHERE status='Done'")]
    )
    goals_done = len([r for r in c.execute("SELECT * FROM goals WHERE status='Done'")])
    score = habits_done * 10 + goals_done * 20
    st.metric("Your Discipline Score", score)
