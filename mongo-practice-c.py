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

# 一次新增多笔资料，取得多笔资料的编号
result = collection.insert_many(
    [
        {"name": "zhangsan", "email": "test@test.com", "password": "jack", "level": 2},
        {"name": "lisi", "email": "test@test.com", "password": "bob", "level": 2},
    ]
)
print("新增资料成功")
print(result.inserted_ids)
# 把资料新增到集合中，取得新增资料编号
# result=collection.insert_one(
#     {"name": "blue", "email": "blue@blue.com", "password": "zhu", "level": 2}
# )

# print(result.inserted_id)
# print("新增资料成功")
