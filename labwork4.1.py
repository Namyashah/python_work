'''
#1
#(Write a Python program that uses at least five built-in functions (e.g., len, max,
sorted), sum), and type) to perform operations on a list of numbers.)
number = [1,2,3,4,5,6,7]
print(len(number))
print(max(number))
print(min(number))
print(sum(number))
print(type(number))

#2
#(Create a user-defined function (UDF) that calculates the factorial of a given number.)
n = [2,3,4,5,6]
def emp():     
    num = [i**2 for i in n ]
    return num
            
z = emp()
print(z)

#3
#(Implement a program where a UDF accepts a list of integers and returns the square of
each integer in a new list using a list comprehension.)
def factorial(n):
    fact = 1
    for i in range(1,n+1) :
        fact *= i
    return fact
        
num = int(input(""))
z = factorial(num)
print(z)

#4
#(Write a UDF that takes a string as input and returns the frequency of each character in
the string as a dictionary.)
def name(n):
    ditto = {}
    for char in n:
        if char in ditto :
            ditto[char] += 1
        else:
            ditto[char] = 1
    return ditto
tour = input("")
z = name(tour)
print(z)

#5
#(Create a program that takes a user-defined function as an argument to calculate the
cube of a list of numbers.)
def cube(v):
    return v**3
def name2(ton,numbers):
    return [ton(i) for i in numbers]

num = [3,4,5,6,7]    
z = name2(cube,num)
print(z)

#6
#(Write a Python function that accepts an arbitrary number of integer arguments and
returns their sum and product.)
def nam(*demo):
    sum  = 0
    for i in demo:
        sum = sum +i
    return sum
def nam1(*demo):
    sum = 1 
    for i in demo:
        sum = sum*i
    return sum
z = nam(2,3,4,6,7)
w = nam1(2,3,4,6,7)
print(z)
print(w)

#7
#(Implement a function that takes a list of student names using *args and prints each
name on a new line.
- Add functionality to check if the list is empty and display a suitable message.)
def std(*demo):
    if demo==():
        print("The student list is empty")
    else :
        for i in demo :
            print(i)

std("namya","yug","jugal","rahi","vansh","rahul")

#8
#(Develop a program where a UDF accepts *args and filters out the strings from the
arguments.
- Return a tuple of filtered values (e.g., strings in one tuple, numbers in another).)
def namya(*args):
    t1 = []
    t2 = []
    for i in args :
        if type(i)==str :
            t2.append(i) 
        elif type(i)==int :
            t1.append(i) 
    return t1,t2
t1,t2 = namya(int(input("")),int(input("")),int(input("")),input(""),input(""))
print(t1)
print(t2)

#9
#(Write a function that accepts **kwargs to print out a formatted description of a person
#(e.g., name, age, city).)
def person(**kwargs):
    for i in kwargs.items():
        print(i)

person(name = input(""),age = int(input("")),city = input(""))
''' 