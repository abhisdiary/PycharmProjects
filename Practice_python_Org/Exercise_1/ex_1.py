"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""
from datetime import datetime

name = input("Please enter your name: ")
age = input("Please enter your age: ")
try:
    if (int(age) > 0) & (int(age) < 100):
        difference = 100 - int(age)
        print(name, "You will be 100 in:", datetime.now().year + difference)
    elif int(age) == 100:
        print("Wow", name, "you've already become 100!")
    elif int(age) > 100:
        difference = int(age) - 100
        print(name, "You became 100 in:", datetime.now().year - difference)
except ValueError:
    print("Enter Age in DIGITS please.")
