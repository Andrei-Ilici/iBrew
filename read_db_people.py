import pymysql

connection = pymysql.connect(
    host =	"localhost",
    port = 3306,
    user = "root",
    password = "root_password",
    db = "brew",
)
cursor = connection.cursor()
cursor.execute("SELECT first_name, age FROM person")
rows = cursor.fetchall()
print (rows)
for row in rows:
    print("Name - " + row[0] + ' is '+' old.')

# first_name = input("The first name is: ")
# surname = input("The surname is: ")
# age = int(input("The age is: "))

# sql_person_command = "INSERT INTO person (first_name, surname, age) VALUES (%s, %s, %s)"
# val_person = (first_name, surname, age)
# cursor.execute(sql_person_command, val_person)
connection.commit()

cursor.close()
connection.close()