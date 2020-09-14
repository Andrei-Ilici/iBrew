import pymysql
from sqlalchemy import text

connection = pymysql.connect(
    host =	"localhost",
    port = 3306,
    user = "root",
    password = "ttii2.jI",
    db = "people",
)

cursor = connection.cursor()

# first_name = input("The first name is: ")
# surname = input("The surname is: ")
# age = int(input("The age is: "))

# sql_person_command = input("write SQL command: ")
# val_person = (first_name, surname, age)
# cursor.execute(sql_person_command, val_person)

mesag = text ("SELECT surname from person")
cursor.execute (mesag)

connection.commit()
cursor.close()
connection.close()