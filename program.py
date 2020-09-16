
import sys
import os
import csv
from funct_person import Person
from funct_drink import Drinks
from funct_order import Order
from funct_favourite import Favourite





# def menu():
#     os.system("clear")
#     menu_text ="""
# Please select an option by entering a number:

#     [1] Display all people
#     [2] Display all drinks
#     [3] Add people
#     [4] Add drinks
#     [5] Order menu
#     [6] Link people with drinks
#     [7] Exit
#     """
#     print(menu_text)
#     return int(input("Enter a number: "))

# while True:
#     selection = menu()
#     if selection == 1:
#         read("program_people.csv")
#         for individual in people:
#             print(individual)
#     if selection == 2:
#         read("program_drinks.csv")
#         for beverage in drinks:
#             print(beverage)
#     if selection == 3:
#         Person.write("program_people.csv")
#     if selection == 4:
#         Drinks.write("program_drinks.csv") 
#     if selection == 5:
#         bar_menu()
#     if selection == 6:
#         link()
#     if selection == 7:
#         print("Bye, thanks for using our program!!")
#         exit()
#     input("Press Enter to return to main menu.")