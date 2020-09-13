
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