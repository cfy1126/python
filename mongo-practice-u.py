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
# 更新集合中的一笔文件资料
# result = collection.update_one({"email": "test@test.com"}, {"$mul": {"level": 2}})
# print("符合筛选条件的文件数量", result.matched_count)
# print("实际更新的文件数量", result.modified_count)

# 更新集合中的多笔文件资料 $set $unset $inc $mul
result = collection.update_many({"level": 2}, {"$set": {"description": "我是会员"}})
print("符合更新文件数量", result.matched_count)
print("实际更新的文件数量", result.modified_count)
