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
    T.delete(1.0, END)
    for individual in people:
        T.insert(END, individual)
        T.insert(END, '\n')
    NewWindow_Addpeople()

def readdrk():
    read("program_drinks.csv")
    from read_csv import drinks
    T.delete(1.0, END)
    for beverage in drinks:
        T.insert(END, beverage)
        T.insert(END, '\n')

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

def NewWindow_Addpeople():
    new = Toplevel(root)
    new.title("Add people")
    mylabel = Label(new, text="Works")
    mylabel.grid(row=2, column =2)
    new_name = Entry(new, width=27)
    new_age = Entry(new, width=27)
    new_height = Entry(new, width=27)
    new_fav = Entry(new, width=27)
    
    new_name.grid(row=1,column=2)
    new_age.grid(row=2, column=2)
    new_height.grid(row=3, column=2)
    new_fav.grid(row=4, column=2)
    
    new_pers_enter = Button(new, text= "Enter", command=lambda: enterval())
    new_pers_enter.grid(row=5, column=2)
    
    new_pers_exit = Button(new, text="Exit", command=new.destroy)
    new_pers_exit.grid(row=6, column=2)
    
    name_label = Label(new, text= "Insert name here: ")
    age_label = Label(new, text= "Insert age here: ")
    height_label = Label(new, text= "Insert height here: ")
    fav_label = Label(new, text= "   Insert favourite drink here:   ")

    name_label.grid(row=1, column=1)
    age_label.grid(row=2, column=1)
    height_label.grid(row=3, column=1)
    fav_label.grid(row=4, column=1)
    
    def enterval():
        value_name = new_name.get()
        value_age = new_age.get()
        value_height = new_height.get()
        value_fav = new_fav.get()
        print(value_name + value_age + value_height + value_fav)    
    

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

#Arrange buttonsfrom program import read
T.grid(row=2, column=1)
button_read_people.grid(row=3, column=1)
button_read_drinks.grid(row=4, column=1)
button_add_people.grid(row=5, column=1)
button_add_drinks.grid(row=6, column=1)
button_order_menu.grid(row=7, column=1)
button_link_people.grid(row=8, column=1)
button_exit.grid(row=9, column=1)

root.mainloop()