from flask import Flask
from flask import request
from flask import redirect
import json

app = Flask(__name__, static_folder="static", static_url_path="/")


@app.route("/en/")
def index_english():
    return json.dumps({"status": "ok", "text": "Hello xiao cao"})


@app.route("/zh/")
def index_zh():
    return json.dumps(
        {"status": "ok", "text": "你好，小曹"}, ensure_ascii=False
    )  # 指示不要用 ASCII 编码处理中文


@app.route("/")
def index():
    # 导向到路径 /en/
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/")


app.run(port=3001)
