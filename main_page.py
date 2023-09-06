import os
import config as cfg

from flask import Flask, render_template, request, redirect, url_for
from scripts.page_activity_data import PageActivityData

app = Flask(__name__)

@app.route("/routine/user_id=<index>", methods=["GET", "POST"])
def user_routine(index):
    if request.method == 'GET':
        return render_template("user_routine_prompt.html")
    
    return redirect(url_for("main_page"))

@app.route("/user_list", methods=["GET", "POST"])
def user_page():
    if request.method == 'GET':
        return render_template("user_select.html")
    
    return redirect(url_for("user_routine"))

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        return render_template("main_page.html")

    return redirect(url_for("user_page"))

if __name__ == "__main__":
    app.run(debug=True)