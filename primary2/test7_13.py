from pymysql import Connection
# 连接MySQL对象
conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
# 获取游标对象
cursor=conn.cursor()
# 选择数据库
conn.select_db("test")
# 使用游标对象，执行了语sql句
# cursor.execute("select * from student")
cursor.execute("insert into student values (5,'jane',18 ,'female') ")
# 手动提交
# conn.commit()
# 获取查询结果
result:tuple=cursor.fetchall()

for r in result:
    print(r)
# 关闭数据库
conn.close()
























