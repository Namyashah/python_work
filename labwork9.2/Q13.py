import sys
input = sys.argv
lst_number = input[1]
print(lst_number)
sum = 0
for i in lst_number:
    try:
        num = int(i)
        sum = sum + num
    except ValueError as e:
        print(f"Non - Numeric {i} are Not Allowed!!")
print(f"The sum of All Digit is {sum}")
