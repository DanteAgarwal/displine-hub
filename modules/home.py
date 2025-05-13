import streamlit as st
import sqlite3
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.badges import badge

def home():
    
    # Page Header
    st.markdown("## 🏠 Welcome to **DisciplineHub** – Your Control Center")
    st.markdown("Track your grind, measure your progress, and stay accountable. Let’s get it. 💪")

    conn = sqlite3.connect('disciplinehub.db')
    c = conn.cursor()

    # ========== HABITS ========== #
    c.execute("SELECT * FROM habits WHERE status='Done'")
    habits_done = len(c.fetchall())

    # ========== GOALS ========== #
    c.execute("SELECT * FROM goals WHERE status='Done'")
    goals_done = len(c.fetchall())

    # ========== DISCIPLINE SCORE ========== #
    discipline_score = habits_done * 10 + goals_done * 20

    # ========== METRIC CARDS ========== #
    st.markdown("### 📊 Your Daily Discipline Snapshot")
    col1, col2, col3 = st.columns(3)
    col1.metric("✅ Habits Done", habits_done, f"{habits_done * 10} pts")
    col2.metric("🎯 Goals Crushed", goals_done, f"{goals_done * 20} pts")
    col3.metric("🔥 Discipline Score", discipline_score)

    style_metric_cards(
        background_color="#f0f2f6",
        border_color="#e0e0e0",
        border_left_color="#4CAF50",
        border_size_px=2,
        box_shadow=True
    )

    st.divider()

    # ========== MODULE PREVIEWS ========== #
    st.markdown("### 🚀 Module Activity Overview")

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("⏰ Timebox Tyrant")
            st.info("Track your time-blocked sessions and maintain your calendar discipline.")
            badge(type="github", name="Timeboxing Docs")
            st.progress(0.5, text="2/4 sessions completed")

        with col2:
            st.subheader("🔨 HabitForge Coach")
            st.success("2 new habits added this week.")
            st.caption("Custom routines shaping your future discipline.")

        with col3:
            st.subheader("🚀 Focus Mode Launcher")
            st.warning("Focus mode used only 1 time today.")
            st.caption("Activate this to kill distractions and get in the zone.")

    st.divider()

    # ========== ACCOUNTABILITY ========== #
    st.markdown("### 🤖 Accountability Buddy")
    with stylable_container(
        key="accountability-box",
        css_styles="""
            {
                background-color: #fff8e1;
                border: 1px solid #fdd835;
                padding: 1rem;
                border-radius: 12px;
            }
        """
    ):
        st.markdown("**You're doing well!** Keep smashing those goals. 💥")
        st.markdown(f"**Total Goals Completed:** `{goals_done}`")

    conn.close()
