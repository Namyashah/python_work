import subprocess as sub
answer = sub.Popen(["wc","-l"])
print(answer)