'''
#1
#(Write a Python program to demonstrate the use of type casting constructors (intO,floatO, str, and bool):
#Take input from the user as a string.
#Convert the string into an integer, a float, and a boolean.
#Print the converted values along with their types.)
a = input("")
b = int(a)
print(type(b))

b = float(a)
print(type(b))

a = input("")
boolvalue = a.lower() == a  
print(boolvalue)
  
#2
#(Write a program where the user inputs a floating-point number.
#Convert this number into an integer using intO and print both values with a
#message explaining the difference.)
a = float(input(""))
b = int(a)
print(b)
print(type(b))
print(a)
print(type(a))

#3
#(Create a program that: Takes a boolean value (True or False) as input.
#Converts the boolean to an integer and a string, and prints all three values.)
bool_value = input("bool = ")
if bool_value=="True" :
    bool_value = True 
elif bool_value=="False" :
    bool_value = False
else :
    raise ValueError("Invalid boolean value! Please enter True or False.")

str_value = str(bool_value)
int_value = int(bool_value)
print(str_value)
print(int_value)
print(bool_value)

#4
#(Write a Python program to: Declare a variable of each datatype (integer, float, string, boolean, list, tuple,
#dictionary).
#Print the value, type (using type®), and memory address (using idO) of each variable)
a = int(input(""))
print(a)
print(type(a))
print(id(a))

a = float(input(""))
print(a)
print(type(a))
print(id(a))

a = input("")
print(a)
print(type(a))
print(id(a))

bool_value = input("bool = ")
if bool_value=="True" :
    bool_value = True 
elif bool_value=="False" :
    bool_value = False
print(bool_value)
print(type(bool_value))
print(id(bool_value))

lst = [1,2,3,4,5,6,7]
print(lst)
print(type(lst))
print(id(lst))

tple = (2,3,4,5,6,7)
print(tple)
print(type(tple))
print(id(tple))

dict = {"key":1,"keys":2}
print(dict)
print(type(dict))
print(id(dict))

#5
#(Create a program that: Declares two variables with the same value.
#Prints their memory addresses using id and checks if they are the same.
#Modifies one of the variables and checks the memory addresses again.)
a = int(input(""))
b = float(input(""))
print(id(a))
print(id(b))
'''