import subprocess as sub
lst = [(1,"apple"),(2,"cherry"),(3,"banana")]
answer = sorted(lst,key=lambda x: x[1])
print(answer)