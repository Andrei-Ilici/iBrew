from database import connect
from funct_drink import Drinks

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

def add_drinksdb():
    connect()
    from database import connection

    cursor_drinks = connection.cursor()
    name = input ("What is the name of your drink? ")
    container = input("What kind of bottle does it come in? ")
    volume = float(input( "What is the volume of your drink? "))

    sql_drink = "INSERT INTO drink (name, container, volume) VALUES (%s, %s, %s)"
    val_drink = (name, container, volume)
    cursor_drinks.execute(sql_drink, val_drink)
    connection.commit()
    cursor_drinks.close()
    connection.close()