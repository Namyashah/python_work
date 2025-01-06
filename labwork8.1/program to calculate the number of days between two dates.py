import datetime
dot = datetime.date(day=5,month=8,year=2006)
print(dot)
dot1 = datetime.date(day=25,month=8,year=2006)
print(dot1)
print(dot1 - dot)
dot2 = datetime.date.today()
print(dot2 + datetime.timedelta(days=7))