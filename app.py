from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(_name_)

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT"))
}

def connect():
    return mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        port=db_config["port"],
        database="railway"
    )

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_feedback", methods=["GET", "POST"])
def add_feedback():
    if request.method == "POST":
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (user_name, message, rating) VALUES (%s, %s, %s)",
            (request.form["user_name"], request.form["message"], request.form["rating"])
        )
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add_feedback.html")


@app.route("/add_course", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO courses (course_name, duration) VALUES (%s, %s)",
            (request.form["course_name"], request.form["duration"])
        )
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add_course.html")


@app.route("/add_enrollment", methods=["GET", "POST"])
def add_enrollment():
    if request.method == "POST":
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
            (request.form["student_id"], request.form["course_id"])
        )
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add_enrollment.html")


if _name_ == "_main_":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)