import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect("tasks.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    conn = get_db_connection()
    tasks = conn.execute(
        "SELECT id, title, completed FROM tasks"
    ).fetchall()
    conn.close()

    return render_template("index.html", tasks = tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()

    if title:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,)
        )    
        conn.commit()
        conn.close()
    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    conn = get_db_connection()

    task = conn.execute(
        "SELECT id FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()

    if task is None:
        conn.close()
        return "Task is not found", 404

    conn.execute(
        "DELETE FROM tasks WHERE id = ?", (task_id,)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("home"))



@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    new_title = request.form.get("title", "").strip()

    if not new_title:
        return "Task title cannot be empty", 400

    conn = get_db_connection()

    task = conn.execute(
        "SELECT id FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()

    if task is None:
        conn.close()
        return "Task not found", 404

    conn.execute(
        "UPDATE tasks SET title = ? WHERE id = ?",
        (new_title, task_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    conn = get_db_connection()

    task = conn.execute(
        "SELECT id FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()

    if task is None:
        conn.close()
        return "Task not found", 404

    conn.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)    


