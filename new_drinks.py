from tkinter import Entry, Tk, Button, Label
from database import connect

def NewWindow_Adddrinks():
    new = Tk()
    new.title("Add drinks")
    
    new_drink = Entry(new, width=27)
    new_category = Entry(new, width=27)
    new_volume = Entry(new, width=27)
    new_price = Entry(new, width=27)
    
    new_drink.grid(row=1,column=2)
    new_category.grid(row=2, column=2)
    new_volume.grid(row=3, column=2)
    new_price.grid(row=4, column=2)
    
    new_drinks_enter = Button(new, text= "Enter", command=lambda: enterval())
    new_drinks_enter.grid(row=5, column=2)
    
    new_drinks_exit = Button(new, text="Exit", command=new.destroy)
    new_drinks_exit.grid(row=6, column=2)
    
    drink_label = Label(new, text= "Insert drink here: ")
    category_label = Label(new, text= "Insert drink category here: ")
    volume_label = Label(new, text= "Insert volume here: ")
    price_label = Label(new, text= "Insert price here: ")

    drink_label.grid(row=1, column=1)
    category_label.grid(row=2, column=1)
    volume_label.grid(row=3, column=1)
    price_label.grid(row=4, column =1)
    
    def enterval():
        connect()
        from database import connection
        
        value_drink = new_drink.get()
        value_container = new_category.get()
        value_volume = new_volume.get()
        value_price = new_price.get()
        
        cursor_drinks = connection.cursor()

        sql_drink = "INSERT INTO drink (name, category, volume, price) VALUES (%s, %s, %s, %s)"
        val_drink = (value_drink, value_container, value_volume, value_price)
        cursor_drinks.execute(sql_drink, val_drink)
        connection.commit()
        cursor_drinks.close()
        connection.close()
        new.destroy()