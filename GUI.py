from tkinter import *
from funct_favourite import Favourite
from read_csv import read

root = Tk()
root.title("iBrew app")
people = [2]
# e = Entry(root, width=32)
# e.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

#Define button actions
def readpeop():
    read("program_people.csv")
    from read_csv import people
    for individual in people:
        print(individual)

def readdrk():
    read("program_drinks.csv")
    from read_csv import drinks
    for beverage in drinks:
        print(beverage)

def addpeop():
    from funct_person import Person
    Person.write("program_people.csv")

def adddrk():
    from funct_drink import Drinks
    Drinks.write("program_drinks.csv") 

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

#Arrange buttonsfrom program import read
button_read_people.grid(row=2, column=1)
button_read_drinks.grid(row=3, column=1)
button_add_people.grid(row=4, column=1)
button_add_drinks.grid(row=5, column=1)
button_order_menu.grid(row=6, column=1)
button_link_people.grid(row=7, column=1)
button_exit.grid(row=8, column=1)

root.mainloop()