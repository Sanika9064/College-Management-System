from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "12345"),
    "database": os.environ.get("DB_NAME")
}

def connect(db):
    return mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db
    )

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- FEEDBACK MODULE ----------------
@app.route("/add_feedback", methods=["GET", "POST"])
def add_feedback():
    if request.method == "POST":
        conn = connect("college_feedback_db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (user_name, message, rating) VALUES (%s, %s, %s)",
            (request.form["user_name"], request.form["message"], request.form["rating"])
        )
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add_feedback.html")


# ---------------- COURSE MODULE ----------------
@app.route("/add_course", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        conn = connect("college_courses_db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO courses (course_name, duration) VALUES (%s, %s)",
            (request.form["course_name"], request.form["duration"])
        )
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add_course.html")


# ---------------- ENROLLMENT MODULE ----------------
@app.route("/add_enrollment", methods=["GET", "POST"])
def add_enrollment():
    if request.method == "POST":
        conn = connect("college_enrollments_db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
            (request.form["student_id"], request.form["course_id"])
        )
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("add_enrollment.html")


if __name__ == "__main__":
    app.run(debug=True)