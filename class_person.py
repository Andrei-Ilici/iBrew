
class Person:
    def __init__(self,first_name,surname,age):
        self.first_name = first_name
        self.surname = surname
        self.age = age
    
    def __repr__(self):
        return f"{self.first_name} {self.surname} is {self.age} years old."
    
    def __getitem__(self,first_name):
        return self.first_name[first_name]