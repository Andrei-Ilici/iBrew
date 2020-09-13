
class Order:
    def __init__(self,name,drink):
        self.name = name
        self.drink = drink
    
    def __repr__(self):
        return f"{self.name} wants to order a {self.drink}."