#Read
from funct_person import Person
from funct_drink import Drinks
import os
import sys
import csv

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
                person = Person(row[0],row[1],row[2])
                people.append(person)
            elif file_name == "program_drinks.csv":
                drink = Drinks(row[0],row[1],row[2])
                drinks.append(drink)