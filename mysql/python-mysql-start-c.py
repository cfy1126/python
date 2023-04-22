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
# 将变数资料带入到 SQL 指令里面
productId=6
productName='奶绿'
cursor=con.cursor()
cursor.execute("INSERT INTO product(id,name) VALUES(%s,%s)",(productId,productName))
con.commit() # 确认执行
# 关闭资料库连线
con.close()