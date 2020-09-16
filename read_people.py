from database import connect
from funct_person import Person

def read_peopledb():
    connect()
    from database import connection
    global rowsp,people
    people=[]
    cursor_people = connection.cursor()
    
    cursor_people.execute("SELECT first_name, last_name, age FROM person")
    rowsp = cursor_people.fetchall()
    for row in rowsp:
        person = Person(row[0],row[1],row[2])
        people.append(person)
    
    cursor_people.close()
    connection.close()

def add_peopledb():
    connect()
    from database import connection
    
    cursor_people = connection.cursor()
    first_name = input("The first name is: ")
    surname = input("The surname is: ")
    age = int(input("The age is: "))

    sql_person_command = "INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)"
    val_person = (first_name, surname, age)
    cursor_people.execute(sql_person_command, val_person)
    connection.commit()
    cursor_people.close()
    connection.close()

read_peopledb()