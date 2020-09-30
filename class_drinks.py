
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