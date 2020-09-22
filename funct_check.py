from class_order import total_orders, individual_spending
#from new_round import prices
from funct_visualise import visualise
from tkinter import Button, END, Entry, Label, Text, Tk
from datetime import datetime
from random import randint

def check():
    new = Tk()
    new.title("Check")
    
    T = Text(new, height = 19, width= 48)
    T.delete(1.0, END)
    welcome_message = ("Generation bar" +'\n'+ str(datetime.now()) +'\n' + "Table "+ str(randint(1, 20)))
    T.insert(END, welcome_message)
    
    # for key in total_orders:
    #     message = ('\n' + )
    
    for key in individual_spending:
        message = ('\n'+ key + " owes the group £" +  str(individual_spending[key]) +"." )
        T.insert(END, message)
    
    T.grid()

    button_visualise = Button(new, text = "Visualise the spending", command = visualise())
    button_visualise.grid()
    
    new.mainloop()