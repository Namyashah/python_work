'''
#1
class Addition :
    def add(self,n):
        print(n+n)
class Concat(Addition) :
    def add(self,n) :
        if type == 'int':
            print(n+n)
        else :
            super().add(n)
c1 = Concat()
c1.add("namya")

#2
class shape :
    def __init__(self) :
        self.width = 20
        self.length = 40
        self.pie = 3.14
    def area(self):
        pass
class rectangle(shape):
    def area(self):
        self.length = float(input("Enter the value of length of rectangle = "))
        self.width = float(input("Enter the value of width of rectangle = "))
        print(f"The area of rectangle is {self.length*self.width}")
        pass
class circle(shape):
    def area(self):
        self.width = float(input("Enter the value of width of circle = "))
        print(f"The area of circle is {self.width*self.pie}")
        pass

c2 = rectangle()
c2.area()
c1 = circle()
c1.area()

#3
class demo:
    def __init__(self):
        self.string = "asdfghjk"
    def you(self):
        if isinstance(self.string,str):
            print(len(self.string))
        else :
            print("Self.string is not an string")
class namya(demo):  
    def you(self):
        self.lst = [3,4,5,6,7,6,5,4]
        if isinstance(self.lst, list):
            print(len(self.lst))
        else :
            print("It is not supported")
class ton(demo):
    def you(self):
        self.dct = {"a":10,"b":"demo","c":20,"d":"yug"}
        if isinstance(self.dct,dict):
            print(len(self.dct))
        else :
            print("It is not supported")
        super().you()
    
c1 = ton()
c2 = namya()
c1.you()
c2.you()

#4
class Transport:
    def travel(self):
        self.distance_km = None
        self.price = None
        self.destination = None
class train(Transport):
    def travel(self):
        self.distance_km = int(input("Enter the KM = "))
        self.price = int(input("Enter the price = "))
        self.destination = input("Enter the destination")
        print(f"The distance is {self.distance_km} the price is {self.price} and the destination is {self.destination}")
class plane(Transport):
    def travel(self):
        self.distance_km = int(input("Enter the KM = "))
        self.price = int(input("Enter the price = "))
        self.destination = input("Enter the destination")
        print(f"The distance is {self.distance_km} the price is {self.price} and the destination is {self.destination}")
        
C1 = train()
C1.travel()
C2 = plane()
C2.travel()

#5
class calculator:
    def method(self) :
        print("Hello i am method my job is to plus anything!!!")
    def method(self,a,b,run) :
        run = a+b
        print(f"hello The sum of {a} and {b} is {run}")
c1 = calculator()
c1.method()
c1.method(12,34)

#6
class animal:
    def speak(self):
        sound = None
class dog(animal):
    def speak(self):
        sound = input("Enter the sound of dog = ")
        print(f"The sound of dog is {sound}")
class cat(animal):
    def speak(self):
        sound = input("Enter the sound of cat = ")
        print(f"The sound of cat is {sound}")

c1 = dog()
c1.speak()
c2 = cat()
c2.speak()

#7
class shape :
    def __init__(self) :
        self.width = 20
        self.length = 40
        self.pie = 3.14
    def area(self):
        pass
class rectangle(shape):
    def area(self):
        self.length = float(input("Enter the value of length of rectangle = "))
        self.width = float(input("Enter the value of width of rectangle = "))
        print(f"The area of rectangle is {self.length*self.width}")
        pass
class circle(shape):
    def area(self):
        self.width = float(input("Enter the value of width of circle = "))
        print(f"The area of circle is {self.width*self.pie}")
        pass

c2 = rectangle()
c2.area()
c1 = circle()
c1.area()
'''
    