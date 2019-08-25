"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
num = input("Enter the number: ")
check = input("Enter the number to check: ")
if int(check) % int(num) == 0:
    print("Yes", check, "is a factor of", num)
else:
    print("NO", check, "is not a factor of", num)
