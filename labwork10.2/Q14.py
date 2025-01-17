import functools
number = [1,2,3,4,5]
def product(x,y):
    return x*y

answer = functools.reduce(product,number)
print(answer)