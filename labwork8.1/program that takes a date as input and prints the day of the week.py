import datetime
dot = datetime.date(day=int(input("")),month=int(input("")),year=int(input("")))
date_str = dot.strftime("%A-%m-%Y")
print(date_str)