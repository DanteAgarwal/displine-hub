import streamlit as st

from modules.db import c, conn


def accountability_bot():
    st.subheader("🤖 Accountability Buddy")
    goal = st.text_input("Your Goal")
    deadline = st.date_input("Deadline")
    if st.button("Set Goal"):
        c.execute(
            "INSERT INTO goals (goal, deadline, status) VALUES (?, ?, ?)",
            (goal, str(deadline), "Ongoing"),
        )
        conn.commit()
    st.write("## Current Goals")
    for row in c.execute("SELECT * FROM goals"):
        id, g, d, s = row
        st.write(f"📌 {g} - ⏳ {d} - Status: {s}")
