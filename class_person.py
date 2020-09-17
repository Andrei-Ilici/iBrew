
class Person:
    def __init__(self,first_name,surname,age):
        self.first_name = first_name
        self.surname = surname
        self.age = age
    
    def __repr__(self):
        return f"{self.first_name} {self.surname} is {self.age} years old."
    
    def write(self):
        with open(self,"a") as write_elem:
            new_first_name = input("Please write the person first name: ") 
            new_surname = input("Please write their surname: ")
            new_age = input("Please write their age: ")
            write_elem.write('\n' + new_first_name+ ","+ new_surname+ ","+ new_age)