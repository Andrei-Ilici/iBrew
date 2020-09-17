from database import connect
from class_drinks import Drinks

def read_drinksdb():
    connect()
    from database import connection
    global drinks
    drinks=[]

    cursor_drinks = connection.cursor()
    cursor_drinks.execute("SELECT name, container, volume FROM drink")
    rowsd = cursor_drinks.fetchall()

    for row in rowsd:
        drink = Drinks(row[0],row[1],row[2])
        drinks.append(drink)
    
    cursor_drinks.close()
    connection.close()