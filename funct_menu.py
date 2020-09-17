from read_csv import read
from class_order import Order

def bar_menu():
    orders = []
    read("program_people.csv")
    from read_csv import people
    for individual in people:
        menu_product = input(individual.name + " would like to order a ")
        order = Order(individual.name, menu_product)
        orders.append(order)
    for order in orders:
        print(order)