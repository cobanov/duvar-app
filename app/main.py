import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import database
import os
import pytz


app = Flask(__name__)

database.create_tables()
# token = os.getenv("password") # If you are deploying the project on PaaS like heroku or
# if you don't want to push your password to GitHub you
# should pass a password as environmental variable.

token = "password"
app.secret_key = "./]asd}vcbOH."


@app.route("/main", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            entry_content = request.form.get("message")
            current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
            database.create_entry(
                entry_content, current_time.strftime("%m.%d.%Y, %H:%M"))
            flash("Gönderi Başarılı")

        except Exception as e:
            pass

    return render_template("home.html", entries=database.retrieve_entries())


@app.route("/wipe", methods=["GET", "POST"])
def wipe():
    if request.method == "POST":
        password = request.form.get("password")
        if password == token:
            database.clear_database()
            flash("Silme İşlemi Başarılı")
            return redirect(url_for('home'))

    return render_template("wipe.html")


@app.route("/delete/<message_id>", methods=["GET", "POST"])
def delete(message_id):
    if request.method == "POST":
        password = request.form.get("password")
        if password == token:
            database.delete(message_id)
            flash("Silme İşlemi Başarılı")
            return redirect(url_for('home'))

    return render_template("wipe.html")


@app.route("/upvote/<message_id>", methods=["GET", "POST"])
def upvote(message_id):
    database.upvote(message_id)
    return render_template('succes.html')


@app.route("/top", methods=["GET", "POST"])
def top():
    if request.method == "POST":
        try:
            entry_content = request.form.get("message")
            current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
            database.create_entry(
                entry_content, current_time.strftime("%m.%d.%Y, %H:%M"))
            flash("Gönderi Başarılı")
        except Exception as e:
            pass

    return render_template("home.html", entries=database.retrieve_entries_top())


@app.route("/rules")
def rules():
    return render_template("rules.html")
