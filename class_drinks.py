
class Drinks:
    def __init__(self,name,category,volume,price):
        self.name = name
        self.category = category
        self.volume = volume
        self.price = price
        
    def __repr__(self):
        return f"{self.name} is a {self.category} drink sold in a bottle of {self.volume} liters for £{self.price}."
    
    def __getitem__(self,name):
        return self.name[name]
    # def write(self):
    #     with open(self,"a") as write_elem:
    #         new_drink = input("Please write the drink name: ")
    #         new_container = input("Please write the container type: ")
    #         new_volume = input("Please write the volume of the container in liters: ")
    #         write_elem.write('\n' + new_drink + "," + new_container + "," + new_volume)