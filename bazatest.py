import pymysql

connection = pymysql.connect(
    host =	"localhost",
    port = 3306,
    user = "root",
    password = "ttii2.",
    db = "people",
)
cursor = connection.cursor()
cursor.execute("SELECT person_id, first_name FROM person")
rows = cursor.fetchall()
print (rows)
for row in rows:
    print("ID - " + str(row[0]) + ", Name - " + row[1])
cursor.close()
connection.close()