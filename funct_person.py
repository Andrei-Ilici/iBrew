
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
            new_line = input("Please write the Name, Age, Height and Favourite drink separated by a comma: ")
            write_elem.write('\n' + new_line)