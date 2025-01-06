import datetime
dot = datetime.datetime.now(datetime.timezone.utc)
dot1 = datetime.datetime.now().astimezone()
print(type(dot))
print(type(dot1))