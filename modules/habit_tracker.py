# modules/habit_tracker.py
# import time
# import datetime
# from modules.db import c, conn
# import streamlit as st

# def habit_tracker_main(shared_data):
#     while True:
#         today = datetime.date.today().isoformat()
#         c.execute("SELECT COUNT(*) FROM habits WHERE date=? AND status='Done'", (today,))
#         shared_data["habits_done"] = c.fetchone()[0]
#         time.sleep(5)  # Polling every 5 seconds

# def habit_tracker_ui():
#     st.subheader("📊 Habit Tracker (Full View)")
#     # Existing Streamlit input logic here...
# import datetime

# import streamlit as st

# from modules.db import c, conn


# def habit_tracker():
#     st.subheader("📊 Habit Tracker")
#     habit = st.text_input("Enter Habit")
#     if st.button("Add Habit"):
#         c.execute(
#             "INSERT INTO habits (name, status, date) VALUES (?, ?, ?)",
#             (habit, "Pending", datetime.date.today()),
#         )
#         conn.commit()
#     st.write("## Today's Habits")
#     for row in c.execute(
#         "SELECT * FROM habits WHERE date=?", (datetime.date.today().isoformat(),)
#     ):
#         id, name, status, date = row
#         if st.checkbox(name, value=(status == "Done")):
#             c.execute("UPDATE habits SET status='Done' WHERE id=?", (id,))
#             conn.commit()
import streamlit as st
import sqlite3
import datetime

def habit_tracker():
    st.subheader("📊 Habit Tracker")
    conn = sqlite3.connect('disciplinehub.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY, name TEXT, status TEXT, date TEXT)''')
    conn.commit()

    habit = st.text_input("Enter Habit")
    if st.button("Add Habit"):
        c.execute("INSERT INTO habits (name, status, date) VALUES (?, ?, ?)", (habit, 'Pending', datetime.date.today()))
        conn.commit()
    st.write("## Today's Habits")
    for row in c.execute("SELECT * FROM habits WHERE date=?", (datetime.date.today().isoformat(),)):
        id, name, status, date = row
        if st.checkbox(name, value=(status=='Done')):
            c.execute("UPDATE habits SET status='Done' WHERE id=?", (id,))
            conn.commit()
    conn.close()
