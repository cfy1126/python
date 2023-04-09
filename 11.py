from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, static_folder="static", static_url_path="/")

# 使用 GET 方法，处理路径 / 的对应方法
@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/page")
def page():
    return render_template("page.html")


@app.route("/show")
def show():
    name = request.args.get("name", "")
    return "欢迎光临，" + name

# 使用 GET 方法，处理 /calculate 对应的方法
@app.route("/calculate",methods=["POST"])
def calculate():
    # 接收 GET 方法的 Query String
    # maxNumber = request.args.get("max", "")
    # 接收 POST 方法的 Query String
    maxNumber=request.form["max"]
    maxNumber = int(maxNumber)
    result = 0
    for n in range(1, maxNumber + 1):
        result += n
    return render_template("result.html",result=result)


app.run(port=3001)
