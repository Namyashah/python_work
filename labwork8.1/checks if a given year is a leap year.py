import datetime
dot = datetime.datetime(day=int(input("")),month=int(input("")),year=int(input("")))
date = dot.year
if dot.year%4==0:
    print(f"{dot.year} is a leap year!")
    if dot.year%100==0:
        print(f"{dot.year} is a leap year!")
        if dot.year%400==0:
            print(f"{dot.year} is a leap year!")
        else :
            print(f"{dot.year} is not a leap year!")
    else :
        print(f"{dot.year} is not a leap year!")
else :
    print(f"{dot.year} is not a leap year!")
