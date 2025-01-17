import os
answer = os.getcwd()
os.chdir("..")
answer1 = os.listdir()
os.mkdir("practise_task")
os.rmdir("practise_task")
print(answer)
print(answer1)