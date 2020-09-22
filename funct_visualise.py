from tkinter import Button, END, Entry, Label, Text, Tk
from dict_order import total_orders, individual_spending

import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def visualise_person():
    newer = Tk()
    newer.title("Visualisation 1")
    
    labels1 = []
    values1 = []
    
    for key in individual_spending:
        labels1.append(key)
        values1.append(individual_spending[key])
    
    fig = matplotlib.figure.Figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    
    ax.pie(values1)
    ax.legend(labels1, title = "Names")
    ax.set_title("Individual spend referenced to total")
    
    canvas = FigureCanvasTkAgg(fig, master=newer)
    canvas.get_tk_widget().pack()
    canvas.draw()

    newer.mainloop()
    
def visualise_drink():
    newer = Tk()
    newer.title("Visualisation 2")
    
    labels2 = []
    values2 = []
    
    for key in total_orders:
        labels2.append(key)
        values2.append(total_orders[key])
    
    fig = matplotlib.figure.Figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    
    ax.pie(values2)
    ax.legend(labels2, title = "Drinks")
    ax.set_title("Drink spending")
    
    canvas = FigureCanvasTkAgg(fig, master=newer)
    canvas.get_tk_widget().pack()
    canvas.draw()

    newer.mainloop()
    