from database import connect
from class_person import Person

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