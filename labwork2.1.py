'''
#1
#Write a Python program to: Take a number as input from the user.
#Use an 'if-else' statement to check if the number is even or odd and print the result.
a = int(input(""))
if a%2==0 :
    print("a is even")
else :
    print("b is odd")   
    
#2
#(Create a program that: Accepts a user's age as input.
#Uses nested 'if-else statements to categorize the user into age groups:
#Child (0-12)
#Teenager (13-19)
#Adult (20-59)
#Senior (60+))
Age = int(input("Enter the Age = "))
if Age <60 :
    if  Age <=12:
        print("You are Child")
    elif Age <=19:
        print("You are a Teenager")
    else :
        print("Yuo are Adult")
else:
    print("You are a Senior")
        
#3
#(Implement a program that: Takes three integers as input.
#Uses an 'if-elif-else' statement to find and print the largest number.)
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))

if a > b:
    if a > c:
        print("a is max")
    elif c > a:
        print("c is max")
    else:
        print("a and c are the same and the largest")
elif b > c:
    if b > a:
        print("b is max")
    else:
        print("b and a are the same and the largest")
elif c > b:
    print("c is max")
elif b == c == a:
    print("all are the same")
else:
    print("b and c are the same and the largest")
       
#4
#(Write a Python program using a 'switch-case' equivalent to:
#Take an operator (+*, -, ***, */') as input.
#Perform the corresponding operation on two numbers entered by the user.)
a = int(input("Enter the number a = "))
b = int(input("Enter the number b = "))
choice = input("Enter the choice = ")
if choice == '+' :
    result = a + b
    print("the sum is =  ",result)
elif choice == '-' :
    result = a - b
    print("The sub is :-- " ,result)
elif choice == '*' :
    result = a * b
    print("The multipication  is :-- " ,result)
elif choice == '/':
    if a != 0:  
        result = a / b
        print("The result of division is:--   ",result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

#5
#(Write a program using a while loop to:
#Take numbers as input from the user until they enter 'O'.)
i = int(input("enter the number = "))
while i <= 10:
    print(i)
    i += 1


#6
#(Create a program using a 'for' loop to: Iterate over a given range(1 to 10).
#Print each digit's square, one per line.)
for i in range (1,11,1):
    print(i)
print()
for i in range (1,11,1):
    print(i**2)

#7
#(Write a program to: Use a 'while' loop to print all even numbers between 1 and 50.)
i = 1
while i <= 50:
    if  i%2 == 0:
        print(i)
    i = i + 1

#8
#(Write a program to: Use the 'rangel)' function to generate a sequence of numbers from 1 to 20.
#Print only the odd numbers using a 'for' loop.)
for i in range (1,21,1):
    print(i)
print()
for i in range (1,21,1):
    if i%2 == 1:
        print(i)

#9
#(Implement a program that:Uses the rangel' function with three arguments (start, stop, step) to print multiples
#of 5 from 5 to 50.)
for i in range (5,51,5):
    print(i)

#10
#(Create a program using a 'for' loop and rangel' to: Print a reverse countdown from 10 to 1.)
for i in range (10,0,-1):
    print(i)

#11
#(Write a program that: Uses a 'for' loop and rangel' to iterate through numbers from 1 to 50.
#Checks if each number is divisible by 2, 3, or both using nested 'if-elif-else'.
#Prints messages for each case (e.g., "Divisible by 2", "Divisible by 3", "Divisible by both"').)
for i in range(1,51):
    if i%2 == 0 and  i%3 == 0:
        print(i,":-Both are divisible by 2 and 3")
    elif i%2 == 0 and i%3 != 0:
        print(i,":-The number is divisible by 2")
    elif i%2 != 0 and i%3 == 0:
        print(i,":-The number is divisible by 2")
    else:
        print(i)
'''