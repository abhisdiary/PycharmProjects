ex1 = input("Guess what my favorite integer is: ")
try:
    if int(ex1) == 7:
        print("That is correct")
    else:
        print("No that is not")
except:
    print("Please run the progeam again and enter an integer.")

"""
There are many other Python's Built_In Exceptions:
Visit: https://docs.python.org/3/library/exceptions.html
"""