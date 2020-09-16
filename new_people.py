from tkinter import *

def NewWindow_Addpeople():
    new = Tk()
    new.title("Add people")
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