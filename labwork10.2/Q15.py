import functools
number = [23,56,787,65,98,35,67]
def largest(x,y):
    return x if x>y else y

answer = functools.reduce(largest,number)
print(answer)