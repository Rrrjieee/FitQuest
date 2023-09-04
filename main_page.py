import os
import config as cfg

from flask import Flask, render_template, request, redirect
from scripts.page_activity_data import PageActivityData

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        return render_template("main_page.html")

    if request.form.get('start') == 'START':
        return redirect("/user_list")

@app.route("/user_list", methods=["GET", "POST"])
def user_page():
    if request.method == 'GET':
        print("/user_list >> GET")
        return render_template("user_select.html")
    
    print("/user_list >> POST")
    return render_template("user_select.html")

@app.route("/user_routine")
def user_routine():
    return render_template("user_routine_prompt.html")

if __name__ == "__main__":
    app.run()