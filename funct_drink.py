
class Drinks:
    def __init__(self,name,d_type,container,volume):
        self.name = name
        self.category = d_type
        self.container = container
        self.volume = volume
        
    def __repr__(self):
        return f"{self.name} comes in a {self.category} bottle of {self.volume} liters."
    
    def write(self):
        with open(self,"a") as write_elem:
            new_line = input("Please write the Drink name, its type plus the container and volume it's sold in separated by a comma: ")
            write_elem.write('\n' + new_line)