from tkinter import Button, END, Entry, Label, Text, Tk
from functools import partial
from read_people import read_peopledb
from read_drinks import read_drinksdb
from class_order import total_orders

def NewWindow_addround():
    new = Tk()
    new.title("Add round")
    read_peopledb()
    from read_people import people
    myLabel = Label(new, text="Who would like to order some drinks today?")
    myLabel.pack()
    
    
    for person in people:
        click = Button(new, text = person.first_name, command =partial(ordername, person.first_name))
        click.pack()
    
    button_exit = Button(new, text = "Cancel", command =new.destroy)
    button_exit.pack()

    new.mainloop()
    
def ordername(name):
        newest = Tk()
        newest.title("Select round")
        
        text = name + " would like to order: "
        myLabel = Label(newest, text= text)
        myLabel.grid()
        
        values=[]
        drink_name=[]
        
        read_drinksdb()
        from read_drinks import drinks
        i=1
        for drink in drinks:
            drinkLabel = Label(newest, text = drink.name)
            drinkLabel.grid(row=i, column=0)
        
            drink_name.append(drink.name)
            number_box = Entry(newest, width=27)
            number_box.grid(row = i, column =2)
            values.append(number_box)
            i+=1
        
        def enterval(name):
            print(name + " wants to order:")
            i=0
            
            for value in values:
                print(str(value.get()) + " " + drink_name[i])
                if drink_name[i] in total_orders.keys():
                    total_orders[drink_name[i]] += int(value.get())
                else:
                    total_orders[drink_name[i]] = int(value.get())
                i+=1
        
        afisare = Button (newest, text = "save", command = lambda: enterval(name))
        afisare.grid()
        
        button_exit = Button(newest, text = "Select different person", command =newest.destroy)
        button_exit.grid()
        newest.mainloop()
