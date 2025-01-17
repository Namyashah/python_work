number = [1,2,3,4,5,6,7,82,3,464,74,644,453]
def even(num):
    if num%2==0:
        return num
answer = list(filter(even,number))
print(answer)