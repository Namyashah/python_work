import sys
user = int(input("Enter your number = "))
if user==0:
    print("You Have Successfully Passes The Exam!!")
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    print(a+b+c)
elif user==1:
    sys.exit("You Haved Failed The Exam!!")
else :
    print("Enter proper Input!!")