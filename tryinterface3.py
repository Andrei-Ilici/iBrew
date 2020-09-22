from tkinter import Button, END, Entry, Label, Text, Tk

drinks = ['Fanta','Schweppes','Tuborg','Pepsi']
values=[]

root = Tk()
root.title("Maybe it works")

i=0
for drink in drinks:
    message = "I want to order " + drink + " for "
    myLabel = Label(root, text=message)
    myLabel.grid(row = i, column=1)
    
    number_box = Entry(root, width=27)
    number_box.grid(row = i, column =2)
    values.append(number_box)
    i+=1

def enterval():
    list2=[]
    for entry in values:
        list2.append(int(entry.get()))
        #print (entry.get())
    print(list2)

afisare = Button (root, text = "save", command = lambda: enterval())
afisare.grid()

root.mainloop()