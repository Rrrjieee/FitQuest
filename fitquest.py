import os

from flask import Flask, render_template, request, redirect, url_for, abort
from flask_apscheduler import APScheduler
from scripts.routine_type import *

app     = Flask(__name__)
data    = {}

# @app.route("/routine")

@app.route("/user_id=<index>/ready")
def ready_screen(index):
    data["timeout"]     = 4
    return render_template("ready_screen.html", index=index, timeout=data["timeout"])
    
@app.route("/user_id=<index>/option=<mode>")
def user_routine(index, mode):
    rout_type       = get_routine_type(mode)
    data["option"]  = rout_type
    if (rout_type == "invalid"):
        abort(404)

    match (rout_type):
        case RoutineType.custom:
            return render_template("user_custom_routine.html", id=index)
        
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
    import fitquest_load_exercises
    exer_list   = fitquest_load_exercises.load_exercises()
    app.run(debug=True, use_reloader=False)