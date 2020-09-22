from dict_order import total_orders, individual_spending
from funct_visualise import visualise_drink, visualise_person
from tkinter import Button, END, Entry, Label, Text, Tk
from datetime import datetime
from random import randint

def check():
    new = Tk()
    new.title("Check")
    total = 0
    
    T = Text(new, height = 19, width= 48)
    T.delete(1.0, END)
    welcome_message = ("Generation bar" +'\n'+ str(datetime.now().strftime("%b-%d-%Y %H:%M:%S")) +'\n' + "Table "+ str(randint(1, 20)) + '\n' + '\n')
    T.insert(END, welcome_message)
    
    for key in total_orders:
        message = ('\n' + "Ordered £" + str(total_orders[key]) + " worth of " + key + ".")
        T.insert(END, message)
    
    T.insert(END, "\n\n")
    
    for key in individual_spending:
        message = ('\n'+ key + " owes the group £" +  str(individual_spending[key]) +"." )
        T.insert(END, message)
        total += individual_spending[key]
    
    final_message = ('\n\n'+ "Total owed equals: £" + str(total))
    T.insert(END, final_message)
    T.grid()

    button_visualise_person = Button(new, text = "Visualise individual spending", command = lambda: visualise_person())
    button_visualise_person.grid()
    
    button_visualise_drink = Button(new, text = "Visualise drink spending", command = lambda: visualise_drink())
    button_visualise_drink.grid()
    
    
    new.mainloop()