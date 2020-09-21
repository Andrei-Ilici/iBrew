from tkinter import Button, END, Entry, Label, Text, Tk

drinks = ['Fanta','Schweppes','Tuborg','Pepsi']

root = Tk()
root.title("Maybe it works")

i=0
for drink in drinks:
    message = "I want to order " + drink + " for "
    myLabel = Label(root, text=message)
    myLabel.grid(row = i, column=1)
    
    number_box = Entry(root, width=27)
    number_box.grid(row = i, column =2)
    number_value = number_box.get()
    
    i+=1
    
def enterval():
    print(number_value)

afisare = Button (root, text = "save", command = lambda: enterval())
afisare.grid()

root.mainloop()