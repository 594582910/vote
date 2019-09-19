import pymysql.cursors

try:
    conn = pymysql.connect(host='172.16.4.150', port=3306, user='root', password='123456', db='mysql', charset='utf8')
    # create cursor
    cursor = conn.cursor()
    print("Connect DB successfully!")
except ConnectionError:
    print("failure")

sql = "insert into www(test,hello) values (2,1)"
selsql = "select * from www"

cursor.execute(sql)
# cursor.execute(selsql)
# data = cursor.fetchall()
# print(data)
conn.commit()

cursor.close()
conn.close()

