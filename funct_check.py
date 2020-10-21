## This function is displayed once the app user requests the check after everything they ordered

from dict_order import total_orders, individual_spending
from funct_visualise import visualise_drink, visualise_person
from tkinter import Button, END, Entry, Label, Text, Tk
from datetime import datetime
from random import randint

def check():
    new = Tk()
    new.title("Check")
    total = 0
    
    # At the top of the window, the welcome text will display current time of the system and a random table number from 1 to 20.
    # Future version idea: add option to add a personalised table number. Accounts for multiple tables ordering at the same time. Based on the table number, it can output specific checks.
    # Delete the saved data after check (table is free so a new group can occupy it) 
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

    # This function allows the person paying for the bill to know who ordered what, and split the bill quicker
    button_visualise_person = Button(new, text = "Visualise individual spending", command = lambda: visualise_person())
    button_visualise_person.grid()
    
    # This function is intented for the bar owner mainly, who wants to know what are the best selling drinks
    button_visualise_drink = Button(new, text = "Visualise drink spending", command = lambda: visualise_drink())
    button_visualise_drink.grid()
    
    
    new.mainloop()