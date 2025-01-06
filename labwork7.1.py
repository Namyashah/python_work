'''
#1
#(Write a Python program to create a text file named sample.txt.
#Write the sentence "Python is a versatile programming language." into the file.)
file = open("Sample.txt","x")
file.write("Python is a versatile programming language")
file.close()

#2
#(Write a Python program to open an existing file in read mode and display its content.
#Open the file in write mode, overwrite the content, and write a new sentence
#"Learning file handling in Python is fun!").
file = open("Sample.txt","r")
print(file.read())
file.close()

toy = open("Sample.txt","w")
toy.write("Learning file handling in Python is fun!!")
toy.close()

#3
#(Write a Python program to read and print the contents of the file sample. txt line by line.)
file = open("Sample.txt","w+")
for i in range(1,6):
    file.write("My Name is Namya!!\n")
    
file.seek(0)

for i in file :
    print(file.read())
file.close()

#4
#(Create a Python program that writes multiple lines of text to a file named notes.txt. The content should be:
#Line 1: Python is easy to learn.
#Line 2: It has numerous libraries.
#Line 3: File handling is one of its features.)
file = open("notes.txt","a")
file.write("Python is easy to learn\n")
file.write("It has numerous libraries\n")
file.write("File handling is one of its features")
file.close()

#5
#(Write a Python program to append "Line 4: Python supports multiple modes of file
#handling." to the file notes.txt.)
file = open("notes.txt","a")
file.write("\n  Python supports multiple modes of file handling")
file.close()

#6
#(Write a Python program to open a file in binary mode.
#Use rb mode to read the content of a text file and display its content in binary#ormat.)
file = open("images.jpg","rb")
print(file.read())
file.close()

#7

#8
#(Write a Python program to open a text file in read-write mode. Read the existing content.
#Append the line "This file was last modified by adding this sentence." to the file.)
file = open("Sample.txt","+r")
print(file.read())
file.write("\nThis file was last modified by adding this sentence")
file.close()

#9
#(Create a Python program that takes a word as input and searches for it in sample.txt.
#If found, display the line number(s) where the word appears.)
word = input("Enter the word = ")
file = open("Sample.txt","r")
number = 1
num = []

for i in file:
    if word in file :
        num.append(number)
    number += 1
    
file.close()
if num :
    print(f"The word {word} is found in number {num}")
else :
    print(f"The word {word} is not found on this txt")
    
#10
#(Write a Python program to read content from an existing file source. txt and copy it to a
#new file backup.txt.)
file = open("Sample.txt","r")
content = file.read()
file.close()

folder = open("notes.txt","w")
folder.write(content)
file.close()

print(f"Data copied from file sample.txt to notes.txt")

#11
#(Create a Python program to demonstrate all modes (r, w, a, rt, wt, at). For each mode:
#Open a file, Write or read content depending on the mode. Close the file properly.)
#file = open("Sample.txt","r")
#print(file.read())
#file.close()

#file = open("notes.txt","w")
#file.write("Hello! I am Namya Shah ")
#file.close()

#file = open("demo.txt","a")
#file.write("Hello\n")
#file.write("I am Namya Shah\n")
#file.write("I love to play criket\n")

#file = open("demo2.txt","+r")
#print(file.read())
#file.write("Data\n")
#file.write("thank you\n")
#file.write("byeee\n")

#file = open("demo3.txt","w+")
#file.write("I am namya shah\n")
#file.write("I am namya shah\n")
#file.write("I am namya shah\n")
#file.seek(0)
#print(file.read())

#file = open("demo4.txt","a+")
#file.write("\nheloo\n")
#file.write("heloo\n")
#file.write("heloo")
#file.seek(0)
#print(file.read())
'''