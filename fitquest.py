# import os
import json
import fitquest_load_css as fq_css

from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from scripts.routine_type import *
from scripts.exercise import BaseExercise, get_exercise

app                         = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'
data                        = {}

#   =================   CSS  Section    =====================
@app.route('/css/user_custom_routine.css')
def css_user_custom_routine():
    return fq_css.user_custom_routine(app, exer_list)

#   =================  Request  Section =====================
@app.route("/req_data", methods=["POST"])
def request_req_data():
    req_data        = request.get_json()
    rout_type       = get_routine_type(req_data["method"])
    match (rout_type):
        case RoutineType.premade:
            data['exer_list']   = data['routines'][req_data["index"]]
            data['exer_list']   = json.dumps(data['exer_list'], indent=4)
            return jsonify({"response": "200: OK!"})

#   =================   HTML Section    =====================
@app.route("/user_id=<index>/exercise")
def exercise_screen(index):
    print("Exercise screen requested.")
    return render_template("exercise_page.html", index=index, template=2, exer_list=data['exer_list'])

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
            routines        = [[], []]
            
            routines[0].append(vars(get_exercise("sit_ups")))
            routines[0].append(vars(get_exercise("lunges")))
            routines[0].append(vars(get_exercise("push_ups")))

            routines[1].append(vars(get_exercise("lunges")))
            routines[1].append(vars(get_exercise("jumping_jacks")))
            routines[1].append(vars(get_exercise("push_ups")))

            data['routines']    = routines
            routines            = json.dumps(routines, indent = 4)

            desc_file           = open("premade_desc.json", 'r')
            routine_desc        = json.dumps(json.load(desc_file), indent=4)
            desc_file.close()

            return render_template("user_premade_routine.html",
                                   id=index,
                                   routine_data=routines,
                                   routine_desc=routine_desc)
        
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
    app.run(debug=True)