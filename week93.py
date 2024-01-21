import re
class DateError(Exception):
    pass

birthday = input("Enter your date of birth: ",)

day = re.findall("^[0-9][0-9]",birthday)

a=int(day[0])
print(a)
if (a>31 or a<=0):
    raise DateError("Incorrect date")
