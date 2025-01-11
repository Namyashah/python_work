'''
#1
num = int(input("Enter the number you want = "))
if num>=0 :
    print(f"The number is {num}")
else :
    raise ValueError("The user has entered negative input.")    

#2
def check_even(number):
    if type(number)==int :
        if number%2==0 :
            print("The number is even!!!")
        else :
            raise ValueError("The number is Odd")
    else :
        raise TypeError("The input is not an integer")
        
check_even(12)    

#3
age = int(input("Enter your age = "))
assert age>18,"The age should be above 18"
print(f"The age of yours is {age}")

#4
def check_palindrome(string):
    assert len(string)>0,"Your string is empty "
    print("The number is palindrome")
    
check_palindrome(input("Enter the input = "))

#5
class InsufficientBalanceError(Exception):
    pass
balance = 50000
def withdrawal(get):
    if get<balance:
        print("The amount has been withdran!!")
    else :
        raise InsufficientBalanceError("The amount is greater than balance amount")
withdrawal(int(input("Enter the amount you want to withdran = ")))    

#6
class InvalidEmailError(Exception):
    pass
    
def validate_Email():
    email = input("Enter the email = ")
    if "@" or ".com" not in email :
        raise InvalidEmailError("The email does not contain @ or .com or .org")
    else :
        print(f"Your email is {email}")
        
validate_Email()

#7
class InvalidGradeError(Exception):
    pass
    
def grade_student():
    grade_input = input("Enter the grade the student have = ").strip()
    assert len(grade_input)>0,"The grade is empty sorry"
    print("[You can go ahead]")
    grade = int(grade_input)
    
    if grade>=1 and grade<100:
        print(f"The grade of a student is {grade}")
        if grade<40 :
            raise InvalidGradeError("Failing grade")
    else :
        raise ValueError("The grade you haved enter are out of range ")
grade_student()

#8
class HighTemperatureError(Exception):
    pass
    
def conversion(num):
    if type(num)==int:
        print(f"The number is {num} and integer")
    else :
        raise TypeError("The input is not an integer")
    assert num>-273 and num<=10000,"The tempeature is out of range"
    print("You can go ahead")
    if num>1000 :
        raise HighTemperatureError("The Tempareture is unrealistic")
    
conversion(int(input("Enter the number you want = ")))
'''