import sqlite3

conn = sqlite3.connect("disciplinehub.db", check_same_thread=False)
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY, name TEXT, status TEXT, date TEXT)"""
)
c.execute(
    """CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY, goal TEXT, deadline TEXT, status TEXT)"""
)
conn.commit()
