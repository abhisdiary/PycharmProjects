from datetime import datetime

print("Date Today (date hour:minute:second:microsecond): " + str(datetime.now()))
delta = datetime.now() - datetime(1999, 8, 13)
print("Total days spent since my birthday: " + str(delta.days))
print("Total seconds spent since my birthday: " + str(delta.seconds))
print("This month is: " + str(datetime.now().month))
print("So, this month is: " + str(datetime.now().strftime("%B")) + ", in short: " + str(datetime.now().strftime("%b")))
print("This day is: " + str(datetime.now().strftime("%A")) + ", in short: " + str(datetime.now().strftime("%a")))
print("This time is: " + str(datetime.now().strftime("%p")))
print("This appropriate time is: " + str(datetime.now().strftime("%X")))

# Different format
a_date = datetime.strptime("03.08.1993:20:48", "%d.%m.%Y:%H:%M")
print(a_date)
print(a_date.strftime("%d-%m-%Y %H.%M"))

print("Reference: http://strftime.org/")
