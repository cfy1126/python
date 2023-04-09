# 载入 pymongo 套件
import pymongo
import certifi

# 连线到 MongoDB 云端资料库

client = pymongo.MongoClient(
    "mongodb+srv://root:112611You@mycluster.d222soe.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=certifi.where(),
)
# 把资料放进资料库中
db = client.website  # 选择操作 test 资料库

collection = db.users  # 选择操作 users 集合
# 筛选集合中的文件资料
# doc = collection.find_one({"email": "blue@blue.com"})
# print("取得的资料", doc["description"])

# 复合筛选条件
# doc = collection.find_one(
#     {
#         "$and": [
#             {"email": "blue@blue.com"},
#             {"password": "yan"}
#         ]
#     }
# )
# print("取得的资料", doc)

# 筛选结果排序 pymongo.DESCEDING,pymogon.ASCENDING
cur = collection.find({"$or": [{"email": "blue@blue.com"}, {"level": 2}]},sort=[
    ("level",pymongo.DESCENDING)
])
print("取得资料",cur)
for doc in cur:
    print(doc)
