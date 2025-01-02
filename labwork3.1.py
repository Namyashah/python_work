'''
#1
#(Write a Python program to: Take a user's first name and last name as input.
#Print them in the format: Hello. [Last Namel. [First Namel!)
First_name = input("first name = ")
Last_name = input("last name = ")

print("Hello!",[First_name],[Last_name],"!")

#2
#(Create a program to: Format and display the following sentence: "The price of {item) is {price} dollars."
#Replace {item} with "apple" and (price) with 5.50 using f-strings.)
item = "apple"
price = 5.50
print(f"The price of {item} is {price} dollors")

#3
#(Implement a program to: Take a string as input.
#Print the string reversed and also print whether it is a palindrome.)
string = input("")
a = string[::-1]
if a==string :
    print("It is palindrome")
else :
    print("It is not palindrome")
    
#4
#(Create a program that:
- Takes a string input from the user.
- Converts the string to uppercase, lowercase, and title case.)
string = input("")
a = string.upper()
print(a)

a = string.lower()
print(a)

a = string.title()
print(a)

#5
#(Write a Python program to:
- Create a list of integers from 1 to 10.
- Append a new number to the list and print the updated list.)
namya = [i for i in range(1,11)]
print(namya)
namya.append(11)
print(namya)

#6
#(Create a program to:
- Take a list of numbers as input from the user.
- Find and print the largest and smallest number in the list.)
a = int(input(""))
numbers = [i for i in range(1,a)]
print(numbers)
numbers.reverse()
print(numbers)
print(max(numbers))
print(min(numbers))

#7
#(Implement a program that:
- Creates a tuple with some duplicate values (e.g., (1, 2, 2, 3, 4, 4, 5)).
- Prints the unique values from the tuple.)
tuple = (1,2,2,3,3,4,5,5,5,6,6,7)
z = tuple 
z = set()
z = tuple(z)
print(tuple)

#8
#(Write a Python program to:
- Create a list of 5 integers.
- Modify the third element of the list and print the updated list.)
a = int(input(""))
lst = [i for i in range(1,a)]
print(lst)
lst[3] = 'namya'
print(lst)

#9
#(Write a program to:
- Create a list with nested elements (e.g., [1, [2, 3], 4]).
- Modify the inner list and print the updated list.)
a = [1,2,3]
a.append([22,33,44,55])
a.append(["namya"])
print(a)
a[3] = ["hiiiiii"]
print(a)

#10
#(Create a Python program that:
- Demonstrates adding, removing, and replacing elements in a list.
- Explain why this is not possible with tuples.)
lst = [1,2,3,4,5,6,7,8,9]
lst.append(10)
lst.remove(3)
lst[1] = '20'
print(lst)

#this are not suitable for tuples because they are immutable and list are not .

#11
#(Implement a program to:
- Create a tuple of 3 lists (e.g., ([1, 2], [3, 4], [5, 6])).
- Modify one of the inner lists and explain how it does not violate tuple immutability.)
tuple = ([1,2,3],[4,5,6],[7,8,9])
tuple[0] = [1,2,3,4,5,6,7]
print(tuple)
#tuple is only meant for seeing and it is not used for modifying data or tuple.

#12
#(Write a program to:
- Swap two variables with each other using a third variable.)
a = [23,56,56,78,43]
b = [84,36,45,78,23]
a = b
a.append(87)
print(a)
print(b) 

#13
#(Write a program to:
- Swap two variables with each other without using a third variable.)
a = [23,56,56,78,43]
b = [84,36,45,78,23]
a = b.copy()
b.append(100)
print(a)
print(b)
'''