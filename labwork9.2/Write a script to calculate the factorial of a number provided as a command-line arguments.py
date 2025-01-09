import sys
input = sys.argv
number = int(input[1])
fact = 1
for i in range(1,number+1):
    fact *= i
print(f"The Factorial is : {fact}")