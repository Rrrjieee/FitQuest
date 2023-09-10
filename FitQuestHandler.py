import os

from flask import Flask, render_template, request, redirect, url_for, abort
from scripts.routine_type import *

app     = Flask(__name__)
data    = {}

@app.route("/user_id=<index>/option=<mode>")
def user_routine(index, mode):
    rout_type       = get_routine_type(mode)
    data["option"]  = rout_type
    if (rout_type == "invalid"):
        abort(404)

    match (rout_type):
        case RoutineType.premade:
            return render_template("user_premade_routine.html", id=index)
        
    return "Sorry, no webpage yet."

@app.route("/user_id=<index>")
def user_front_page(index):
    data["id"]  = index
    return render_template("user_front_page.html", id=data["id"])

@app.route("/user_login")
def user_login():
    return render_template("user_login.html")

@app.route("/")
@app.route("/index")
def main_page():
    return render_template("home_page.html", is_homepage=True)

if __name__ == "__main__":
    app.run(debug=True)