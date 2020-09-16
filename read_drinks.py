from database import connect

def read_drinksdb():
    connect()
    from database import connection

    cursor_drinks = connection.cursor()
    cursor_drinks.execute("SELECT name, container, volume FROM drink")
    rows = cursor_drinks.fetchall()
    print (rows)

    for row in rows:
        print(str(row[0]) + "comes in a " + row[1] + ' bottle of ' + str(row[2])+' liters.')
    
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