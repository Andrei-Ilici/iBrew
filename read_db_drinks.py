import pymysql

connection = pymysql.connect(
    host =	"localhost",
    port = 3306,
    user = "root",
    password = "ttii2.jI",
    db = "drinks",
)
cursor = connection.cursor()
cursor.execute("SELECT drink_id, name, volume FROM drink")
rows = cursor.fetchall()
print (rows)
for row in rows:
    print("ID - " + str(row[0]) + ": " + row[1] + ' has a volume of ' + str(row[2])+' liters.')
cursor.close()
connection.close()