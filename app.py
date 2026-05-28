from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# -------------------------
# LOGIN PAGE
# -------------------------
@app.route("/")
def login():
    return render_template("login.html")


@app.route("/", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        session["user"] = username
        return redirect("/dashboard")

    return redirect("/")


# -------------------------
# DASHBOARD
# -------------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    users_count = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        user=session["user"],
        users_count=users_count
    )


# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run()