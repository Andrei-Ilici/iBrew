from tkinter import Entry, Tk, Button, Label
from database import connect

def NewWindow_Addpeople():

    new = Tk()
    new.title("Add people")
    new_first_name = Entry(new, width=27)
    new_surname = Entry(new, width=27)
    new_age = Entry(new, width=27)
    
    new_first_name.grid(row=1,column=2)
    new_surname.grid(row=2, column=2)
    new_age.grid(row=3, column=2)
    
    new_pers_enter = Button(new, text= "Enter", command=lambda: enterval())
    new_pers_enter.grid(row=5, column=2)
    
    new_pers_exit = Button(new, text="Exit", command=new.destroy)
    new_pers_exit.grid(row=6, column=2)
    
    first_name_label = Label(new, text= "Insert first name here: ")
    surname_label = Label(new, text= "Insert surname here: ")
    age_label = Label(new, text= "Insert age here: ")

    first_name_label.grid(row=1, column=1)
    surname_label.grid(row=2, column=1)
    age_label.grid(row=3, column=1)
    
    def enterval():
        connect()
        from database import connection
        value_first_name = new_first_name.get()
        value_surname = new_surname.get()
        value_age = new_age.get()
        
        cursor_people = connection.cursor()

        sql_person_command = "INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)"
        val_person = (value_first_name, value_surname, value_age)
        cursor_people.execute(sql_person_command, val_person)
        connection.commit()
        
        cursor_people.close()
        connection.close()