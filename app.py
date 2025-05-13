# # DisciplineHub: All-in-One Self-Discipline Platform (Streamlit + GPT-2)
# # Core Modules: Tracker, Timebox, HabitForge, Focus Mode, Accountability, Score API, Voice Journal

# # ======================
# # Required Libraries
# # ======================
# import streamlit as st
# import sqlite3
# import datetime
# import subprocess
# import os
# import time
# import pyttsx3
# import speech_recognition as sr
# from apscheduler.schedulers.background import BackgroundScheduler
# from transformers import pipeline

# # ======================
# # Init Section
# # ======================
# st.set_page_config(page_title="DisciplineHub", layout="wide")
# st.title("🧠 DisciplineHub – Master Your Mind")

# # DB setup
# conn = sqlite3.connect('disciplinehub.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY, name TEXT, status TEXT, date TEXT)''')
# c.execute('''CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY, goal TEXT, deadline TEXT, status TEXT)''')
# conn.commit()

# # ======================
# # GPT2-based Journaling
# # ======================
# def voice_journal():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("🎙 Speak now for your journal...")
#         audio = recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio)
#         st.success(f"Transcribed: {text}")
#         gpt = pipeline("text-generation", model="gpt2")
#         insight = gpt("Reflect on this: " + text, max_length=100)[0]['generated_text']
#         st.write("🧘 Self-Coaching Insight:", insight)
#     except Exception as e:
#         st.error(f"Error: {e}")

# # ======================
# # Habit Tracker
# # ======================
# def habit_tracker():
#     st.subheader("📊 Habit Tracker")
#     habit = st.text_input("Enter Habit")
#     if st.button("Add Habit"):
#         c.execute("INSERT INTO habits (name, status, date) VALUES (?, ?, ?)", (habit, 'Pending', datetime.date.today()))
#         conn.commit()
#     st.write("## Today's Habits")
#     for row in c.execute("SELECT * FROM habits WHERE date=?", (datetime.date.today().isoformat(),)):
#         id, name, status, date = row
#         if st.checkbox(name, value=(status=='Done')):
#             c.execute("UPDATE habits SET status='Done' WHERE id=?", (id,))
#             conn.commit()

# # ======================
# # Timebox Tyrant
# # ======================
# def timebox_tyrant():
#     st.subheader("⏰ Timebox Tyrant")
#     task = st.text_input("What task are you doing?")
#     minutes = st.slider("How long to work (minutes)?", 1, 120, 25)
#     if st.button("Start Focus Session"):
#         end_time = time.time() + minutes * 60
#         engine = pyttsx3.init()
#         st.success("Timer Started")
#         while time.time() < end_time:
#             time.sleep(10)
#         engine.say("You better be working!")
#         engine.runAndWait()

# # ======================
# # HabitForge
# # ======================
# def habitforge():
#     st.subheader("🔨 HabitForge Coach")
#     cue = st.text_input("Cue")
#     craving = st.text_input("Craving")
#     response = st.text_input("Response")
#     reward = st.text_input("Reward")
#     if st.button("Log Habit Loop"):
#         st.success(f"Loop Saved: Cue: {cue}, Craving: {craving}, Response: {response}, Reward: {reward}")

# # ======================
# # Focus Mode Launcher
# # ======================
# def focus_mode():
#     st.subheader("🚀 Focus Mode Launcher")
#     allowed = st.text_area("Allowed apps (comma-separated)").split(',')
#     if st.button("Launch Focus Mode"):
#         running = subprocess.check_output("tasklist", shell=True).decode()
#         for line in running.splitlines():
#             for app in allowed:
#                 if app.strip().lower() not in line.lower():
#                     os.system(f"taskkill /f /im {line.split()[0]}")
#         st.success("Non-allowed apps terminated.")

# # ======================
# # Accountability Bot
# # ======================
# def accountability_bot():
#     st.subheader("🤖 Accountability Buddy")
#     goal = st.text_input("Your Goal")
#     deadline = st.date_input("Deadline")
#     if st.button("Set Goal"):
#         c.execute("INSERT INTO goals (goal, deadline, status) VALUES (?, ?, ?)", (goal, str(deadline), 'Ongoing'))
#         conn.commit()
#     st.write("## Current Goals")
#     for row in c.execute("SELECT * FROM goals"):
#         id, g, d, s = row
#         st.write(f"📌 {g} - ⏳ {d} - Status: {s}")

# # ======================
# # Discipline Score API (Dummy for now)
# # ======================
# def discipline_score():
#     st.subheader("📈 Discipline Score")
#     habits_done = len([r for r in c.execute("SELECT * FROM habits WHERE status='Done'")])
#     goals_done = len([r for r in c.execute("SELECT * FROM goals WHERE status='Done'")])
#     score = habits_done * 10 + goals_done * 20
#     st.metric("Your Discipline Score", score)

# # ======================
# # Streamlit Tabs
# # ======================
# tabs = st.tabs(["Tracker", "Timebox", "HabitForge", "Focus Mode", "Accountability", "Score", "Voice Journal"])

# with tabs[0]: habit_tracker()
# with tabs[1]: timebox_tyrant()
# with tabs[2]: habitforge()
# with tabs[3]: focus_mode()
# with tabs[4]: accountability_bot()
# with tabs[5]: discipline_score()
# with tabs[6]: voice_journal()

# # ======================
# # Scheduler for future bot pings (optional)
# # ======================
# scheduler = BackgroundScheduler()
# def goal_check():
#     # Here you'd add notifications or logic
#     pass
# scheduler.add_job(goal_check, 'interval', minutes=30)
# scheduler.start()


import streamlit as st
from modules.home import home
from modules.habit_tracker import habit_tracker
from modules.timebox_tyrant import timebox_tyrant
from modules.habitforge import habitforge
from modules.focus_mode import focus_mode
from modules.accountability_bot import accountability_bot
from modules.discipline_score import discipline_score
from modules.voice_journal import voice_journal

# ======================
# Init Section
# ======================
st.set_page_config(page_title="DisciplineHub", layout="wide")  # 👈 FIRST thing on the page

st.title("🧠 DisciplineHub – Master Your Mind")

# ======================
# Streamlit Tabs
# ======================
tabs = st.tabs(["Home", "Tracker", "Timebox", "HabitForge", "Focus Mode", "Accountability", "Score", "Voice Journal"])

with tabs[0]: home()
with tabs[1]: habit_tracker()
with tabs[2]: timebox_tyrant()
with tabs[3]: habitforge()
with tabs[4]: focus_mode()
with tabs[5]: accountability_bot()
with tabs[6]: discipline_score()
with tabs[7]: voice_journal()
