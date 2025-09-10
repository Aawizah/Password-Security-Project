from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def check_login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if check_login(username, password):
        return f"<h2>Welcome, {username}! (Weak system, insecure)</h2>"
    else:
        return "<h2>Login failed!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
