import datetime
from flask import Flask, render_template, request
import database


app = Flask(__name__)

database.create_tables()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("message")
        current_time = datetime.datetime.today() + datetime.timedelta(hours=3)
        database.create_entry(entry_content, current_time.strftime("%m.%d.%Y, %H:%M"))

    return render_template("home.html", entries=database.retrieve_entries())
