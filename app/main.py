import datetime
from flask import Flask, render_template, request
import database


app = Flask(__name__)

database.create_tables()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("message")
        database.create_entry(entry_content, datetime.datetime.today().strftime("%m.%d.%Y, %H:%M"))

    return render_template("home.html", entries=database.retrieve_entries())
