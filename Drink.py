total = int(input("How many names do you want to input?\n"))
names = []
drinks = []

for i in range(0,total):
    name = input("What is your friend's name?\n")
    drink = input("What is their favourite drink?\n")
    names.append(name)
    drinks.append(drink)

for i in range(0,total):
    print( names[i].capitalize() + "'s favourite drink is " + drinks[i].lower() )