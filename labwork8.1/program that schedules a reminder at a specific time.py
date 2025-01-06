import time
import datetime as e
dot = e.time(hour=int(input("")),minute=int(input("")),second=int(input("")))
for i in range(dot.hour,dot.minute,dot.second):
    print(i)
    time.sleep(1)
print("Your timer is completed!!")