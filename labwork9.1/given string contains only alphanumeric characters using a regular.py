import re
data = input("Enter your data = ")
q = r"^[a-zA-Z0-9]+$"

answer = re.match(q,data)
if answer != None:
    print("The string is Valid")
else:
    print("The string is Not Valid")