import pymysql

connection = pymysql.connect(
    host =	"localhost",
    port = 3306,
    user = "root",
    password = "ttii2.jI",
    db = "people",
)
cursor = connection.cursor()
cursor.execute("SELECT person_id, first_name, surname, age FROM person")
rows = cursor.fetchall()
print (rows)
for row in rows:
    print("ID - " + str(row[0]) + ", Name - " + row[1] + ' '+ row[2]+ ' is '+ str(row[3]) + ' old.')

first_name = input("The first name is: ")
surname = input("The surname is: ")
age = int(input("The age is: "))

sql_person_command = "INSERT INTO person (first_name, surname, age) VALUES (%s, %s, %s)"
val_person = (first_name, surname, age)
cursor.execute(sql_person_command, val_person)
connection.commit()

cursor.close()
connection.close()