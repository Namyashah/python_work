import datetime
dot = datetime.datetime(day= int(input("")),month= int(input("")),year= int(input("")),hour= int(input("")),minute= int(input("")),second= int(input("")))
print(dot)

date_str = dot.strftime("%d-%m-%Y")
print(date_str)
date_str1 = dot.strftime("%m-%d-%Y")
print(date_str1)
time_str = dot.strftime("%H-%M-%S")
print(time_str)
time_str1 = dot.strftime("%I-%M-%S")
print(time_str1)