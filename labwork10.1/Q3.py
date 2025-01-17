import os
answer = os.getcwd()
os.chdir("..")
os.chdir("source")
answer1 = os.getcwd()

print(answer)
print(answer1)