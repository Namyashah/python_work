import os
file = open("old.txt","x")
os.rename("old.txt","new.txt")
os.remove("new.txt")