# 载入 pymongo 套件
import pymongo
import certifi
from bson.objectid import ObjectId

# 连线到 MongoDB 云端资料库

client = pymongo.MongoClient(
    "mongodb+srv://root:112611You@mycluster.d222soe.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=certifi.where(),
)
# 把资料放进资料库中
db = client.website  # 选择操作 test 资料库

collection = db.users  # 选择操作 users 集合

# 取得集合中的第一笔文件资料
# data=collection.find_one()
# 根据 ObjectId 取得文件资料
# data = collection.find_one(ObjectId("64326c95cbad3845acb618a8"))
# 取得文件资料中的栏位
# print(data["_id"])
# print(data["name"])
# print(data)
# 一次取得多笔文件资料
cursor=collection.find()
for doc in cursor:
    print(doc["name"])
