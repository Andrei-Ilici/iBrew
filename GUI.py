from tkinter import *
from funct_favourite import Favourite
from read_csv import read
from new_people import NewWindow_Addpeople
from new_drinks import NewWindow_Adddrinks
from read_people import read_peopledb

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
    read("program_drinks.csv")
    from read_csv import drinks
    T.delete(1.0, END)
    for beverage in drinks:
        T.insert(END, beverage)
        T.insert(END, '\n')

def addpeop():
    NewWindow_Addpeople()
    # from funct_person import Person
    # Person.write("program_people.csv")

def adddrk():
    NewWindow_Adddrinks()
    # from funct_drink import Drinks
    # Drinks.write("program_drinks.csv") 

def ordermenu():
    from funct_menu import bar_menu
    from funct_order import Order
    bar_menu()

def linkpeop():
    from funct_link import link
    link()

#Define interface
hellomenu = """
Please select an option by entering a number:

    [1] Display all people
    [2] Display all drinks
    [3] Add people
    [4] Add drinks
    [5] Order menu
    [6] Link people with drinks
    [7] Exit
    """
myLabel = Label(root, text=hellomenu)
myLabel.grid(row=1, column=1)

#Define button
button_read_people = Button(root, text="Read people", padx=120, pady=20, command=readpeop)
button_read_drinks = Button(root, text="Read drinks", padx=120, pady=20, command=readdrk)
button_add_people = Button(root, text="Add people", padx=120, pady=20, command=addpeop)
button_add_drinks = Button(root, text="Add drinks", padx=120, pady=20, command=adddrk)
button_order_menu = Button(root, text="Order menu", padx=120, pady=20, command=ordermenu)
button_link_people = Button(root, text="Link people", padx=120, pady=20, command=linkpeop)
button_exit = Button(root, text="Exit", padx=135, pady=20, command=root.quit)
T= Text(root, height=7, width=69)

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