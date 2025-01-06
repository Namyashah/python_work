import datetime
datetime_str = input("Enter your date = ")
object_datetime = datetime.datetime.strptime(datetime_str,"%d-%m-%Y")
print(type(object_datetime))
print(object_datetime)

dot = datetime.date.today()
print(dot)
date_str = dot.strftime("%d-%m-%Y")
print(type(date_str))
print(date_str)