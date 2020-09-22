from tkinter import Button, END, Entry, Label, Text, Tk
from functools import partial
from read_people import read_peopledb
from read_drinks import read_drinksdb
from dict_order import total_orders, individual_spending

def NewWindow_addround():
    new = Tk()
    new.title("Add round")
    read_peopledb()
    from read_people import people
    myLabel = Label(new, text="Who would like to order some drinks today?")
    myLabel.pack()
    
    
    for person in people:
        click = Button(new, text = person.first_name, command =partial(ordername, person.first_name, person.age))
        click.pack()
    
    button_exit = Button(new, text = "Cancel", command =new.destroy)
    button_exit.pack()

    new.mainloop()
    
def ordername(name, person_age):
    newest = Tk()
    newest.title("Select round")
    
    text = name + " would like to order: "
    myLabel = Label(newest, text= text)
    myLabel.grid()
    
    values=[]
    drink_name=[]
    global drink_price
    drink_price=[]
    
    read_drinksdb()
    from read_drinks import drinks
    i=1
    for drink in drinks:
        if person_age <18 and drink.category == "alcoholic":
            continue
        else:
            drinkLabel = Label(newest, text = drink.name)
            drinkLabel.grid(row=i, column=0)
            drink_name.append(drink.name)
            drink_price.append(drink.price)
            number_box = Entry(newest, width=27)
            number_box.grid(row = i, column =2)
            values.append(number_box)
            i+=1
    
    def enterval(name):
        i=0
        order_value = 0
        
        for value in values:
            
            if drink_name[i] in total_orders.keys():
                total_orders[drink_name[i]] += round( float(value.get())*drink_price[i],2)
            else:
                total_orders[drink_name[i]] = round( float(value.get())*drink_price[i],2)
            
            order_value += round( float(value.get())*drink_price[i],2)
            i+=1       
        if name in individual_spending:
            individual_spending[name] += round ( float(order_value), 2)
        else:
            individual_spending[name] = round ( float(order_value), 2)
        
    
    afisare = Button (newest, text = "Save", command = lambda: enterval(name))
    afisare.grid()
    
    button_exit = Button(newest, text = "Select different person", command =newest.destroy)
    button_exit.grid()
    newest.mainloop()
