from flask import Flask
from flask import request
from flask import render_template
from flask import session

app = Flask(__name__, static_folder="static", static_url_path="/")
# 设定Session的密钥
app.secret_key = "any string secret"


@app.route("/")
def index():
    return render_template("index.html")


# 使用 GET 方法处理路径 /hello?name=使用者名字
@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    # session["栏位名称"]=资料
    session["username"] = name
    return "你好，" + name


# 使用 GET 方法处理路径 /talk
@app.route("/talk")
def talk():
    name = session["username"]
    return name + "，很高兴见到你"


app.run(port=3001)
