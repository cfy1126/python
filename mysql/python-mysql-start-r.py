import mysql.connector
# 连线到资料库
con=mysql.connector.connect(
    user="root",
    password="112611you",
    host="localhost",
    database="caodb"
)
print("数据库连接成功")
# 建立Cursor 物件，用来对资料库下 SQL 指令
cursor=con.cursor()
# 取得一笔资料
# cursor.execute("SELECT * FROM product WHERE id=2")
# data=cursor.fetchone()
# print(data)
# print(data[0],data[1])

# 取得多笔资料
cursor.execute("SELECT * FROM product")
data=cursor.fetchall()
print(data)
# 逐一取得
for row in data:
    print(row)

con.commit() # 确认执行
# 关闭资料库连线
con.close()