'''
#1
#(Develop a program that divides two numbers provided by the user. 
#Use try … except to handle division by zero)

def div(num1,num2):
    if num1//num2>0 :
        divi = num1//num2
        print(f"The Division of Both numbers are {divi}")
    else :
        raise ZeroDivisionError("Numbers are not divisable by Zero")
try :
    div(6,12)
except ZeroDivisionError as e :
    print(f"Not Possible Because of {e}")
except :
    print("General Exception Block!!!")

#2
#(Write a program that tries to access an element in a list at a non-existent index 
#Handle the exception using try … except)

def function(taken):
    try :
        choice = int(input("Enter your index choice = "))
        if choice<len(taken):
            print(f"The Index value of your choice is {choice}")
        else :
            raise IndexError("Your list doesn't have such index range!!")
    except IndexError as e :
        print(f"Not Possible of {e}")
    except :
        print("General Exception Block!!!")
        
function([1,2,3,4,5])

#3
#(Write a program to input a filename from the user, read its content, and handle any file-related exceptions. 
#Use the else block to print the file content if no exception occurs.)

def file(clerk):
    try :
        with open(clerk,"r") as file :
            content = file.read()
    except FileNotFoundError as e :
        print("File does not exist!!")
    except :
        print("General Exception Block!!!")
    else :
        print(content)
    
file(input("Enter the File name = "))

#4
#(Write a program that tries to access an element in a string at a non-existent index. 
#Handle exceptions, and use the else block to print the result if no exception occurs)

def demo(turbulance):
    element = input("Enter the element you want access of = ")
    try :
        if element not in turbulance:
            raise IndexError("The element does not exist in the string!!")
        else :
            print(f"The element of your choice is {element}")
    except IndexError as e :
        print(f"Not Possible Because of {e}")
    except :
        print("General Exception Block!!!")
    else :
        print(turbulance)
demo(input("Enter the string please = "))

#5
#(Write a program that opens a file
#handles any exceptions if the file doesn’t exist, and ensures the file is closed using the finally block)

def read_file(filename):
    file = None
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File does not exist!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if file:
            print("File closed successfully!")
read_file(input("Enter the file name: "))

#6
#(Create a program that performs division. 
#Handle exceptions for invalid inputs and ensure a final message is displayed using the finally block
#regardless of the outcome)

def division():
    try:
        a = int(input("Enter your number a = "))
        b = int(input("Enter your number b = "))
        c = a//b
        if c==0:
            raise ZeroDivisionError("Any number Should Not Be Divided By Zero!!")
        else :
            print(f"The Division of a and b is {c}")
            print("================================================================")
    except ZeroDivisionError as e:
        print(f"Not Possible Because {e}")
    except:
        print("General Exception Block!!!")
    finally:
        print("The Division is Performed Successfully.Thank You For Using It!")

division()

#7
#Write a program that prompts the user to enter a number and attempts to find its square root.
#Use try to handle invalid input (e.g., negative numbers), else to print the square root if
#successful, and finally to display a message like "Execution complete."

def square():
    try:
        number_square = int(input("Enter the Number You Want Square Root of = "))
        n = int(input("Enter the correspondence number = "))
        if number_square>0:
            square_number = number_square//n
            print(f"The Square Root Of {number_square} is {square_number}")
            print("=========================================================")
        else:
            raise ValueError("The Number Should Be Positive.")
    except ValueError as e:
        print(f"Not Possible Becuase {e}")
    except:
        print("General Exception Block!!!")
    finally:
        print("Execution Complete!!!")

square()
'''