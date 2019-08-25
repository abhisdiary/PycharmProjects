# Without Parameter
def ex():
    print("hello world")


ex()


# With Parameter
def single(a):
    print(a)


single(9)


def multiple(a, b, c):
    d = a * b
    print(c, d)


multiple(5, 10, "The result is:")


# Calling Functions Inside Other Functions
def giver(a, b):
    c = a + b
    return c


def taker(d, e):
    output = giver(d, e)
    return output


print(taker(1, 5))
