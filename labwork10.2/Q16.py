import functools
number = [1,2,3,4,5,6,7]
def filter_program(x):
    if x%2==0:
        return x    
answer = list(filter(filter_program,number))
print(answer)
def map_program(x):
    return x**2
answer1 = list(map(map_program,answer))
print(answer1)
def reduce_program(x,y):
    return x+y
answer2 = functools.reduce(reduce_program,answer1)
print(answer2)