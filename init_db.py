import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Example data
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
               ("admin", "1234"))

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
               ("ahmad", "1111"))

conn.commit()
conn.close()

print("DB Ready")