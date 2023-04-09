from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, static_folder="static", static_url_path="/")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page")
def page():
    return render_template("page.html")


app.run(port=3001)
