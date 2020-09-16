
class Person:
    def __init__(self,name,age,height,favourite_drink):
        self.name = name
        self.age = age
        self.height = height
        self.favourite_drink = favourite_drink
    
    def __repr__(self):
        return f"{self.name} is {self.age} old, {self.height} meters tall and loves drinking {self.favourite_drink}."
    
    def write(self):
        with open(self,"a") as write_elem:
            new_name = input("Please write the person name: ") 
            new_age = input("Please write their age: ")
            new_height = input("Please write their height: ")
            new_fav_drink = input("Please write their favourite drink: ")
            write_elem.write('\n' + new_name+ ","+ new_age+ ","+ new_height+ ","+new_fav_drink)