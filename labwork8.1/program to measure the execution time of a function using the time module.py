import time
start = time.time()

for i in range(1,1000):
    a = 0
    a += (i**100)
    print(i)

end = time.time()

print(f"The execution Time between two Programs is {end-start}")