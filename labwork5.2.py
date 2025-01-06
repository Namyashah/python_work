'''
#1
class forza:
    def __init__(self):
        self.a = input("Enter your car = ")
    def display(self):
        print(f"My first car is {self.a}")
class horizan(forza):
    pass

alpha = horizan()
alpha.display()

#2
class headmaster:
    def __init__(self):
        self.ID = int(input("Enter the ID number = ")) 
        self.name = input("Enter the name of teacher = ")
    def getdata(self):
        print(f"The ID of headmaster is {self.ID} and name is {self.name}")
class admin(headmaster):
    pass
class teacher(headmaster):
    pass
    
G1 = admin()
G2 = teacher()
G1.getdata()
G2.getdata()

#3
class grandparent:
    def __init__(self):
        self.number = int(input("Enter the number of balance = "))
    def balance(self):
        print(f"The amount of balance grandparent has is {self.number}")
class parent(grandparent):
    def assault(self):
        print("The total amount of asset is 1000")
class child(parent):
    def getdata(self):
        print("I have nothing sorry!!")
        
beta = child()
beta.balance()
beta.assault()
beta.getdata()
    

#4
class animal:
    def __init__(self):
        self.veg = input("Enter whether an animal is vegitarian or not = ")
        self.colour = input("Enter the color = ")
        print(f"The animal is {self.veg} and color is {self.colour}")
class dog(animal):
    def getdata(self) :
        print("My breed is a dog")
class cat(animal):
    def dunk(self) :
        print("My breed is a cat")
        
gama = dog()
gama.getdata()
gama2 = cat()
gama2.dunk()

#5
class a :
    def namya(self):
        print("My name is namya")
        
class b(a) :
    def demo(self):
        print("My is name demo")
        
class c(b) :
    def league(self):
        print("My name is unique")
        
class d :
    def tinder(self):
        print("Hello i am not usable")
        
class e :
    def namya(self):
        print("My name is not supportable")
        
class f(d,e,c) :
    def toy(self):
        print("I am a toy")
        super().namya()
        
delta = f()
delta.namya()
delta.demo()
delta.tinder()
delta.league()
delta.toy()

#6
number = int(input("Enter the number = "))
print(type(number))
num = float(input("Enter the num = "))
print(type(num))

#7
num = int(input("Enter the number = "))
print(id(num))
number = int(input("Enter the number = "))
print(id(number))

#8
class demo :
    pass
print(dir(demo))

#9
class demo :
    pass
    
D1 = demo()
a = isinstance(D1,demo)
print(a)

#11
class square:
    def __init__(self) :
        self.number = int(input("Enter the number = "))
    def getdata(self) :
        print(f"The square of a number is {self.number*self.number}")
    class cube:
        def __init__(self) :
            self.num = int(input("Enter the number = "))
        def getdata(self) : 
            print(f"The cube of a num is {self.num*self.num*self.num}")
        
game = square()
game.getdata()

toy = game.cube()
toy.getdata()

#12
class string:
    def __init__(self):
        self.gun = input("Enter the string input = ")
    class length:
        def __init__(self,yoyo):
            self.koko = yoyo.gun
        def getdata(self):
            rohan = len(self.koko)
            print(f"The lenght of string input is {rohan}")
            
rowdy = string()

new = string.length(rowdy)
new.getdata()
'''