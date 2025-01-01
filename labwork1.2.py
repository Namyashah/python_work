'''
#1
#(Write a program to demonstrate different formatting options in print):
#Use sep to separate values with a custom character.
#Use end to customize what appears at the end of a print) statement.)
print("mango","strawberry","apple","orange",sep = "^")
print("hiii",end = "_______")
print("hello world",end = "__#$@%")
print()

#2
#(Create a program that asks the user for their name, age, and favourite hobby using the
#input) function, then displays a formatted message like:
#"Hello, ‹name>! At <age>, enjoying < hobby> sounds fun!")
Name = input("")
Age = int(input(""))
Hobby = input("")
print("Hello",Name,"!","At",Age,"enjoying",Hobby,"sounds fun!")

#3
#(Perform addition, subtraction, multiplication, division, floor division, modulus, and
#exponentiation on two numbers input by the user.)
a = int(input(""))
b = int(input(""))

print("addition = ",a+b)
print("subtraction = ",a-b)
print("multiplications = ",a*b)
print("division = ",a//b)
print("modules = ",a%b)
print("exponentiation = ",a**2,b**2)

#4
#(Create a program where the user inputs their height and weight.
#Store them in appropriately named variables and print a formatted message
#displaying their values.)
Height = int(input(""))
Weight = int(input(""))

measurements = "Height = ",Height,"Weight",Weight
print(measurements)


#5
#(Implement a program to demonstrate logical operators (and, or, not) by asking the uses
#for boolean inputs (e.g., true/false values).)
a = int(input(""))
b = int(input(""))

if a==1 and b==2 :
    print("hiii")
elif a==3 or b==5 :
    print("byeee")
else :
    print("nothing")  

#6
#(Write a program to demonstrate assignment operators (=, +=, =, *=, /=) using a single variable.)
a = int(input(""))

a = a+1 
print(a)
a = a-1
print(a)
a = a*2
print(a)
a = a//2
print(a)
'''