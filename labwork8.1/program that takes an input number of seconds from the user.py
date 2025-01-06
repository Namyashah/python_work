import time
second = int(input("Enter your timer = "))
for i in range(second,0,-1):
    print(i)
    time.sleep(1)
print("Your timer is completed!!")