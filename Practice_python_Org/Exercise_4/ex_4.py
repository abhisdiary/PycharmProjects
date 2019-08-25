"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""
number = input("Enter the number:")
i = 1
lst = []
while i <= (int(number) / 2):
    if int(number) % i == 0:
        lst.append(i)
    i += 1
lst.append(int(number))
print(lst)
