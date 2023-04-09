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


@app.route("/show")
def show():
    name = request.args.get("name", "")
    return "欢迎光临，" + name


@app.route("/calculate")
def calculate():
    maxNumber = request.args.get("max", "")
    maxNumber = int(maxNumber)
    result = 0
    for n in range(1, maxNumber + 1):
        result += n
    return render_template("result.html",result=result)


app.run(port=3001)
