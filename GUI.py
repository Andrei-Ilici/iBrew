from tkinter import Entry, Tk, Button, Label, END, Text
from new_people import NewWindow_Addpeople
from new_drinks import NewWindow_Adddrinks
from new_round import NewWindow_addround
from read_people import read_peopledb
from read_drinks import read_drinksdb
from funct_check import check

root = Tk()
root.title("iBrew app")

#Define button actions
def readpeop():
    read_peopledb()
    from read_people import people
    T.delete(1.0, END)
    for person in people:
        T.insert(END, person)
        T.insert(END, '\n')

def readdrk():
    read_drinksdb()
    from read_drinks import drinks
    T.delete(1.0, END)
    for beverage in drinks:
        T.insert(END, beverage)
        T.insert(END, '\n')

def addpeop():
    NewWindow_Addpeople()

def adddrk():
    NewWindow_Adddrinks()

def addround():
    NewWindow_addround()

def getcheck():
    check()

### Define interface
hellomenu = """
Please select one of the following options: 
"""
myLabel = Label(root, text=hellomenu)
myLabel.grid(row=1, column=1)

#Define button
button_read_people = Button(root, text="Read people", padx=119, pady=20, command=readpeop)
button_read_drinks = Button(root, text="Read drinks", padx=121, pady=20, command=readdrk)
button_add_people = Button(root, text="Add people", padx=123, pady=20, command=addpeop)
button_add_drinks = Button(root, text="Add drinks", padx=125, pady=20, command=adddrk)
button_order_menu = Button(root, text="Order round", padx=121, pady=20, command=addround)
button_link_people = Button(root, text="Get the check", padx=115, pady=20, command=getcheck)
button_exit = Button(root, text="Exit", padx=147, pady=20, command=root.destroy)
T= Text(root, height=15, width=69)

#Arrange buttons
T.grid(row=2, column=1)
button_read_people.grid(row=3, column=1)
button_read_drinks.grid(row=4, column=1)
button_add_people.grid(row=5, column=1)
button_add_drinks.grid(row=6, column=1)
button_order_menu.grid(row=7, column=1)
button_link_people.grid(row=8, column=1)
button_exit.grid(row=9, column=1)

root.mainloop()