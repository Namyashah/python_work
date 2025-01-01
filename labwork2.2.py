'''
#1
#(Write a Python program that: Uses a for loop to print numbers from 1 to 20.
#Skip numbers divisible by 4 using the continue statement).
for i in range(1,21):
    if i%4==0 :
        continue
    print(i)
    
#2
#(Implement a program using a while loop to: Print numbers from 1 to 10.
#Stop the loop using the break statement when the number is 7.)    
i = 1
while 1<=10:
    if i==7 :
        break
    print(i)
    i = i+1
    
#3 
#(Create a program that: Iterates over a string (e.g., "PYTHON").
#Uses a continue statement to skip vowels and print only consonants.)   
str = "PYTHON"
for i in str :
    if i=="A" or i=="a" or i=="E" or i=="e" or i=="I" or i=="i" or i=="U" or i=="u" or i=="O" or i=="o" :
        continue
    print(i,end = "")
    
#4
#(Write a Python program to: Generate a list of cubes for numbers between 1 and 10 using list
#comprehension.)
lst = [i**3 for i in range(1,11)]
print(lst)

#5
#(Implement a program to: Create a list of all even numbers from 1 to 50 using list comprehension.)
lst = [i for i in range(1,51) if i%2==0]
print(lst)

#6
#(Create a program that:Takes a list of words as input.
#Use list comprehension to create a new list containing only words that start with a vowel.)
vowels = []
words = ["namya","yug","rahi","kashvi","heet","ougal"]
alpha = [i for i in words if i=="A" or i=="a" or i=="E" or i=="e" or i=="I" or i=="i" or i=="U" or i=="u" or i=="O" or i=="o"]
vowels.append(alpha)
print(vowels)