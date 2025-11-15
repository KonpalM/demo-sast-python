from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)


API_KEY = "SUPER_SECRET_KEY_123"

def get_db_connection():
    conn = sqlite3.connect("users.db")
    return conn


@app.route("/user")
def get_user():
    user_id = request.args.get("id", "1")

    conn = get_db_connection()
    cur = conn.cursor()

    # Vulnerable query: user input directly concatenated
    query = "SELECT * FROM users WHERE id = " + user_id
    cur.execute(query)
    rows = cur.fetchall()

    name = request.args.get("name", "friend")
    return f"<h1>Hello {name}</h1><p>Rows: {rows}</p>"


@app.route("/log")
def read_log():
    file_name = request.args.get("file", "app.log")
    os.system("cat " + file_name)  # SonarQube should mark as risky

    return "OK"


def debug_print(msg):
    print("DEBUG:", msg)

if __name__ == "__main__":
    app.run(debug=True)
