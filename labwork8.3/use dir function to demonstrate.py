import math 
print(dir(math))
print()
print()
class Person :
    def __init__(self):
        self.name = input("Enter your name")
        self.age = int(input("Enter your age = "))
    def welcome(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")
    def exit(self):
        print("Goodbyee!!")
p1 = Person()
print()
print()
print(dir(p1))