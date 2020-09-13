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

name = input ("What is the name of your drink? ")
volume = float(input( "What is the volume of your drink?"))

sql_drink = "INSERT INTO drink (name, volume) VALUES (%s, %s)"
val_drink = (name, volume)

cursor.execute(sql_drink, val_drink)
connection.commit()

cursor.close()
connection.close()