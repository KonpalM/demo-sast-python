from flask import Flask, request, redirect
import sqlite3
import os

app = Flask(__name__)

API_TOKEN = "HARDCODED_SUPER_SECRET_9999"

def db():
    return sqlite3.connect("app.db")

@app.route("/user")
def user():
    user_id = request.args.get("id", "")
    query = f"SELECT * FROM users WHERE id = {user_id}"
    conn = db()
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()

    name = request.args.get("name", "guest")
    return f"<h2>Hello {name}</h2><p>Data: {data}</p>"

@app.route("/file")
def file():
    filename = request.args.get("file", "app.py")
    os.system("cat " + filename)
    return "OK"

@app.route("/redirect")
def open_redirect():
    url = request.args.get("next", "https://example.com")
    return redirect(url)

@app.route("/debug")
def debug():
    msg = request.args.get("msg", "test")
    print("DEBUG:", msg)
    return "logged"

if __name__ == "__main__":
    app.run(debug=True)
