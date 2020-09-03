# This might be the big program
import sys
import os
import csv
from funct_person import Person
from funct_drink import Drinks

class Order:
    def __init__(self,name,drink):
        self.name = name
        self.drink = drink
    
    def __repr__(self):
        return f"{self.name} wants to order a {self.drink}."
    
class Favourite:
    def __init__(self,name,drink):
        self.name = name
        self.drink = drink
    
    def __repr__(self):
        return f"{self.name} would love to order a {self.drink}."
    
    def write(self):
        with open(self,"a") as write_elem:
            new_line = input("Please write the Drink name, its type plus the container and volume it's sold in separated by a comma: ")
            write_elem.write('\n' + new_line)


#Read
def read(file_name):
    global people, drinks
    if file_name == "program_people.csv":
        people = []
    elif file_name == "program_drinks.csv":
        drinks = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if file_name == "program_people.csv":
                person = Person(row[0],row[1],row[2],row[3])
                people.append(person)
            elif file_name == "program_drinks.csv":
                drink = Drinks(row[0],row[1],row[2],row[3])
                drinks.append(drink)

def bar_menu():
    orders = []
    read("program_people.csv")
    for individual in people:
        menu_product = input(individual.name + " would like to order a ")
        order = Order(individual.name, menu_product)
        orders.append(order)
    for order in orders:
        print(order)

def link():
    preference = []
    drink_list=[]
    read("program_people.csv")
    print("The available clients are: ")
    for individual in people:
        print("- " + individual.name)
    read("program_drinks.csv")
    for beverage in drinks:
        drink_item = beverage.name
        drink_list.append(drink_item)
    print("The available drinks to select are: ")
    i = 1
    for beverage in drink_list:
        print(str(i) +". "+ beverage)
        i += 1
    for individual in people:
        fav = int(input(individual.name + " loves drinking drink number: "))
        favour = Favourite(individual.name, drink_list[fav-1])
        preference.append(favour)
    for pref in preference:
        print(pref)

def menu():
    os.system("clear")
    menu_text ="""
Please select an option by entering a number:

    [1] Display all people
    [2] Display all drinks
    [3] Add people
    [4] Add drinks
    [5] Order menu
    [6] Link people with drinks
    [7] Exit
    """
    print(menu_text)
    return int(input("Enter a number: "))

while True:
    selection = menu()
    if selection == 1:
        read("program_people.csv")
        for individual in people:
            print(individual)
    if selection == 2:
        read("program_drinks.csv")
        for beverage in drinks:
            print(beverage)
    if selection == 3:
        Person.write("program_people.csv")
    if selection == 4:
        Drinks.write("program_drinks.csv") 
    if selection == 5:
        bar_menu()
    if selection == 6:
        link()
    if selection == 7:
        print("Bye, thanks for using our program!!")
        exit()
    input("Press Enter to return to main menu.")