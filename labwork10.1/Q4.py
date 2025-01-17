import os 
folder = input("Enter the folder = ")
if os.path.exists(folder):
    print("Folder Already Exists!!")
else:
    os.mkdir(folder)