from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__,static_folder="static",static_url_path="/")

@app.route("/")
def index():
    return "Hello Flask"

app.run(port=3001)