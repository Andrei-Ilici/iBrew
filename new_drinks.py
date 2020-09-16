from tkinter import *

def NewWindow_Adddrinks():
    new = Tk()
    new.title("Add drinks")
    new_drink = Entry(new, width=27)
    new_container = Entry(new, width=27)
    new_volume = Entry(new, width=27)
    
    new_drink.grid(row=1,column=2)
    new_container.grid(row=2, column=2)
    new_volume.grid(row=3, column=2)
    
    new_drinks_enter = Button(new, text= "Enter", command=lambda: enterval())
    new_drinks_enter.grid(row=5, column=2)
    
    new_drinks_exit = Button(new, text="Exit", command=new.destroy)
    new_drinks_exit.grid(row=6, column=2)
    
    drink_label = Label(new, text= "Insert drink here: ")
    container_label = Label(new, text= "Insert container here: ")
    volume_label = Label(new, text= "Insert volume here: ")

    drink_label.grid(row=1, column=1)
    container_label.grid(row=2, column=1)
    volume_label.grid(row=3, column=1)
    
    def enterval():
        value_drink = new_drink.get()
        value_container = new_container.get()
        value_volume = new_volume.get()
        print( value_drink + ' '+ value_container + ' ' + value_volume)    