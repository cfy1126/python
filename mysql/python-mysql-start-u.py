import mysql.connector

# 连线到资料库
con = mysql.connector.connect(
    user="root", password="112611you", host="localhost", database="caodb"
)
print("数据库连接成功")
# 更新资料
cursor = con.cursor()
productId = 1
productName = "美式"
cursor.execute("UPDATE product SET name=%s WHERE id=%s", (productName, productId))
con.commit()  # 确认执行
# 关闭资料库连线
con.close()
