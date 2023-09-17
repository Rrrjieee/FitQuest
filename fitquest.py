import os
import fitquest_load_css as fq_css

from flask import Flask, render_template, request, redirect, url_for, abort
from scripts.routine_type import *

app                         = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
data                        = {}

#   =================   CSS  Section    =====================
@app.route('/css/user_custom_routine.css')
def css_user_custom_routine():
    return fq_css.user_custom_routine(app, exer_list)

#   =================   HTML Section    =====================
@app.route("/user_id=<index>/exercise")
def exercise_screen(index):
    print("Exercise screen requested.")
    return render_template("exercise_page.html", index=index, template=2)

@app.route("/user_id=<index>/ready")
def ready_screen(index):
    data["timeout"]     = 3
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
    import fitquest_load_exercises as fq_load_exer
    exer_list   = fq_load_exer.load_exercises()
    app.run(debug=True, use_reloader=False)