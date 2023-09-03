import os
import config as cfg

from flask import Flask, render_template
from scripts.page_activity_data import PageActivityData

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("html/main_page.html")

if __name__ == "__main__":
    app.run()