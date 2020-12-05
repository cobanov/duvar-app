import datetime
from flask import Flask, render_template, request
import database
import os


app = Flask(__name__)

database.create_tables()
token = os.getenv("password")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            entry_content = request.form.get("message")
            current_time = datetime.datetime.today() + datetime.timedelta(hours=3)
            database.create_entry(
                entry_content, current_time.strftime("%m.%d.%Y, %H:%M"))
        except Exception as e:
            pass

    return render_template("home.html", entries=database.retrieve_entries())


@app.route("/wipe", methods=["GET", "POST"])
def wipe():
    if request.method == "POST":
        password = request.form.get("password")
        if password == token:
            database.clear_database()
            return render_template("home.html", entries=database.retrieve_entries())

    return render_template("wipe.html")


@app.route("/upvote/<message_id>", methods=["GET", "POST"])
def upvote(message_id):
    database.upvote(message_id)
    return render_template("succes.html")


@app.route("/top", methods=["GET", "POST"])
def top():
    if request.method == "POST":
        try:
            entry_content = request.form.get("message")
            current_time = datetime.datetime.today() + datetime.timedelta(hours=3)
            database.create_entry(
                entry_content, current_time.strftime("%m.%d.%Y, %H:%M"))
        except Exception as e:
            pass

    return render_template("home.html", entries=database.retrieve_entries_top())


@app.route("/rules")
def rules():
    return render_template("rules.html")
