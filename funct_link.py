from read_csv import read

def link():
    from class_person import Person
    from class_drinks import Drinks
    from class_favourite import Favourite

    preference = []
    drink_list=[]
    read("program_people.csv")
    from read_csv import people

    print("The available clients are: ")
    for individual in people:
        print("- " + individual.name)
    read("program_drinks.csv")
    from read_csv import drinks
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