
class Drinks:
    def __init__(self,name,container,volume):
        self.name = name
        self.container = container
        self.volume = volume
        
    def __repr__(self):
        return f"{self.name} comes in a {self.container} bottle of {self.volume} liters."
    
    def write(self):
        with open(self,"a") as write_elem:
            new_drink = input("Please write the drink name: ")
            new_container = input("Please write the container type: ")
            new_volume = input("Please write the volume of the container in liters: ")
            write_elem.write('\n' + new_drink + "," + new_container + "," + new_volume)