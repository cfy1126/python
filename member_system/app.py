# 初始化数据库连接
import pymongo
import certifi

client = pymongo.MongoClient(
    "mongodb+srv://root:112611You@mycluster.d222soe.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=certifi.where(),
)
db = client.member_system
print("数据库连接成功")

# 初始化 Flask 服务器
from flask import *

app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "123456"


# 处理路由
@app.route("/")
def index():
    return render_template("index.html")


# 会员页面
@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html", name=session["nickname"])
    else:
        return redirect("/")


# /error?msg=错误讯息
@app.route("/error")
def error():
    message = request.args.get("msg", "发生错误，请联系客服")
    return render_template("error.html", message=message)


# 注册
@app.route("/signup", methods=["POST"])
def signup():
    # 从前端接收资料
    nickname = request.form["nickname"]
    email = request.form["email"]
    password = request.form["password"]
    # 根据接收到的资料，和资料库互动
    collection = db.user
    # 检查会员集合中是否有相同的 Email 的文件资料
    result = collection.find_one({"email": email})
    if result != None:
        return redirect("/error?msg=邮箱已经被注册")
    # 把资料放进资料库，完成注册
    collection.insert_one({"nickname": nickname, "email": email, "password": password})
    return redirect("/")


# 登录
@app.route("/signin", methods=["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]
    collection = db.user
    result = collection.find_one({"$and": [{"email": email}, {"password": password}]})
    print(result)
    if result != None:
        session["nickname"] = result["nickname"]
        return redirect("/member")
    return redirect("/error?msg=账号或者密码输入错误")


# 登出
@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")


app.run(port=3001)
