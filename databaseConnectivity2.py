import mysql.connector

dbname = "world"
user = "root"
password = "rohit"
host = "localhost"
port = "3306"

conn = mysql.connector.connect(
 database=dbname,
 user=user,
 password=password,
 host=host,
 port=port
 )


cursor = conn.cursor()
cursor.execute("Select * from city where name = 'Rafah' ")

rows = cursor.fetchall()
for i in rows:
    print(i)