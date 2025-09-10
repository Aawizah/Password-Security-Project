import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Insert demo user (weak: password in plain text)
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("alice", "password123"))

conn.commit()
conn.close()

print("Database initialized with user: alice / password123")
