import streamlit as st
import sqlite3

def home():
    st.title("🏠 Home – DisciplineHub Overview")

    conn = sqlite3.connect('disciplinehub.db')
    c = conn.cursor()

    # Habit Tracker Data
    st.subheader("📊 Habit Tracker")
    habits_done = len([r for r in c.execute("SELECT * FROM habits WHERE status='Done'")])
    st.write(f"Habits completed today: {habits_done}")

    # Timebox Tyrant Data
    st.subheader("⏰ Timebox Tyrant")
    # You can add more detailed tracking here if needed

    # HabitForge Data
    st.subheader("🔨 HabitForge Coach")
    # You can add more detailed tracking here if needed

    # Focus Mode Data
    st.subheader("🚀 Focus Mode Launcher")
    # You can add more detailed tracking here if needed

    # Accountability Bot Data
    st.subheader("🤖 Accountability Buddy")
    goals_done = len([r for r in c.execute("SELECT * FROM goals WHERE status='Done'")])
    st.write(f"Goals completed: {goals_done}")

    # Discipline Score Data
    st.subheader("📈 Discipline Score")
    score = habits_done * 10 + goals_done * 20
    st.metric("Your Discipline Score", score)

    conn.close()
