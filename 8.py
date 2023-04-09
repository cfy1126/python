from flask import Flask
from flask import render_template

app=Flask(__name__,static_folder="static",static_url_path="/")

@app.route("/")
def index():
    return render_template("index",name="xiao cao")

app.run(port=3001)