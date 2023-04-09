from flask import Flask
from flask import request # 载入 Request 物件
# 建立 Application 物件,可以设定静态档案路径处理
app=Flask(
  __name__,
  static_folder="static", # 静态档案的资料夹名称
  static_url_path="/" # 静态档案对应的网址路径
  ) 
# 所有在 static 资料夹下的档案，都对应到网址路径 /static/ 档案名称

# 建立路径 /getSum 对应的处理方法
# 利用要求字符串（Query String）提供弹性： /getSum?max=最大数字&min=最小数字
@app.route("/getSum")
def getSum(): # min+(min+1)+(min+2)+(min+3)+....+max
  # 接收要求字符串中的参数资料
  maxNumber=request.args.get("max",100)
  maxNumber=int(maxNumber)
  minNumber=request.args.get("min",1)
  minNumber=int(minNumber)
  result=0
  for n in range(minNumber,maxNumber+1):
    result+=n
  return "结果："+str(result)

# 建立路径 / 对应的处理方法
@app.route("/")
def index():
  # print("请求方法",request.method)
  # print("通讯协定",request.scheme)
  # print("主机名称",request.host)
  # print("路径",request.path)
  # print("完整的网址",request.url)
  # print("浏览器和作业系统",request.headers.get("user-agent"))
  # print("语言偏好",request.headers.get("accept-language"))
  # print("引用网址",request.headers.get("referrer"))
  lang=request.headers.get("accept-language")
  print("语言偏好",lang)
  if lang.startswith("en"):
    return "Hello Flask"
  else:
    return "您好，欢迎光临！"

# 建立路径 /data 对应的处理方法
@app.route("/data")
def handleData():
  return "love blue" # 回应网站首页的内容

# 动态路由：建立路径 /user/使用者名称 对应的处理方法
@app.route("/user/<username>")
def handleUser(username):
  if username=='xiao cao':
    return "Hello xiao cao"
  else:
    return "Hello 曹发友"

# 启动网站服务器(127.0.0.1)，可通过 port 参数指定端口
app.run(port=3001)