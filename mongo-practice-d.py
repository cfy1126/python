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
# 删除集合中的一笔文件资料
# result = collection.delete_one({"email": "test@test.com"})
# print("实际上删除的资料有几笔", result.deleted_count)
# 删除集合中的多笔文件资料
result=collection.delete_many({
    "email":"test@test.com"
})
print("实际删除的资料有几笔",result.deleted_count)