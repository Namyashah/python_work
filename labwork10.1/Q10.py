import os 
file = input("Enter the file name = ")
if os.path.exists(file):
    print("File Exists!!")
else :
    print("File Created Successfully!!")